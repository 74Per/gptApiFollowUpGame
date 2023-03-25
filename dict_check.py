import urllib.request
import json



def solution(a):
    client_id = "7wRceAsqThkgdFkdzpYN"
    client_secret = "TYRvI6qLH2"
    encText = urllib.parse.quote(a)
    url = 'https://openapi.naver.com/v1/search/encyc?query=' + encText
    request = urllib.request.Request(url)
    request.add_header('X-Naver-Client-Id', client_id)
    request.add_header('X-Naver-Client-Secret', client_secret)

    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode('utf-8'))
    
    if data['items']:
        return True
    else:
        return False

