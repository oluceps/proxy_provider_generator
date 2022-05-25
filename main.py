# coding: UTF-8
from requests.api import request
import yaml
import requests
import toml

tml = toml.loads(open("/home/rito/Engineering/parse_to_provider/config.toml", 'r').read())

location = tml.get("work_dir").get('clash')
print(f"proxy_providers will be written to {location}")
headers = {'user-agent': 'clash'}

def gen_provider():
    for i in tml.get('subscribe').keys():
        curr_config = yaml.safe_load(requests.get(tml.get('subscribe').get(i), headers=headers).text)
        if 'proxies' in curr_config:
            dict = {'proxies': curr_config['proxies']}

            with open(f"{location}{i}.yaml", 'w+') as provider:
                try:
                    provider.write(yaml.dump(dict, allow_unicode=True))
                except IOError:
                    print("Direction have no access permission \n")


gen_provider()
