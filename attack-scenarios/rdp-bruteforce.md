# RDP Brute-Force Detection Scenario

This scenario is planned for the lab.

The intended traffic path is:

Linux attacker `10.1.0.3`
-> Windows endpoint `10.1.0.2`

The automation should extract the actual remote/source IP from the security
event rather than confusing it with the monitored endpoint IP.

DFIR-IRIS should use the `ip-src` IOC type for the remote source IP.

Do not test against external systems.
