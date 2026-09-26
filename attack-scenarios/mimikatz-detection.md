# Mimikatz Detection Scenario

## Objective

Demonstrate detection and automated triage of a suspicious Mimikatz-related
process execution on the Windows lab endpoint.

## Telemetry path

Windows endpoint
-> Sysmon Event ID 1
-> Wazuh agent
-> Wazuh custom rule `100002`
-> n8n
-> VirusTotal / LLM
-> DFIR-IRIS

## Indicators demonstrated

The workflow can normalize:

- SHA-256
- SHA-1
- MD5
- filename
- affected endpoint IP

## Safety

Run this only in the isolated lab. Do not use credential-dumping tooling
against systems or accounts that you do not own or have explicit authorization
to test.
