# from bs4 import BeautifulSoup as BS
# import requests
#
# url = 'https://www.google.com/search?q=eur+to+usd&sxsrf=APq-WBuBz9gsaSwH4e1sR-gZ511AEOyvdw%3A1645219288311&source=hp&ei=2A0QYrC8EJb8rgTU0IXICg&iflsig=AHkkrS4AAAAAYhAb6GW8KSCYHfY8ObtYLuKv4udj8bQb&ved=0ahUKEwiwiIW6l4r2AhUWvosKHVRoAakQ4dUDCAY&uact=5&oq=eur+to+usd&gs_lcp=Cgdnd3Mtd2l6EAMyCQgAEEMQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABDLATIFCAAQgAQyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLAToECCMQJzoECAAQQzoICAAQgAQQsQM6BwgAELEDEEM6CggAELEDEIMBEEM6CwgAEIAEELEDEIMBOgcIABAKEMsBUABYpRdgmBxoAHAAeACAAWWIAa8FkgEDOS4xmAEAoAEB&sclient=gws-wiz'
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0)'
#            'Gecko/20100101 Firefox/97.0'}
# page = requests.get(url, headers=headers)
# soup = BS(page.content, 'html.parser')
# match_ = soup.find("span", class_='DFlfde SwHCTb')
# price = match_.get_attribute_list('data-value')
#
# while True:
#     print("Please choose convertasion:\n"
#           "1.$ to eur\n"
#           "2.Eur to $")
#     a = input()
#     if a =="1":
#        b = input('Please input amount:')
#        c = float(price[0])*float(b)
#        print(f'Amount is {c} euro')
#     else:
#         x = input('Please input amount:')
#         w = float(x) /float(price[0])
#         print(f'Its {w} $')

import re
text = 'Время сейчас 09:00'
pattern = re.compile(r'\b([0-1][0-9]|2[0-4]):[0-5][0-9]\b')
matches = pattern.finditer(text)
for match in matches:
    print(match)
