from urllib.parse import urlparse


class AssetAPI:

    def __init__(self, client):
        self.client = client

    def get_all(self, server, page_size=1000):

        url = (
            server +
            f"/maximo/oslc/os/mxasset"
            f"?lean=1"
            f"&oslc.select=*"
            f"&oslc.pageSize={page_size}"
        )

        assets = []

        while url:

            print(f"Download : {url}")

            response = self.client.get(url)
            print("HTTP :", response.status_code)
            print("URL  :", response.url)
            print("TYPE :", response.headers.get("Content-Type"))
            response.raise_for_status()

            data = response.json()

            assets.extend(data["member"])

            response_info = data.get("responseInfo", {})

            print("\n=== RESPONSE INFO ===")
            print(response_info)
            print("=====================\n")

            next_page = response_info.get("nextPage")

            if next_page:

                next_url = next_page.get("href")

                parsed = urlparse(next_url)

                url = server + parsed.path + "?" + parsed.query

            else:
                url = None

        return assets