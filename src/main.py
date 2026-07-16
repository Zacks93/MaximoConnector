from core.config import Config
from api.client import MaximoClient

cfg = Config()

client = MaximoClient(cfg.server)

print("=" * 40)
print("MAXIMO CONNECTOR")
print("=" * 40)

print("Server :", cfg.server)
print("Page Size :", cfg.page_size)

print()

response = client.get(cfg.server)
print("HTTP Status :", response.status_code)
print("Redirect URL :", response.url)

print()
print("=" * 40)
print("LOGIN PAGE")
print("=" * 40)

print(response.text[:1000])