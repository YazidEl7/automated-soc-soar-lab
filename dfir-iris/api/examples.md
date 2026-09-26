# DFIR-IRIS API Examples

## Create case

The n8n workflow calls the DFIR-IRIS API to create an incident/case.

Use your local API base URL and keep the API token in n8n credentials or a secret
store rather than hard-coding it in the workflow.

## Create IOC

The lab maps normalized IOC types to DFIR-IRIS IOC type IDs.

Current lab mappings:

| IOC type | DFIR-IRIS type ID |
|---|---:|
| filename | 37 |
| ip-any | 76 |
| ip-src | 79 |
| md5 | 90 |
| sha1 | 111 |
| sha256 | 113 |

For an affected endpoint IP, `ip-any` is used in the current Mimikatz case.
For a real remote source IP in the planned RDP scenario, `ip-src` is appropriate.
