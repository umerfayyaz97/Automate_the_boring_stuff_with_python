# import webbrowser

# webbrowser.open("https://inventwithpython.com")

import requests

response = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(type(response))