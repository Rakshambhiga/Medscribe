import requests

def get_request():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("GET Request")
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json()[:2])  
    print("-" * 50)

def post_request():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(url, json=data)
    print("POST Request")
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
    print("-" * 50)

def put_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = {"id": 1, "title": "updated title", "body": "updated body", "userId": 1}
    response = requests.put(url, json=data)
    print("PUT Request")
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
    print("-" * 50)

def delete_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(url)
    print("DELETE Request")
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    print("-" * 50)

# Example usage
if __name__ == "__main__":
    get_request()
    post_request()
    put_request()
    delete_request()
