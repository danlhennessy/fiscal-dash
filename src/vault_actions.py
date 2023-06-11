from src import app_config
import hvac
import json
import os


class vault():
    def __init__(self, url, namespace, token) -> None:
        self.client = hvac.Client(url=url, namespace=namespace, token=token)
        print(f'Is client authenticated: {self.client.is_authenticated()}')

    def create_secret(self, path, secret: dict):
        response = self.client.secrets.kv.v2.create_or_update_secret(path=path, secret=secret)
        print(json.dumps(response, indent=4, sort_keys=True))

    def display_secret(self, path):
        response = self.client.secrets.kv.read_secret_version(path=path)
        print(json.dumps(response, indent=4, sort_keys=True))

    def get_secret(self, path, key):
        response = self.client.secrets.kv.read_secret_version(path=path)
        return response['data']['data'][key]

    def dict_all(self, path):
        response = self.client.secrets.kv.v2.read_secret_version(path=path)
        data = response['data']['data']
        return dict(data)


if os.environ.get('DOCKER_ENV') == 'true':
    FISCAL_VAULT = vault(
        url=os.environ.get('VAULT_URL'),
        namespace=os.environ.get('VAULT_NAMESPACE'),
        token=os.environ.get('VAULT_TOKEN')
        )
else:
    FISCAL_VAULT = vault(
        url=app_config.VAULT_URL,
        namespace=app_config.VAULT_NAMESPACE,
        token=app_config.VAULT_TOKEN
        )
