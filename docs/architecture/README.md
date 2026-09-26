# Architecture

## Logical flow

The lab is organized into network/security monitoring, automation, and incident-response layers.

1. Endpoints generate telemetry.
2. Wazuh collects and analyzes endpoint events.
3. n8n receives selected Wazuh alerts.
4. n8n extracts and enriches indicators.
5. An LLM analyzes the supplied evidence.
6. DFIR-IRIS stores the incident and observables.
7. Future steps add analyst notification, approval, and automated containment.

Recommended diagrams for this folder:

- architecture-diagram.png
- network-topology.png
- data-flow.png
