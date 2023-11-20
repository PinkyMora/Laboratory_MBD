
import requests
url = "https://opendata.aemet.es/opendata/api/prediccion/maritima/costera/costa/47"
"""url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/normales/estacion/08482" """

querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0aWMzZm1iQGdtYWlsLmNvbSIsImp0aSI6ImZjN2Q4NjY2LTViYjQtNDZmMC1hMDdmLTM4YjQ4YmExNTllZCIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNjk5ODg5ODE4LCJ1c2VySWQiOiJmYzdkODY2Ni01YmI0LTQ2ZjAtYTA3Zi0zOGI0OGJhMTU5ZWQiLCJyb2xlIjoiIn0.OEZppp8TfIuza-tsRsFuox-TyE4nLyeDx8PPOLAvuzg"}

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

jsonAemet = response.json();

url = jsonAemet['datos'];

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)