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
