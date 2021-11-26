import requests
response = requests.get("https://statsapi.web.nhl.com/api/v1/teams/1/roster")
print(response.status_code)
print(response.text)




