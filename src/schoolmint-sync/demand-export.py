import os

import requests


def main():
    response = requests.post(
        url=(
            "https://"
            + os.getenv("SCHOOLMINT_DOMAIN")
            + ".schoolmint.net/api/v2/demand_exports"
        ),
        headers={"Api-Token": os.getenv("SCHOOLMINT_API_TOKEN")},
        data={"account_email": os.getenv("SCHOOLMINT_ACCOUNT_EMAIL")},
    )

    response.raise_for_status()

    print(response.json())


if __name__ == "__main__":
    main()
