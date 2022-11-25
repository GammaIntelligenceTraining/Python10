from configparser import ConfigParser

use_setting = 'DATABASE'
config = ConfigParser()
config.read('config.ini')


print(dict(config['EMAIL']))

config.add_section('NEWSECTION')
config.set('NEWSECTION', 'login', 'roman')
config.set('NEWSECTION', 'pass', '4321')

print(config['NEWSECTION']['login'])

with open('config.ini', 'w') as config_file:
    config.write(config_file)