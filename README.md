# proxy_provider_generator
use to generate proxy-provider used in Clash from subscribe url

## Quick Start  
create `timer.timer` and `provider_update.service` in `/etc/systemd/system/`  

### template
`timer.timer`
```
[Unit]
Description=Runs clash proxy-provider update periodly

[Timer]
OnUnitActiveSec=72h
Unit=provider_update.service

[Install]
WantedBy=multi-user.target
```
Set the OnUnitActiveSec yourself.  

`provider_update.service`
```
[Unit]
Description=update clash proxy provider
[Service]
Type=simple
Restart=on-failure
User=usrname
Group=usrname
WorkingDirectory=/etc/Clash-Meta/proxy_providers/
ExecStart=/home/${username}/mambaforge/envs/ten/bin/python /home/${username}/Engineering/parse_to_provider/main.py

[Install]
WantedBy=multi-user.target
```

```
sudo systemctl daemon-reload  
sudo systemctl enable timer.timer 
sudo systemctl start timer.timer
```
