# Automated SOC/SOAR Security Operations Laboratory (Federator Project)

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Architecture](https://img.shields.io/badge/Architecture-SOAR%20%7C%20SIEM%20%7C%20XDR%20%7C%20LLM-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

## Executive Overview
The **Federator Project** is an end-to-end automated Security Operations Center (SOC) and Security Orchestration, Automation, and Response (SOAR) architecture designed to eliminate alert fatigue, accelerate incident response, and enforce automated network containment.

By unifying **Wazuh (SIEM/XDR)**, **Sysmon**, **Suricata (NIDS)**, **n8n (SOAR)**, **VirusTotal (Threat Intelligence)**, **Google Gemini LLM (AI Analysis)**, **DFIR-IRIS (Incident Management)**, and **pfSense (Firewall Enforcement)**, this laboratory achieves:
* **MTTD (Mean Time To Detect):** `< 5 minutes`
* **MTTR (Mean Time To Respond):** `< 1 minute` (automated triage and active response)
* **Human-in-the-Loop Validation:** Interactive approval workflows via Discord Webhooks prior to active IP blocking on pfSense.

---

## 🏗️ Architecture & Data Flow
```
+-----------------------------------------------------------------------------------+
|                                  COLLECTION LAYER                                 |
|  +--------------------+   +-------------------+   +----------------------------+  |
|  | Windows Endpoint   |   | Linux Attacker    |   | Suricata NIDS              |  |
|  | (Sysmon + Agent)   |   | (Hydra/Mimikatz)  |   | (Network Inspection)       |  |
|  +---------+----------+   +---------+---------+   +--------------+-------------+  |
+------------|------------------------|----------------------------|----------------+
|                        |                            |
+------------------------+----------------------------+
| (Event Logs & Telemetry)
v
+-----------------------------------------------------------------------------------+
|                              CORRELATION & SIEM LAYER                             |
|  +-----------------------------------------------------------------------------+  |
|  | Wazuh SIEM/EDR (192.168.100.233)                                           |  |
|  |  - Custom Local Rules (Rule 100002: Mimikatz, Rule 60122: RDP Brute-Force)  |  |
|  |  - Active Integration Script forwarding JSON payloads to n8n Webhook       |  |
|  +-------------------------------------+---------------------------------------+  |
+----------------------------------------|------------------------------------------+
| (HTTP POST Webhook)
v
+-----------------------------------------------------------------------------------+
|                              SOAR & ORCHESTRATION LAYER                           |
|  +-----------------------------------------------------------------------------+  |
|  | n8n SOAR Orchestrator (192.168.100.236:5678)                               |  |
|  |  1. Webhook Trigger & IoC Extraction (IPs, File Hashes)                     |  |
|  |  2. VirusTotal Reputation API Query                                         |  |
|  |  3. Gemini LLM Contextual Threat Assessment & Triage Report                 |  |
|  |  4. DFIR-IRIS Case Creation via REST API                                     |  |
|  |  5. Discord Interactive Notification (Approve Block / Reject Ignore)        |  |
|  +-------------------------------------+---------------------------------------+  |
+----------------------------------------|------------------------------------------+
| (Approved Remediation Request)
v
+-----------------------------------------------------------------------------------+
|                              ENFORCEMENT & DFIR LAYER                             |
|  +----------------------------------+    +-------------------------------------+  |
|  | pfSense Firewall Gateway         |    | DFIR-IRIS Incident Case Repository  |  |
|  |  - Dynamic IP Blocking (Alias)   |    |  - Complete Audit Trail & Timeline   |  |
|  +----------------------------------+    +-------------------------------------+  |
+-----------------------------------------------------------------------------------+
```
## 🌐 Network Addressing Plan

| Component / Host | IP Address | Subnet / Interface | Description |
| :--- | :--- | :--- | :--- |
| **pfSense Gateway** | `10.0.2.15` / `192.168.100.10` / `10.1.0.1` | WAN / DMZ / LAN | Router & Firewall Gateway |
| **Windows Client** | `10.1.0.2` | LAN (`10.1.0.0/24`) | Monitored Target Endpoint (Sysmon + Wazuh Agent) |
| **Linux Attacker** | `10.1.0.3` | LAN (`10.1.0.0/24`) | Attack Machine (Kali / Ubuntu with Hydra & Mimikatz) |
| **Wazuh Server** | `192.168.100.233` | DMZ (`192.168.100.0/24`) | SIEM / XDR Manager & Indexer |
| **DFIR-IRIS Server** | `192.168.100.235` | DMZ (`192.168.100.0/24`) | Incident Case Management Platform[cite: 3] |
| **n8n SOAR Server** | `192.168.100.236` | DMZ (`192.168.100.0/24`) | Workflow Automation & AI Agent Host[cite: 3] |
| **Suricata NIDS** | `192.168.100.237` | DMZ (`192.168.100.0/24`) | Network Intrusion Detection System |
---

## 📋 Prerequisites & System Requirements

### Hardware Requirements
* **RAM:** Minimum 24 GB 
* **CPU:** 4 Cores / 8 Threads minimum
* **Disk Space:** 150 GB free SSD storage

### Software & API Requirements
* **Hypervisor:** VMware Workstation Pro / ESXi / VirtualBox
* **Docker Engine & Docker Compose** (installed on n8n/DFIR-IRIS host)
* **Active API Keys:**
  * VirusTotal API Key
  * Google Gemini API Key
  * Discord Bot / Webhook URL

## 📂 Repository Structure
```
├── docker-compose.yml              # Deployment file for n8n & DFIR-IRIS services
├── .env.example                    # Environment variables template
├── attack-scenarios/
│   ├── 01-mimikatz-credential-dumping.md # Mimikatz dumping workflow & detection
│   └── 02-rdp-bruteforce-hydra.md        # Hydra RDP brute force & firewall containment
├── dfir-iris/                      # DFIR-IRIS configuration & Python API scripts
├── docs/                           # Full technical deployment & architecture documentation
│   ├── architecture/               # 3-Tier SOAR design & data flow diagrams
│   └── deployment/                 # Step-by-step installation guides (01 through 09)
├── n8n/                            # SOAR workflow exports & AI prompts
│   ├── prompts/                    # Gemini LLM system prompt
│   └── workflows/                  # Complete n8n workflow JSON export
├── pfsense/                        # Network configuration, firewall rules & active response API scripts
├── suricata/                       # Suricata NIDS rule definitions & YAML config
├── wazuh/                          # Custom Wazuh detection rules & n8n integration script
└── windows/                        # Windows Sysmon & Wazuh Agent channel configuration
```
## 📸 Visual Evidence & Screenshots

The end-to-end automated detection, enrichment, and containment pipeline is verified across all core platform components:

| Feature / Demonstration | Evidence Screenshot | Description |
| :--- | :--- | :--- |
| **Wazuh Detection** | `![Wazuh Alert](screenshots/01-wazuh-mimikatz-alert.png)` | Wazuh dashboard displaying Rule `100002` execution triggered by Sysmon Event ID 1. |
| **n8n Automation** | `![n8n Execution](screenshots/02-n8n-workflow-execution.png)` | n8n green execution tree showing JSON ingestion & Gemini LLM API response. |
| **DFIR-IRIS Case** | `![DFIR-IRIS Ticket](screenshots/03-dfir-iris-case.png)` | Automatically created incident ticket in DFIR-IRIS with extracted IOCs. |
| **Discord Interactive** | `![Discord Webhook](screenshots/04-discord-interactive-approval.png)` | Discord notification showing threat details and the interactive **[APPROVE BLOCK]** button. |
| **pfSense Enforcement** | `![pfSense Alias](screenshots/05-pfsense-blocked-alias.png)` | pfSense UI showing `10.1.0.3` dynamically added to the `SOC_Blocked_IPs` firewall alias table. |

## ⚡ Quick Start Guide

### 1. Clone & Setup Environment
git clone [https://github.com/yazidel7/automated-soc-soar-lab.git](https://github.com/yazidel7/automated-soc-soar-lab.git)
```bash
cd automated-soc-soar-lab
cp .env.example .env
# Edit .env with your specific API keys (VirusTotal, Gemini, DFIR-IRIS, Discord)
```

### 2. Deploy Containerized Stack (n8n & DFIR-IRIS)
```
docker-compose up -d
```
Access services at:

- n8n Web UI: http://192.168.100.236:5678
- DFIR-IRIS: https://192.168.100.235

### 3. Deploy Wazuh SIEM Rules & Integration

Copy custom rules and integration script to your Wazuh Manager:
```
cp wazuh/rules/local_rules.xml /var/ossec/etc/rules/local_rules.xml
cp wazuh/integrations/custom-n8n /var/ossec/integrations/custom-n8n
chmod 750 /var/ossec/integrations/custom-n8n
chown root:wazuh /var/ossec/integrations/custom-n8n
systemctl restart wazuh-manager
```
### 4. Import n8n Workflow
1. Log into n8n (http://192.168.100.236:5678).
2. Go to Workflows -> Import from File.
3. Select n8n/workflows/automated-soc-soar-workflow.json.
4. Configure credentials for VirusTotal, Gemini LLM, DFIR-IRIS, and Discord Webhook.
5. Activate the workflow!

## Scenario 1: Credential Dumping (Mimikatz)
- Attack: mimikatz.exe "privilege::debug" "ts::logonpasswords" executed on 10.1.0.2.   
- Detection: Windows Sysmon Event ID 1 -> Wazuh Local Rule 100002.   
- Automation: n8n extracts executable hash -> VirusTotal lookup (Malware/Trojan) -> Gemini LLM report -> Case generated in DFIR-IRIS -> Discord alert sent.

## Scenario 2: RDP Brute-Force Attack (Hydra)
- Attack: hydra -l Administrator -P passlist.txt rdp://10.1.0.2 executed from 10.1.0.3.   
- Detection: Windows Security Event ID 4625 -> Wazuh Rule 60122.   
- Automation: n8n extracts source IP (10.1.0.3) -> Discord notification with "APPROVE BLOCK" button -> Analyst approves -> SSH request to pfSense adds 10.1.0.3 to SOC_Blocked_IPs alias -> Traffic isolated[cite: 1, 3].

## 🎓 Authors & Academic Credits

- Students: Abdelaziz O, YazidEl7, Akram B, Achraf EL[cite: 3]

- Academic Supervisor: Dr. Hachim FALL[cite: 3]

- Institution: SUPMTI (École Supérieure de Management, de Télécommunication et d'Informatique)[cite: 3]

- Program: 5th Year Computer Engineering - Cybersecurity Option (AY 2025-2026)[cite: 3]


### 📜 License

Distributed under the MIT License. See LICENSE for more information.
