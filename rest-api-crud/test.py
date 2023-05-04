import requests

payload={
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "genre": "Classic Literature",
}


response = requests.post("http://localhost:5000/books", json=payload)

print(response.json())
