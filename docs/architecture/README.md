# 🏛️ Lab Architecture & MITRE ATT&CK Mapping

This document details the multi-tier telemetry collection, correlation, orchestration, and active response framework for the **Federator Project**.

---

## 3-Tier SOAR Architecture
[ Tier 1: Telemetry Collection ]
├── Windows Endpoint (Sysmon Event ID 1, 3, 10)
├── Linux Attacker (Controlled Ingress Attacks)
└── Suricata NIDS (Network Inspection & Flood Detection)
│
▼
[ Tier 2: Correlation & Orchestration ]
├── Wazuh SIEM/EDR (Rule Matching & JSON Webhook Forwarding)
└── n8n SOAR Engine (VirusTotal Enrichment & Gemini LLM Analysis)
│
▼
[ Tier 3: Incident Management & Active Containment ]
├── DFIR-IRIS (Automatic Ticket Generation & IOC Logging)
├── Discord Webhook (Human-in-the-Loop Approval Request)
└── pfSense Gateway (REST API Enforcement -> SOC_Blocked_IPs Alias)

---

## 🎯 MITRE ATT&CK Mapping Matrix

| Attack Scenario | Tactic | Technique Name | MITRE ID | Telemetry Source | Wazuh Detection | Automated Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Mimikatz Process Execution** | Credential Access | OS Credential Dumping: LSASS Memory | `T1003.001` | Sysmon Event ID 1 | Rule `100002` | VirusTotal Hash Query, Gemini AI Triage, DFIR-IRIS Case Creation |
| **RDP Brute-Force Attack** | Credential Access | Brute Force: Password Guessing | `T1110.001` | Windows Security Event ID 4625 / Suricata | Rule `60122` / `100001` | Discord Interactive Alert, pfSense Dynamic IP Block (`SOC_Blocked_IPs`) |
| **SMB Lateral Ingress** | Lateral Movement | Remote Services: SMB/Windows Admin Shares | `T1021.002` | Suricata NIDS / Sysmon Event ID 3 | Rule `100003` | Incident Ticket Generation, Endpoint Isolation Alert |
