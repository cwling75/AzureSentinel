import json
import logging
import os
from datetime import datetime

import azure.functions as func

from ..exports_store import ExportsTableStore, ExportsTableNames
from ..azure_sentinel import AzureSentinel
from ..tenable_helper import TenableIO, TenableStatus
from tenable.errors import APIError

connection_string = os.environ['AzureWebJobsStorage']
assets_table_name = ExportsTableNames.TenableAssetExportTable.value
workspace_id = os.environ['WorkspaceID']
workspace_key = os.environ['WorkspaceKey']
log_analytics_uri = os.getenv('LogAnalyticsUri', '')
log_type = 'Tenable_IO_Assets_CL'


def main(msg: func.QueueMessage) -> None:
    logging.info('Python queue trigger function processed a queue item: %s',
                 msg.get_body().decode('utf-8'))
    decoded_message = msg.get_body().decode('utf-8')
    assets_table = ExportsTableStore(connection_string, assets_table_name)

    try:
        export_job_details = json.loads(decoded_message)
        export_job_id = export_job_details.get('exportJobId', '')
        chunk_id = export_job_details.get('chunkId', '')

        if export_job_id == '' or chunk_id == '':
            logging.warn('missing information to process a chunk')
            logging.warn(f'message sent - {decoded_message}')
            raise Exception(
                f'cannot process without export job ID and chunk ID -- found job ID {export_job_id} - chunk ID {chunk_id}')
        else:
            logging.info(
                'using pyTenable client to download asset export job chunk')
            logging.info(
                f'downloading chunk at assets/{export_job_id}/chunks/{chunk_id}')
            tio = TenableIO()
            try:
                chunk = tio.exports.chunk('assets', export_job_id, chunk_id)
                logging.info(
                    f'received a response from assets/{export_job_id}/chunks/{chunk_id}')

                # Send to Azure Sentinel here
                az_sentienl = AzureSentinel(
                    workspace_id, workspace_key, log_type, log_analytics_uri)
                az_code = az_sentienl.post_data(json.dumps(chunk))
                logging.warn(
                    f'Azure Sentinel reports the following status code: {az_code}')

                assets_table.update_if_found(export_job_id, str(chunk_id), {
                    'jobStatus': TenableStatus.finished.value
                })
            except APIError as e:
                logging.warn(
                    f'Failure to retrieve asset data from Tenable. Response code: {e.code} Request ID: {e.uuid} Export Job ID: {export_job_id} Chunk ID: {chunk_id}')
                assets_table.update_if_found(export_job_id, str(chunk_id), {
                    'jobStatus': TenableStatus.failed.value,
                    'tenableFailedRequestId': e.uuid,
                    'tenableFailedRequestStatusCode': e.code
                })
                raise Exception(
                    f'Retrieving from Tenable failed with status code {e.code}')

    except Exception as e:
        assets_table.update_if_found(export_job_id, str(chunk_id), {
            'jobStatus': TenableStatus.failed.value
        })
        logging.warn(
            f'there was an error processing chunks. message sent - {decoded_message}')
        logging.warn(e)
        raise e
