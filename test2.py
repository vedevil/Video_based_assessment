import http.client
import json

def test_api(api_url, payload, content_type):
    try:
        # Extract host, path, and scheme from the URL
        url_parts = api_url.split('/')
        scheme, host = url_parts[0], url_parts[2]
        path = '/' + '/'.join(url_parts[3:])
        
        # Create a connection to the server
        connection = http.client.HTTPSConnection(host)
        
        # Prepare the headers
        headers = {
            "Content-Type": content_type
        }
        
        # Convert the payload to JSON
        json_payload = json.dumps(payload)
        
        # Send the HTTP request
        connection.request("POST", path, json_payload, headers)
        
        # Get the response
        response = connection.getresponse()
        
        # Print the response
        print("Response status:", response.status)
        print("Response reason:", response.reason)
        print("Response headers:", response.getheaders())
        print("Response body:", response.read().decode())
        
        connection.close()
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    api_url = "https://dev-api.withvideo.ai/api/v1/user/signup"
    
    payload = {
        "email": "info@flipped.ai",
        "password": "flipped123"
    }
    
    content_type = "application/json"
    
    test_api(api_url, payload, content_type)
