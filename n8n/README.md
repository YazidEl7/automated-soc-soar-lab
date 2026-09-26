# n8n Automation

The current workflow follows this sequence:

Wazuh webhook
-> normalization
-> IOC extraction
-> VirusTotal enrichment
-> LLM analysis
-> DFIR-IRIS case
-> DFIR-IRIS IOC creation

Planned next stages:

-> Discord
-> human approval
-> pfSense automated response
