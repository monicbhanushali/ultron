import requests
import simplejson as json

def get_country_details( country_name ):
    url = "https://restcountries.eu/rest/v2/name/" + country_name
    http_response = requests.get(url + "?fullText=true")
    country_json_resp=""
    if http_response.status_code == requests.codes.ok:
        country_json_resp = http_response.json()
    else:
        http_response = requests.get(url)
        if http_response.status_code == requests.codes.ok:
            country_json_resp = http_response.json()
        else:
            return -1

    country_name = country_json_resp[0]['name']
    country_capital = country_json_resp[0]['capital']
    country_ccy = country_json_resp[0]['currencies'][0]['code'] +" (" +country_json_resp[0]['currencies'][0]['name']+")"
    country_lang = country_json_resp[0]['languages'][0]['name']

    country_details = "Here is what I found about "+country_name +"\n Capital: "+country_capital + "\n Language: " + country_lang + "\n Currency: "+country_ccy
    country_details += "\n Maps: https://www.google.co.in/maps/place/"+country_name
    return country_details
