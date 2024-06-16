#from rawweb import RawWeb
from xml.etree import ElementTree as ET
import urllib.parse as urlparse
import urllib.request as urlrequest
import base64
import json
log_path = 'demo_burp.log'
def parse_log(log_path):
    '''
    This function accepts burp log file path.
    and returns a dict. of request and response
    result = {'GET /page.php...':'200 OK HTTP / 1.1....','':'',.....}
    '''
    result = {}
    try:
        with open(log_path):
            pass
    except IOError:
        print("[+] Error!!!", log_path, "doesn't exist..")
        exit()

    try:
        tree = ET.parse(log_path)
    except Exception as e:
        print('[+] Opps..! Please make sure binary data is not present in Log, Like raw image dump, flash(.swf files) dump etc')
        exit()

    root = tree.getroot()
    for reqs in root.findall('item'):
        raw_req = reqs.find('request').text
        raw_req = urlparse.unquote(raw_req)
        raw_resp = reqs.find('response').text
        result[raw_req] = raw_resp
    return result

result = parse_log(log_path)

for items in result:
    print (base64.b64decode(items))
