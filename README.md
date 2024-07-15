mitmdump -s scripts/proxy_interceptor1.py
[17:04:14.537] Loading script scripts/proxy_interceptor1.py
[17:04:15.922] NumExpr defaulting to 2 threads.
[17:04:17.559] HTTP(S) proxy listening at *:8080.
[17:04:52.889][127.0.0.1:52644] client connect
[17:04:53.171][127.0.0.1:52644] server connect testfire.net:80 (65.61.137.117:80)
Analyzing request: GET http://testfire.net/search.jsp?query=%3Cscript%3Ealert%281%29%3C%2Fscripts%3E
Request headers: Headers[(b'Host', b'testfire.net'), (b'User-Agent', b'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'), (b'Accept', b'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'), (b'Accept-Language', b'en-US,en;q=0.5'), (b'Accept-Encoding', b'gzip, deflate'), (b'Referer', b'http://testfire.net/search.jsp?query=%3Cscript%3Ealert%281%29%3C%2Fscripts%3E'), (b'Connection', b'keep-alive'), (b'Cookie', b'JSESSIONID=B8BCF8784BAF6F48BF3DAC5F1E855601'), (b'Upgrade-Insecure-Requests', b'1')]
Request body params: []
Extracted UID value: None
UID value is None, skipping SQL keyword analysis for request: GET http://testfire.net/search.jsp?query=%3Cscript%3Ealert%281%29%3C%2Fscripts%3E
[17:04:53.438] Addon error: 'numpy.ndarray' object has no attribute 'predict'
Traceback (most recent call last):                                                                                                                                                                                                         
  File "scripts/proxy_interceptor1.py", line 175, in response                                                                                                                                                                              
    cluster_label = kmeans_model.predict(request_features)[0]                                                                                                                                                                              
                    ^^^^^^^^^^^^^^^^^^^^                                                                                                                                                                                                   
AttributeError: 'numpy.ndarray' object has no attribute 'predict'                                                                                                                                                                          
127.0.0.1:52644: GET http://testfire.net/search.jsp?query=%3Cscript%3Ealert%281%29%3C%2Fscripts%3E
              << 200 OK 6.7k
[17:04:56.015][127.0.0.1:58186] client connect
[17:04:56.097][127.0.0.1:58186] server connect tiles-cdn.prod.ads.prod.webservices.mozgcp.net:443 (34.36.165.17:443)
[17:04:56.153][127.0.0.1:58186] Client TLS handshake failed. The client does not trust the proxy's certificate for tiles-cdn.prod.ads.prod.webservices.mozgcp.net (tlsv1 alert unknown ca)
[17:04:56.155][127.0.0.1:58186] client disconnect
[17:04:56.156][127.0.0.1:58186] server disconnect tiles-cdn.prod.ads.prod.webservices.mozgcp.net:443 (34.36.165.17:443)
[17:05:13.430][127.0.0.1:52644] server disconnect testfire.net:80 (65.61.137.117:80)
[17:05:26.323][127.0.0.1:52644] server connect testfire.net:80 (65.61.137.117:80)
Analyzing request: GET http://testfire.net/
Request headers: Headers[(b'Host', b'testfire.net'), (b'User-Agent', b'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'), (b'Accept', b'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'), (b'Accept-Language', b'en-US,en;q=0.5'), (b'Accept-Encoding', b'gzip, deflate'), (b'Connection', b'keep-alive'), (b'Cookie', b'JSESSIONID=845077026C7DBC8577E352663D608407'), (b'Upgrade-Insecure-Requests', b'1')]
Request body params: []
Extracted UID value: None
UID value is None, skipping SQL keyword analysis for request: GET http://testfire.net/
[17:05:26.589] Addon error: 'numpy.ndarray' object has no attribute 'predict'
Traceback (most recent call last):                                                                                                                                                                                                         
  File "scripts/proxy_interceptor1.py", line 175, in response                                                                                                                                                                              
    cluster_label = kmeans_model.predict(request_features)[0]                                                                                                                                                                              
                    ^^^^^^^^^^^^^^^^^^^^                                                                                                                                                                                                   
AttributeError: 'numpy.ndarray' object has no attribute 'predict'                                                                                                                                                                          
127.0.0.1:52644: GET http://testfire.net/
              << 200 OK 9.0k
[17:05:26.693][127.0.0.1:52644] server disconnect testfire.net:80 (65.61.137.117:80)
127.0.0.1:52644: GET http://testfire.net/images/gradient.jpg
 << Client disconnected.
[17:05:26.699][127.0.0.1:52644] client disconnect
