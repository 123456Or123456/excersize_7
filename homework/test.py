import os #גישה לתיקיות ולקבצים
import requests#בקשות לרשת api (כמן פוסט)

scan_url= 'https://www.virustotal.com/vtapi/v2/file/scan' 
curl_request_url = 'https://www.virustotal.com/vtapi/v2/url/report?apikey=<apikey>&resource=<resource>'
my_api ='3f36b4c89659eaaa70f13a296ea4c2eaa0cbb532c2f6f9b305f57033ad7b66f7'
def scan_file(file_path):
    print("scaning file", file_path)


def scan_folder(older_path):
    pass
