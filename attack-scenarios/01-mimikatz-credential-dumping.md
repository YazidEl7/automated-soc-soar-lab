# Scenario 1: Credential Dumping via Mimikatz

## 🎯 Objective
Validate the automated SOC/SOAR detection, threat intelligence enrichment, AI triage, and incident logging pipeline when Mimikatz process execution occurs.

## 💻 Execution Steps
1. Open PowerShell with Administrative privileges on Windows Target (`10.1.0.2`)[cite: 1, 3].
2. Execute MimikatzLSASS dump command:
   ```powershell
   .\mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" exit

## 🔍 Automation Pipeline StepsSysmon / Wazuh: 
1. Sysmon Event ID 1 captures process execution and flags rule 100002.   
1. n8n Ingestion: Custom webhook integration passes JSON alert to n8n.   
1. IoC Enrichment: SHA256 hash extracted and queried against VirusTotal API.   
1. AI Synthesis: Gemini LLM evaluates event context and flags execution as Critical.   
1. Incident Tracking: Case automatically created in DFIR-IRIS and alert posted to Discord.
