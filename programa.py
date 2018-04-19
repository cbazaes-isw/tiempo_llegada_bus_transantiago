# pylint: disable=C0103
"""
high level support for doing this and that.
"""
import requests

url = "http://web.smsbus.cl/web/buscarAction.do"

payload = "d=busquedaRapida&busqueda_rapida=pc268+405"
headers = {
    'Content-Type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
