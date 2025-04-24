import requests

# API endpoint
url = "https://ai-cyber-shield-app.onrender.com/predict"

# Headers for JSON content
headers = {
    "Content-Type": "application/json"
}

# Sample input
data = {
    "url": "http://example.com"
}

# Sending the POST request
try:
    response = requests.post(url, json=data, headers=headers)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
except Exception as e:
    print("Error:", str(e))
