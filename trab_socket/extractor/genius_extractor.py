import http.client
from env import env
import json

def extractor(requesType):
    conn = http.client.HTTPSConnection("genius-song-lyrics1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': f"{env('GENIUS_KEY')}",
        'X-RapidAPI-Host': "genius-song-lyrics1.p.rapidapi.com"
    }

    request = {
        "letra": "/song/lyrics/", # precisa: id-musica
        "pesquisar": "/search/" # precisa: string-formatada
    }

    url = f'{request}?'

    conn.request()
    res = conn.getresponse("GET",url,headers=headers)
    data = json.loads(res.read().decode("utf-8"))