# RecordedFuture - Import Indicators Logic Apps and IOC Enrichment Playbook templates

## Table of Contents

1. [Overview](#overview)
1. [Import To Sentinel - Deployment](#deployimporttosentinel)
1. [IP - Actively Communicating C&C Server - Indicator Processor - Deployment](#deployIPindicatorprocessor)
1. [Domain - C&C DNS Name - Indicator Processor - Deployment](#deployDOMAINindicatorprocessor)
1. [URL - Recently Reported by Insikt Group - Indicator Processor - Deployment](#deployURLindicatorprocessor)
1. [HASH - Observed in Underground Virus Test Sites - Indicator Processor - Deployment](#deployHASHindicatorprocessor)
1. [IOC (IP, Domain, URL, Hash) Enrichment Playbook - Deployment](#deployIOCEnrichment)

<a name="overview">

# Overview

Recorded Future is the world’s largest provider of intelligence for enterprise security. By combining persistent and pervasive automated data collection and analytics with human analysis, Recorded Future delivers intelligence that is timely, accurate, and actionable.

<a name="deployimporttosentinel">

# Deployment

Due to internal Microsoft Logic Apps dependencies, please deploy first the ImportToSentinel playbook before any of the IndicatorProcessor one. This playbooks will serve via the Microsoft Batching mechanism all of the IndicatorProcessor playbooks, for optimizition of the indicator deployment process.

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FSolutions%2FRecorded%20Future%2FPlaybooks%2FRecordedFuture-ImportToSentinel.json)
[![Deploy to Azure Gov](https://aka.ms/deploytoazuregovbutton)](https://portal.azure.us/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FSolutions%2FRecorded%20Future%2FPlaybooks%2FRecordedFuture-ImportToSentinel.json)

## Detection - IP - Actively Communicating C&C Server

<a name="deployIPindicatorprocessor">

This playbook leverages the Recorded Future API to automate the ingestion of Recorded Future [Actively Communicating C&C Server IP RiskList](https://support.recordedfuture.com/hc/en-us/articles/115000894448-IP-Address-Risk-Rules), into the ThreatIntelligenceIndicator table, for detection (alert) actions in Microsoft Azure Sentinel. For additional information please visit [Recorded Future](https://www.recordedfuture.com/integrations/azure/).

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FSolutions%2FRecorded%20Future%2FPlaybooks%2FRecordedFuture-IP-Actively_Communicating_C2_Server-IndicatorProcessor.json)
[![Deploy to Azure Gov](https://aka.ms/deploytoazuregovbutton)](https://portal.azure.us/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FSolutions%2FRecorded%20Future%2FPlaybooks%2FRecordedFuture-IP-Actively_Communicating_C2_Server-IndicatorProcessor.json)

## Detection - Domain - C&C DNS Name

<a name="deployDOMAINindicatorprocessor">

This playbook leverages the Recorded Future API to automate the ingestion of Recorded Future [C&C DNS Name Domain RiskList](https://support.recordedfuture.com/hc/en-us/articles/115003793388-Domain-Risk-Rules), into the ThreatIntelligenceIndicator table, for detection (alert) actions in Microsoft Azure Sentinel. For additional information please visit [Recorded Future](https://www.recordedfuture.com/integrations/azure/).

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FSolutions%2FRecorded%20Future%2FPlaybooks%2FRecordedFuture-DOMAIN-C2_DNS_Name-IndicatorProcessor.json)
[![Deploy to Azure Gov](https://aka.ms/deploytoazuregovbutton)](https://portal.azure.us/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FSolutions%2FRecorded%20Future%2FPlaybooks%2FRecordedFuture-DOMAIN-C2_DNS_Name-IndicatorProcessor.json)

## Detection - URL - Recently Reported by Insikt Group

<a name="deployURLindicatorprocessor">

This playbook leverages the Recorded Future API to automate the ingestion of Recorded Future [Recently Reported by Insikt Group URL RiskList](https://support.recordedfuture.com/hc/en-us/articles/115010052768-URL-Risk-Rules), into the ThreatIntelligenceIndicator table, for detection (alert) actions in Microsoft Azure Sentinel. For additional information please visit [Recorded Future](https://www.recordedfuture.com/integrations/azure/).

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FSolutions%2FRecorded%20Future%2FPlaybooks%2FRecordedFuture-URL-Recently_Reported_by_Insikt_Group-IndicatorProcessor.json)
[![Deploy to Azure Gov](https://aka.ms/deploytoazuregovbutton)](https://portal.azure.us/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FSolutions%2FRecorded%20Future%2FPlaybooks%2FRecordedFuture-URL-Recently_Reported_by_Insikt_Group-IndicatorProcessor.json)

## Detection - Hash - Observed in Underground Virus Testing Sites

<a name="deployHASHindicatorprocessor">

This playbook leverages the Recorded Future API to automate the ingestion of Recorded Future [Observed in Underground Virus Testing Sites Hash RiskList](https://support.recordedfuture.com/hc/en-us/articles/115000846167-Hash-Risk-Rules), into the ThreatIntelligenceIndicator table, for detection (alert) actions in Microsoft Azure Sentinel. For additional information please visit [Recorded Future](https://www.recordedfuture.com/integrations/azure/).

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FSolutions%2FRecorded%20Future%2FPlaybooks%2FRecordedFuture-HASH-Observed_in_Underground_Virus_Test_Sites-IndicatorProcessor.json)
[![Deploy to Azure Gov](https://aka.ms/deploytoazuregovbutton)](https://portal.azure.us/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FSolutions%2FRecorded%20Future%2FPlaybooks%2FRecordedFuture-HASH-Observed_in_Underground_Virus_Test_Sites-IndicatorProcessor.json)

## Response (Enrichment) - IP, Domain, Hash, URL

<a name="deployIOCEnrichment">

This playbook leverages the Recorded Future API to automatically enrich the IP, Domain, Url and Hash indicators, found in incidents, with the following Recorded Future context: Risk Score, Risk Rules and Link to Intelligence Card. The enrichment content will be posted as a comment in the Sentinel incident. For additional information please visit [Recorded Future](https://www.recordedfuture.com/integrations/azure/) 

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FSolutions%2FRecorded%20Future%2FPlaybooks%2FRecordedFuture-IOC_Enrichment(IP_Domain_URL_Hash).json)
[![Deploy to Azure Gov](https://aka.ms/deploytoazuregovbutton)](https://portal.azure.us/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FSolutions%2FRecorded%20Future%2FPlaybooks%2FRecordedFuture-IOC_Enrichment(IP_Domain_URL_Hash).json)
