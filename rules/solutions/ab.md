
#### Elastic Defend

|Rule name|Description|Source|
|---|---|---|
|Endpoint Security – Elastic Defend|Surfaces all Elastic Defend EDR detections/preventions as SIEM alerts (one rule covers all Defend signals).|A,B|

---

#### Windows AD

|Rule name|Description|Source|
|---|---|---|
|User account exposed to Kerberoasting|Flags accounts vulnerable to Kerberoasting (e.g., RC4‑HMAC) to reduce offline cracking risk.|B|
|FirstTime Seen Account Performing DCSync|First-ever replication behavior by an account (credential access red flag).|A,B|
|Potential Credential Access via DCSync|Patterns of secret replication access (4662/replication) suggesting DCSync.|A|
|Remote Computer Account DnsHostName Update|Suspicious changes to computer account DNS hostname (persistence/lateral).|B|
|Suspicious Access to LDAP Attributes|Enumeration of sensitive LDAP attributes (discovery/credential prep).|B|
|Group Policy Abuse for Privilege Addition|Privilege grants via GPO across many hosts (high impact, uncommon admin action).|A,B|
|Service Creation via Local Kerberos Authentication|Service creation authenticated via Kerberos indicating privilege abuse.|B|
|Potential ADIDNS Poisoning via Wildcard Record Creation|Wildcard DNS records in ADIDNS used for redirection/relay.|B|
|Potential Privileged Escalation via SamAccountName Spoofing|Spoofed `SamAccountName` to impersonate privileged accounts.|B|
|Modification of the msPKIAccountCredentials|Changes to cert/key attributes for silent persistence or escalation.|B|
|Kerberos Pre-authentication Disabled for User|Disabling pre-auth allows offline password cracking; rare and risky.|A,B|
|Scheduled Task Execution at Scale via GPO|GPO‑pushed scheduled tasks for mass execution / lateral ops.|A,B|
|User Added to Privileged Group in Active Directory|Immediate domain privilege escalation (e.g., Domain Admins).|A,B|
|Creation of a DNS-Named Record|New AD‑integrated DNS records—suspicious when frequent/unexpected.|B|
|Potential Relay Attack against a Domain Controller|Relay behavior targeting DCs to impersonate accounts.|B|
|Potential Shadow Credentials added to AD Object|Rogue key added to AD object enabling passwordless persistence.|A|
|AdminSDHolder Backdoor|ACL tampering on AdminSDHolder to persist admin rights.|A|
|WRITEDAC Access on Active Directory Object|Unexpected WriteDACL on sensitive directory objects.|A|
|Sensitive Privilege SeEnableDelegationPrivilege assigned to a User|Delegation rights that enable powerful impersonation.|A|

---

#### Windows

|Rule name|Description|Source|
|---|---|---|
|Windows Event Logs Cleared|Clearing logs to hide activity (PowerShell/wevutil/wmic).|A,B|
|Disable Windows Firewall Rules via Netsh|Disabling firewall via `netsh` (defense evasion).|B|
|Disable Windows Event and Security Logs Using Built-in Tools|Turning off logging via native tools/APIs.|B|
|RDP Enabled via Registry|Silent enabling of Remote Desktop via registry change.|A,B|
|Disabling User Account Control via Registry Modification|Lowering/turning off UAC via registry.|B|
|Volume Shadow Copy Deletion via VssAdmin|Deleting restore points—common ransomware precursor.|A|
|Windows Defender Disabled via PowerShell|Disabling built‑in AV via Set‑MpPreference, etc.|A|
|Remote Windows Service Installed|Remote service creation (classic lateral movement).|A|
|Remote Scheduled Task Creation via RPC|Creating tasks on remote systems for execution.|A|
|PsExec Network Connection|Remote execution over SMB/admin shares via PsExec.|A|
|LSASS Memory Dump Creation|Dumping LSASS for credential theft (comsvcs/procdump/etc.).|A|
|Suspicious Windows PowerShell Arguments|Encoded/compressed/bypass invocations—common malicious patterns.|A|
|Machine Learning Detected a Suspicious Windows Event with a High Malicious Probability Score|ML score flags likely‑malicious Windows events (investigate with Process Analyzer).|B|
|Anomalous Windows Process Creation|Baseline deviation in process creation; useful on stable servers.|B|
|Unusual Windows Service|Unusual service creation/modification outside normal patterns.|B|
|Unusual Windows Network Activity|Outlier network behavior per host; best on servers with steady baselines.|B|
|Unusual Windows Remote User|Unexpected RDP/remote logins by user/host/time profile.|B|

---

#### Network

|Rule name|Description|Source|
|---|---|---|
|SMB (Windows File Sharing) Activity to the Internet|SMB traffic to external IPs—should rarely leave LAN; strong indicator of misconfig or exfil path.|B|
|Statistical Model Detected C2 Beaconing Activity with High Confidence|Periodic command‑and‑control beacon patterns with low FP.|A|
|Machine Learning Detected a DNS Request With a High DGA Probability Score|Algorithmically generated domains (malware infra).|A|
|Potential Network Scan Detected|Fan‑out connection patterns indicating scanning/recon.|A|
|Potential SYN-Based Port Scan Detected|SYN‑only scanning behavior; complements generic scan rule.|A|
|DNS Tunneling|Covert data over DNS (length/frequency/ratio indicators).|A|
|Rare SMB Connection to the Internet|“Rare” outbound SMB from a host—behavioral rarity lens on SMB egress.|A|

---

#### Threat Intel

|Rule name|Description|Source|
|---|---|---|
|Threat Intel IP Address Indicator Match|Host contacted a known‑bad IP (from TI feeds).|A,B|
|Threat Intel URL Indicator Match|Access to known‑malicious URLs.|A,B|
|Threat Intel Hash Indicator Match|File hash matches known malware.|A,B|
|Threat Intel Windows Registry Indicator Match|Registry indicators associated with malware/persistence.|A,B|

---

#### Linux

|Rule name|Description|Source|
|---|---|---|
|Linux User Added to Privileged Group|Sudden membership in sudo/root groups on servers.|A|
|Successful SSH Authentication from Unusual IP Address|SSH logins from atypical IPs/ASNs for that user/host.|A|
|Potential Linux Credential Dumping via Proc Filesystem|Suspicious reads of other processes’ memory/maps.|A|
|Potential Privilege Escalation via OverlayFS|Detects OverlayFS privilege‑escalation exploitation.|A|
|SUID/SGID Bit Set|New/modified binaries with setuid/setgid—priv‑esc vector.|A|
