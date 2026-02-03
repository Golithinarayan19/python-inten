import requests
import json

def fetch_random_user():
    url = "https://randomuser.me/api/"

    try:
        # Send GET request
        response = requests.get(url, timeout=10)

        # Check status code
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return

        # Parse JSON response
        data = response.json()

        # Extract nested fields
        user = data["results"][0]
        name = f"{user['name']['title']} {user['name']['first']} {user['name']['last']}"
        email = user["email"]
        country = user["location"]["country"]
        username = user["login"]["username"]

        # Display clean output
        print("👤 Random User Details")
        print("-" * 25)
        print(f"Name     : {name}")
        print(f"Username : {username}")
        print(f"Email    : {email}")
        print(f"Country  : {country}")

        # Save full API response to a file
        with open("random_user_data.json", "w") as file:
            json.dump(data, file, indent=4)

        print("\n✅ API response saved to random_user_data.json")

    except requests.exceptions.RequestException as e:
        print("❌ API request failed")
        print("Reason:", e)


if __name__ == "__main__":
    fetch_random_user()
