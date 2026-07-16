from urllib.parse import urljoin


class Auth:

    def __init__(self, client):
        self.client = client

    def login(self, login_url, username, password):

        # Ambil halaman login terlebih dahulu
        response = self.client.get(login_url)

        from bs4 import BeautifulSoup

        soup = BeautifulSoup(response.text, "lxml")

        form = soup.find("form")

        action = form.get("action")

        post_url = urljoin(login_url, action)

        payload = {}

        # Ambil semua input hidden
        for item in form.find_all("input"):

            name = item.get("name")

            value = item.get("value") or ""

            if name:
                payload[name] = value

        # Isi username & password
        payload["j_username"] = username
        payload["j_password"] = password

        print("\nPOST URL :", post_url)
        print("Payload :")

        for k, v in payload.items():
            if k == "j_password":
                print(f"{k} = ********")
            else:
                print(f"{k} = {v}")

        response = self.client.post(post_url, payload)

        return response