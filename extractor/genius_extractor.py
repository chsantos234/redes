import http.client
from env import env
import json

def extractor(clientResponse):

    responseList = clientResponse.split(',')
    requestType,param = responseList[0],responseList[1]

    conn = http.client.HTTPSConnection("genius-song-lyrics1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': f"{env('GENIUS_KEY')}",
        'X-RapidAPI-Host': "genius-song-lyrics1.p.rapidapi.com"
    }

    request = {
        "info": "/artist/details/",
        "álbuns": "/artist/albums/",
        "música": "/artist/songs/",
        "letras": "/song/lyrics/"
    }


    if requestType != "letras":

        newString = param.replace(' ','%20')
        conn.request("GET",f"/search/?q={newString}&per_page=2&page=1",headers=headers)
        artistRes = conn.getresponse()
        artistData = json.loads(artistRes.read().decode("utf-8"))
        Id = artistData['hits'][0]['result']['primary_artist']['id']

    else:
        Id = param

    url = f"{request[requestType]}?id={Id}"

    if requestType ==  "letras": url += "&text_format=plain"

    conn.request("GET",url,headers=headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))

    

    return data,url