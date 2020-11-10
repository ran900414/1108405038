import requests

url = "https://dog.ceo/api/breeds/image/random"

payload = {}
headers = {
  'Cookie': '__cfduid=d331dc8bb7162628ab294c9e5f861a26b1604987776'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
