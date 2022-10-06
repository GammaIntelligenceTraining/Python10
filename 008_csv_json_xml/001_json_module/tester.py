import json

with open('tester.json', 'r', encoding='UTF8') as file:
    data = json.load(file)

for person in data['people']:
    print(f'Hello {person["name"]}. Is {person["phone"]} your phone number?')
