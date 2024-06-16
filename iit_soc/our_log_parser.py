#from rawweb import RawWeb
from xml.etree import ElementTree as ET
import urllib
log_path = 'demo_burp.log'
def parse_log(log_path):
    '''
    This fucntion accepts burp log file path.
    and returns a dict. of request and response
    result = {'GET /page.php...':'200 OK HTTP / 1.1....','':'',.....}
    '''
    result = {}
    try:
        with open(log_path): pass
    except IOError:
        print "[+] Error!!! ",log_path,"doesn't exist.."
        exit()
    try:
        tree = ET.parse(log_path)
    except Exception, e:
        print '[+] Opps..!Please make sure binary data is not present in Log, Like raw image dump,flash(.swf files) dump etc'
        exit()
    root = tree.getroot()
    for reqs in root.findall('item'):
        raw_req = reqs.find('request').text
        raw_req = urllib.unquote(raw_req).decode('utf8')
        raw_resp = reqs.find('response').text
        result[raw_req] = raw_resp
    return result

print parse_log(log_path)
