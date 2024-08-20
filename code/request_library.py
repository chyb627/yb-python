import requests

def get_example():
    response = requests.get("https://google.com")
    print(f"Status Code: {requests.status_codes}")
    print(response.text)

if __name__ == "__main__":
    get_example()