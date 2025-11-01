import requests
from pipeline.config import ConfigManager

class APIClient:
    def __init__(self, config):
        # Use get_url() instead of get_base_url()
        self.Base_url = config.get_url()
        self.limit = config.get_limit()
        self.timeout = config.get_timeout()

    def get_all_products(self):
        """Fetch all products using simple pagination."""
        all_products = []
        page = 1

        while True:
            print(f"Fetching page {page}...")

            response = requests.get(
                f"{self.Base_url}/products",
                params={"limit": self.limit, "page": page},
                timeout=self.timeout
            )

            if response.status_code != 200:
                print(f"Error fetching page {page}: {response.status_code}")
                break

            data = response.json()
            if not data:  # stop when no more products
                break

            all_products.extend(data)
            page += 1

        return all_products

    def get_all_users(self):
        """Fetch all users from the API."""
        response = requests.get(f"{self.Base_url}/users", timeout=self.timeout)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching users: {response.status_code}")
            return []


# Test block
if __name__ == "__main__":
    config = ConfigManager()
    client = APIClient(config)

    print("Fetching products...")
    products = client.get_all_products()
    print(f"Fetched {len(products)} products")

    print("\nFetching users...")
    users = client.get_all_users()
    print(f"Fetched {len(users)} users")
