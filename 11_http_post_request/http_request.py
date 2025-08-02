import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

if response.status_code == 200:
    post_data = response.json()
    print("Post Data:")
    print(f"ID: {post_data['id']}")
    print(f"Title: {post_data['title']}")
    print(f"Body: {post_data['body']}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
