from src.vault_actions import FISCAL_VAULT

FISCAL_VAULT.display_secret('secret')

print(FISCAL_VAULT.get_secret('secret', 'key1'))