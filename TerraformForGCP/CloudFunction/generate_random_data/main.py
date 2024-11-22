import json
import requests

def fetch_random_users():
    url = "https://randomuser.me/api/"
    user_records = []  # List to store user records

    try:
        # Loop to fetch 10 records
        for _ in range(10):
            response = requests.get(url)  # Make GET request to the API
            if response.status_code == 200:
                data = response.json()  # Parse the JSON response
                user_records.append(data['results'][0])  # Add the user record to the list
            else:
                print(f"Error: API call failed with status code {response.status_code}")
                return {"error": "Failed to fetch data"}

        # # Return the results as a JSON string
        # return json.dumps(user_records, indent=4)  # Pretty print with indentation
        return user_records

    except Exception as e:
        # Handle exceptions and return error details
        return json.dumps({"error": str(e)}, indent=4)

# Run the function and print the output
def get_data(event):
    result = fetch_random_users()
    # Extract only the required fields
    extracted_data = []

    for record in result:
        extracted_data.append({
            "gender": record.get('gender'),
            "first_name": record.get('name', {}).get('first'),
            "last_name": record.get('name', {}).get('last'),
            "email": record.get('email'),
            "city": record.get('location', {}).get('city'),
            "state": record.get('location', {}).get('state'),
            "country": record.get('location', {}).get('country'),
            "username": record.get('login', {}).get('username'),
            "password": record.get('login', {}).get('password'),
            "phone": record.get('phone'),
            "dob": record.get('dob', {}).get('date')
        })
    print(extracted_data)
    return extracted_data