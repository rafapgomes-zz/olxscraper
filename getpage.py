import requests


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }

def request():
    return requests.get("https://www.olx.com.br/brasil?q=notebook%20ryzen%203",headers=headers)


