import requests
data = {
  "title": 'Post Title',
  "body": 'Post Body',
  "userId": 10,
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)

print(f"Status Code: {response.status_code}")
if response.status_code == 201:
  post_data = response.json()
  print("Post Created Successfully:")
  print(f"ID: {post_data['id']}")
  print(f"Title: {post_data['title']}")
  print(f"Body: {post_data['body']}")
else:
  print(f"Failed to create post. Status code: {response.status_code}")
  print(f"Response: {response.text}") 
