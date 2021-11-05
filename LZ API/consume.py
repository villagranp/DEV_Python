import requests

#GET
print('METODO GET')
api_url = "https://jsonplaceholder.typicode.com/todos/"
response = requests.get(api_url)
response.json()
print(response.json())


#POST
print('METODO POST')
todo = {"userId": 1, "title": "Buy milk", "completed": False}
responsep = requests.post(api_url, json=todo)
responsep.json()
print(responsep.json())



"""
REQUEST

import requests

url = "https://app.pagalocard.com/api/v1/integracion/{token}"

payload = "{\r\n  \"empresa\": \"{\\\"key_secret\\\":\\\"secret\\\",\\\"key_public\\\":\\\"public\\\",\\\"idenEmpresa\\\":\\\"empresa\\\"}\",\r\n  \r\n  \"cliente\": \"{\\\"nit\\\":\\\"55205801\\\",\\\"codigo\\\":\\\"3\\\",\\\"firstName\\\":\\\"Pagalo\\\",\\\"lastName\\\":\\\"CON\\\",\\\"street1\\\":\\\"12 Avenida Zona 15\\\",\\\"country\\\":\\\"GT\\\",\\\"city\\\":\\\"Guatemala\\\",\\\"state\\\":\\\"GT\\\",\\\"postalCode\\\":\\\"04001\\\",\\\"email\\\":\\\"pagalotest2@gmail.com\\\",\\\"ipAddress\\\":\\\"190.104.119.240\\\",\\\"phone\\\":\\\"40404040\\\",\\\"Total\\\":1.5,\\\"deviceFingerprintID\\\":\\\"\\\",\\\"currency\\\":\\\"GTQ\\\",\\\"fecha_transaccion\\\":\\\"2021-05-13 14:37:13\\\"}\",\r\n  \r\n  \"detalle\": \"[{\\\"nombre\\\":\\\"Servicio Virtual\\\",\\\"precio\\\":1.5,\\\"cantidad\\\":1,\\\"tipo\\\":\\\"producto\\\",\\\"id_producto\\\":\\\"777\\\",\\\"Subtotal\\\":1.5}]\",\r\n  \r\n  \"tarjetaPagalo\": \"{\\\"nameCard\\\":\\\"Pagalo Test\\\",\\\"accountNumber\\\":\\\"4000000000000416\\\",\\\"expirationMonth\\\":\\\"12\\\",\\\"expirationYear\\\":\\\"2021\\\",\\\"CVVCard\\\":\\\"123\\\"}\"\r\n}"
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


{
  "decision": "ACCEPT",
  "reasonCode": "00",
  "requestID": "032210027920",
  "infotran": {
    "auditNumber": "027920",
    "referenceNumber": "032210027920",
    "authorizationNumber": "001876",
    "responseCode": "00",
    "messageType": "0210"
  },
  "metadata": {
    "version": "1.0",
    "created_at": "2020-05-10 06:00:05",
    "udpated_at": "2021-05-12 08:02:45",
    "created_by": "developer-pagalo",
    "domain": "app.pagalocard.com",
    "description": "Pagos con pasarela Epay y cuotas"
  },
  "estado": 1
}

"""