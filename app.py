import requests
import json

def fetch_market_data():
    url = "https://api.parcllabs.com/v1/search/markets"
    headers = {
        "accept": "application/json",
        "Authorization": ""  # Replace YOUR_API_KEY with your actual API key
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses

        data = response.json()
        return data  # Return the market data

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")  # Handle connection errors
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")  # Handle timeout errors
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")  # Handle all other requests errors
    except ValueError as json_err:
        print(f"JSON decoding error: {json_err}")  # Handle JSON decoding errors

def main():
    print("Fetching market data from Parcl Labs API...")
    market_data = fetch_market_data()

    if market_data:
        print(json.dumps(market_data, indent=4))  # Pretty print the JSON data

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Real Estate Analyzer!"

if __name__ == "__main__":
    app.run(debug=True)
