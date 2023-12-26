import requests
payload = input("Enter song to be searched")
r = requests.post("https://pagalworld.com.pe/find/",params=payload)
print(r.json())