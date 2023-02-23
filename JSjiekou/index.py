import json, hashlib, time
import xml.etree.ElementTree as ET
from reply import TypeMsg

def main_handler(event, context):
    print(event)
    if event['httpMethod'] == 'GET':
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "plain/text"},
            "body": event['queryString']['echostr']
        }

    if event['httpMethod'] == 'POST':
        webData = event.get("body", None)
        xmlData = ET.fromstring(webData)
        recMsg = TypeMsg(xmlData)
        result = recMsg.send()
        return result