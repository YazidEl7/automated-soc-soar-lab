# Automated SOC / SOAR Lab

A VMware-based cybersecurity lab demonstrating security monitoring, alert enrichment,
incident management, and SOAR-style automation using open-source tools.

## Architecture

Main components:

- pfSense — firewall/router and network segmentation
- Wazuh — SIEM/XDR-style monitoring and alerting
- Windows endpoint — monitored workstation
- Sysmon — Windows process and system telemetry
- Linux attacker VM — controlled attack simulations
- n8n — workflow automation / SOAR orchestration
- VirusTotal — IOC enrichment
- LLM — alert analysis and response recommendations
- DFIR-IRIS — incident and IOC management
- Suricata — optional network IDS component

## Lab Network

| Component | IP address | Role |
|---|---:|---|
| pfSense | 192.168.100.10 / 10.1.0.1 | Firewall / router |
| Windows Client | 10.1.0.2 | Monitored endpoint |
| Linux Attacker | 10.1.0.3 | Controlled attack source |
| Wazuh | 192.168.100.233 | SIEM / monitoring |
| DFIR-IRIS | 192.168.100.235 | Incident response |
| n8n | 192.168.100.236 | SOAR automation |
| Suricata | 192.168.100.237 | Network IDS (optional) |

## Implemented Workflow

```text
Windows + Sysmon
       |
       v
     Wazuh
       |
       v
      n8n
       |
       +--> IOC extraction
       |
       +--> VirusTotal enrichment
       |
       +--> LLM analysis
       |
       +--> DFIR-IRIS case
       |
       +--> DFIR-IRIS IOCs
       |
       +--> Discord notification        [next]
       |
       +--> Human approval              [next]
       |
       +--> pfSense automated response   [next]
```

## Current Project Status

### Implemented

- VMware lab architecture
- pfSense network setup
- Wazuh server
- Windows Wazuh agent
- Sysmon telemetry
- Custom Wazuh rule `100002`
- Wazuh -> n8n webhook integration
- Alert normalization
- IOC extraction
- VirusTotal enrichment
- LLM-based alert analysis
- DFIR-IRIS case creation
- DFIR-IRIS IOC creation

### Planned / In Progress

- Discord notification
- Human approval step
- Automated pfSense blocking
- RDP brute-force scenario
- Suricata integration

## Detection Scenario

The first demonstrated scenario is controlled detection of a Mimikatz-related process execution on
the Windows endpoint.

Wazuh receives Sysmon Event ID 1 telemetry and applies custom detection logic. The resulting alert
is sent to n8n, where the workflow normalizes the alert, extracts indicators, enriches the file
hash with VirusTotal, asks an LLM to analyze the evidence, and creates an incident in DFIR-IRIS.

## Security / Privacy

This repository is intended for a controlled cybersecurity lab.

Do **not** commit:

- API keys
- passwords
- webhook URLs containing secrets
- n8n credentials
- DFIR-IRIS API tokens
- VirusTotal API keys
- LLM API keys
- private SSH keys
- pfSense credentials
- VMware VM files
- Docker volumes
- Windows event logs containing personal data
- malware binaries

Use the example configuration files in this repository and keep real values in local `.env` files
or the corresponding secret/credential systems.

## Suggested GitHub Repository

Repository name:

`automated-soc-soar-lab`

The structure intentionally separates architecture, deployment notes, Wazuh rules, n8n workflow
documentation, DFIR-IRIS API examples, and attack scenarios.
