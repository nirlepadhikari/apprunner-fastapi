from fastapi import FastAPI
import uvicorn
import json
import requests
import xml.etree.ElementTree as E
import xmltodict

app = FastAPI()

@app.get("/")
def read_root():
    url = "http://dev.usbooking.org/us/UnitedSolutions"
    payload = "<?xml version=\"1.0\" ?>\r\n<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\"\r\nxmlns:book=\"http://booking.us.org/\">\r\n    <soapenv:Header/>\r\n    <soapenv:Body>\r\n        <book:SectorCode>\r\n            <strUserId>PLZ137</strUserId>\r\n        </book:SectorCode>\r\n    </soapenv:Body>\r\n</soapenv:Envelope>"
    headers = {
    'Content-Type': 'text/xml',
    'SOAPAction': '#SectorCode'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    root = E.fromstring(response.text)[0][0][0].text
    # convert xml to json
    xml = E.fromstring(root)
    json_data = json.dumps(xmltodict.parse(E.tostring(xml)))
    return json.loads(json_data)


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')

#kick off build