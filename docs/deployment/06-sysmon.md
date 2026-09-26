# 06 - Sysmon

Sysmon provides endpoint process and system telemetry for the Windows lab.

The Wazuh agent can collect the Sysmon Operational event channel:

```xml
<localfile>
  <location>Microsoft-Windows-Sysmon/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
```

Restart the Wazuh agent after changing its configuration.
