import requests 

# These requests work 
print(requests.get("http://127.0.0.1:8000/items?count=20").json())
print(requests.get("http://127.0.0.1:8000/items?category=tools").json())

# This requests fail because "ingredient" is not a valid category, as defined in the Category Enum 

print(requests.get("http://127.0.0.1:8000/items?category=ingredient").json())

# This request fails because count has to be an integer 

print(requests.get("http://127.0.0.1:8000/items?count='Hello'").json())


# And here beacause of pydantic

print(requests.post("http://127.0.0.1:8000/", json={"name": "Screwdriver", "price": 3.99, "count": "Hello", "id": 4}).json())


