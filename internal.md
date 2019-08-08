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
