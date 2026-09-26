#!/usr/bin/env python3
"""
pfSense Active Response IP Containment Script
Interacts with the pfSense REST API to dynamically append malicious IP addresses 
to the 'SOC_Blocked_IPs' firewall alias.
"""

import sys
import os
import requests
import urllib3

# Suppress SSL warnings for self-signed laboratory certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# API Configuration
PFSENSE_IP = os.getenv("PFSENSE_IP", "192.168.100.10")
API_KEY = os.getenv("PFSENSE_API_KEY", "your_pfsense_api_key")
API_SECRET = os.getenv("PFSENSE_API_SECRET", "your_pfsense_api_secret")
ALIAS_NAME = os.getenv("PFSENSE_BLOCK_ALIAS", "SOC_Blocked_IPs")

def add_ip_to_alias(target_ip):
    url = f"https://{PFSENSE_IP}/api/v1/firewall/alias/item"
    headers = {
        "Authorization": f"Bearer {API_KEY}:{API_SECRET}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": ALIAS_NAME,
        "address": target_ip,
        "detail": "Automated SOAR Active Response Block via n8n"
    }

    try:
        response = requests.post(url, headers=headers, json=payload, verify=False, timeout=10)
        
        if response.status_code in [200, 201]:
            print(f"[+] Successfully added {target_ip} to pfSense alias '{ALIAS_NAME}'.")
            
            # Apply firewall rules to enforce immediate block
            apply_url = f"https://{PFSENSE_IP}/api/v1/firewall/apply"
            requests.post(apply_url, headers=headers, verify=False, timeout=10)
            print("[+] pfSense firewall rules reloaded successfully.")
            return True
        else:
            print(f"[-] Failed to update pfSense alias. HTTP {response.status_code}: {response.text}")
            return False

    except Exception as err:
        print(f"[!] Exception occurred while communicating with pfSense API: {str(err)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 block_ip.py <TARGET_IP>")
        sys.exit(1)

    ip_address = sys.argv[1]
    add_ip_to_alias(ip_address)
