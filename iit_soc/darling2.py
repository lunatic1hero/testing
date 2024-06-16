from xml.etree import ElementTree as ET
import urllib.parse as urlparse
import urllib.request as urlrequest
import base64
import csv

log_path = 'demo_burp.log'

def parse_log(log_path):
    '''
    This function accepts burp log file path.
    and returns a dict of request and response
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
        print('[+] Oops..! Please make sure binary data is not present in Log, Like raw image dump, flash(.swf files) dump etc')
        exit()

    root = tree.getroot()
    for reqs in root.findall('item'):
        raw_req = reqs.find('request').text
        raw_req = urlparse.unquote(raw_req)
        raw_resp = reqs.find('response').text
        result[raw_req] = raw_resp
    return result

def rhrp(rawreq):
    try:
        raw = rawreq.decode('utf8')
    except Exception as e:
        raw = rawreq
    global headers, method, body, path
    headers = {}
    sp = raw.split('\n\n', 1)
    if len(sp) > 1:
        head = sp[0]
        body = sp[1]
    else:
        head = sp[0]
        body = ""
    c1 = head.split('\n', head.count('\n'))
    method = c1[0].split(' ', 2)[0]
    path = c1[0].split(' ', 2)[1]
    for i in range(1, head.count('\n') + 1):
        slice1 = c1[i].split(': ', 1)
        if slice1[0] != "":
            try:
                headers[slice1[0]] = slice1[1]
            except:
                pass  
    return headers, method, body, path

# Open the CSV file in text mode
with open('http_log1.csv', "w", newline='') as f:
    c = csv.writer(f)
    c.writerow(["method", "body", "path", "headers"])

result = parse_log(log_path)

for items in result:
    data = []
    rr = base64.b64decode(items).decode('utf-8')
    method, body, path, headers = rhrp(rr)
    data.append(method)
    data.append(body)
    data.append(path)
    data.append(headers)
    # Open the file in text mode for appending
    with open('http_log1.csv', "a", newline='') as f:
        c = csv.writer(f)
        c.writerow(data)
