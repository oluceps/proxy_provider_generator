# proxy_provider_generator
use to generate proxy-provider used in Clash from subscribe url
# [Clash.Meta](https://github.com/MetaCubeX/Clash.Meta) had supported get proxy provider directly from general subscribe link.
## Quick Start  
### clone the repository  
```
git clone https://github.com/oluceps/proxy_provider_generator.git 
```
### Download requirements  
```
pip3 install -r requirements.txt
```
### edit `config.toml` file  
```
[subscribe]
name = "url"

[work_dir]
clash = "/etc/Clash-Meta/proxy_providers/"
```
Fill `clash` with the path stores clash proxy-provider  
Subset of `[subscribe]` could be multipy objects:  
```
sub1 = "url1"
sub2 = "url2"
```
proxy-provider will soon be generated to the dir specified with `python3 main.py`  


## auto task
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
