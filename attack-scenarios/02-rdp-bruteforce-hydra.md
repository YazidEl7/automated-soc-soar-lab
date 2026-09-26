# Scenario 2: RDP Brute-Force & Active Response

## 🎯 Objective
Validate automated detection of high-frequency logon failures and Human-in-the-Loop firewall IP isolation via pfSense[cite: 1].

## 💻 Execution Steps
Run Hydra from Linux Attacker (`10.1.0.3`) targeting RDP on Windows Host (`10.1.0.2`)[cite: 1, 3]:
```bash
hydra -l Administrator -P /usr/share/wordlists/rockyou.txt rdp://10.1.0.2 -t 4
```

## 🔍 Active Response Pipeline Steps

1. Wazuh Detection: Event ID 4625 triggers rule 60122, accumulated failures trigger rule 100001[cite: 1].

1. n8n Triage: Webhook captures source IP 10.1.0.3[cite: 1, 3].

1. Interactive Prompt: Discord notification delivered to SOC team with [APPROVE BLOCK] action button[cite: 1].

1. Enforcement: Upon approval, n8n issues API/SSH command adding 10.1.0.3 to SOC_Blocked_IPs alias on pfSense, severing host connectivity[cite: 1, 3].
