from os import environ

try:
    
    SERVICE_HOST = environ['SERVICE_HOST']
    SERVICE_ADRESS = environ['SERVICE_ADRESS']
    SERVICE_NAME = environ['SERVICE_NAME']
    SERVICE_PORT = int(environ['SERVICE_PORT'])

except Exception as e:

    SERVICE_HOST = '0.0.0.0'
    SERVICE_ADRESS = 'myproject'
    SERVICE_NAME = 'myproject'
    SERVICE_PORT = 7000