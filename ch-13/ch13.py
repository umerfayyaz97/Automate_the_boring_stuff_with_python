# import webbrowser

# webbrowser.open("https://inventwithpython.com")

import requests

# response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(response.status_code)


#raise error if not loaded correctly
response = requests .get('https://inventwithpython.com/page_that_does_not_exist')
response.raise_for_status()
# print(response.status_code) #404

