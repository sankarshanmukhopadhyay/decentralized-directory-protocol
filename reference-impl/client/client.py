import json
from urllib.request import urlopen

BASE_URL = "http://127.0.0.1:8080"


def get_json(path: str):
    with urlopen(f"{BASE_URL}{path}") as response:
        return json.loads(response.read().decode("utf-8"))


if __name__ == "__main__":
    print(json.dumps(get_json("/dedi/query/example.org?page=1&page_size=20"), indent=2))
    print(json.dumps(get_json("/dedi/lookup/example.org/public-key/did:example:merchant-123"), indent=2))
