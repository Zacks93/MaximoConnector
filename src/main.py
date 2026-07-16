from core.config import Config
from api.client import MaximoClient
from api.auth import Auth
from api.asset import AssetAPI

import pandas as pd
from pathlib import Path

cfg = Config()

client = MaximoClient(cfg.server)

auth = Auth(client)

print("=" * 40)
print("MAXIMO CONNECTOR")
print("=" * 40)

login_url = (
    cfg.server +
    "/maximo/webclient/login/login.jsp?appservauth=true"
)

response = auth.login(
    login_url,
    cfg.username,
    cfg.password
)

print()
print("Status :", response.status_code)
print("URL :", response.url)
print()

print(client.session.cookies.get_dict())

print("\n" + "=" * 50)
print("TEST OSLC ASSET")
print("=" * 50)

asset_url = (
    cfg.server +
    "/maximo/oslc/os/mxasset?lean=1&oslc.select=assetnum&oslc.pageSize=1"
)

response = client.get(asset_url)

print("Status :", response.status_code)
print("Content-Type :", response.headers.get("Content-Type"))

print()
data = response.json()

print(data.keys())

print(client.session.cookies.get_dict())

asset_api = AssetAPI(client)

assets = asset_api.get_all(cfg.server)

print()
print("=" * 40)
print("TOTAL ASSET")
print("=" * 40)

print(len(assets))

# Membuat folder output jika belum ada
Path("output").mkdir(exist_ok=True)

# Mengubah list menjadi DataFrame
df = pd.DataFrame(assets)

# Simpan ke Excel
df.to_excel(
    "output/Asset.xlsx",
    index=False
)

print()
print("Export selesai.")
print("File : output/Asset.xlsx")