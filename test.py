import requests

def test_api(api_url, payload, content_type):
    try:
        headers = {"Content-Type": content_type}
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
    api_url = "https://dev-api.withvideo.ai/api/v1/user/signup"
    
    payload = {
        "email": "info@flipped.ai",
        "password": "flipped123"
    }
    
    content_type = "application/json"
    
    test_api(api_url, payload, content_type)
