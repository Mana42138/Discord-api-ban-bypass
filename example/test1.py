import requests

response = requests.post("https://yourwebsitelinkhere.com/post_data?webhook=WEBHOOKGOESHERE")

print(response.json())
