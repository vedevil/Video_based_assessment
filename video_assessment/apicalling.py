import requests

def test_api(endpoints,payload, headers):
    base_url = "https://dev-api.withvideo.ai"
    api_url=base_url+endpoints
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        
        if response.status_code == 200:
            print("Request was successful!")
            print("Response JSON:")
            print(response.json())  # Assuming the response is in JSON format
        else:
            print(f"Request failed with status code: {response.status_code}")
            print("Response content:")
            print(response.text)
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    payload = {
        "email": "info@flipped.ai",
        "password": "flipped123"
    }
    
    content_type = "application/json"
    
    test_api(payload, content_type)
