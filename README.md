mitmdump -s scripts/proxy_interceptor.py
[16:21:44.696] Loading script scripts/proxy_interceptor.py
[16:21:45.122] NumExpr defaulting to 2 threads.
Transformation Pipeline and Model Successfully Loaded
[16:21:49.059] HTTP(S) proxy listening at *:8080.
[16:23:13.565][127.0.0.1:52386] client connect
[16:23:13.836][127.0.0.1:52386] server connect alive.github.com:443 (140.82.113.26:443)
[16:23:14.126][127.0.0.1:52386] Client TLS handshake failed. The client does not trust the proxy's certificate for alive.github.com (tlsv1 alert unknown ca)
[16:23:14.126][127.0.0.1:52386] client disconnect
[16:23:14.127][127.0.0.1:52386] server disconnect alive.github.com:443 (140.82.113.26:443)
[16:23:15.147][127.0.0.1:52402] client connect
[16:23:15.396][127.0.0.1:52402] server connect alive.github.com:443 (140.82.113.26:443)
[16:23:15.653][127.0.0.1:52402] Client TLS handshake failed. The client does not trust the proxy's certificate for alive.github.com (tlsv1 alert unknown ca)
[16:23:15.656][127.0.0.1:52402] client disconnect
[16:23:15.658][127.0.0.1:52402] server disconnect alive.github.com:443 (140.82.113.26:443)
[16:23:17.782][127.0.0.1:52416] client connect
[16:23:18.076][127.0.0.1:52416] server connect alive.github.com:443 (140.82.113.26:443)
[16:23:18.381][127.0.0.1:52416] Client TLS handshake failed. The client does not trust the proxy's certificate for alive.github.com (tlsv1 alert unknown ca)
[16:23:18.383][127.0.0.1:52416] client disconnect
[16:23:18.383][127.0.0.1:52416] server disconnect alive.github.com:443 (140.82.113.26:443)
[16:23:21.079][127.0.0.1:52420] client connect
[16:23:21.483][127.0.0.1:52420] server connect testfire.net:80 (65.61.137.117:80)
[16:23:21.747] Addon error: 'HTTPFlow' object has no attribute 'round_trip_time'
Traceback (most recent call last):                                                                                                                                                                                                         
  File "scripts/proxy_interceptor.py", line 72, in response                                                                                                                                                                                
    features['response_time'] = flow.round_trip_time                                                                                                                                                                                       
                                ^^^^^^^^^^^^^^^^^^^^                                                                                                                                                                                       
AttributeError: 'HTTPFlow' object has no attribute 'round_trip_time'                                                                                                                                                                       
127.0.0.1:52420: GET http://testfire.net/
              << 200 OK 9.0k
[16:23:21.848][127.0.0.1:52426] client connect
[16:23:21.854][127.0.0.1:52440] client connect
[16:23:21.855][127.0.0.1:52456] client connect
[16:23:21.856][127.0.0.1:52466] client connect
[16:23:21.857][127.0.0.1:52480] client connect
[16:23:21.857][127.0.0.1:52482] client connect
[16:23:22.100] Addon error: 'HTTPFlow' object has no attribute 'round_trip_time'
Traceback (most recent call last):                                                                                                                                                                                                         
  File "scripts/proxy_interceptor.py", line 72, in response                                                                                                                                                                                
    features['response_time'] = flow.round_trip_time                                                                                                                                                                                       
                                ^^^^^^^^^^^^^^^^^^^^                                                                                                                                                                                       
AttributeError: 'HTTPFlow' object has no attribute 'round_trip_time'                                                                                                                                                                       
127.0.0.1:52420: GET http://testfire.net/style.css
              << 200 OK 1.1k
[16:23:22.368] Addon error: 'HTTPFlow' object has no attribute 'round_trip_time'
Traceback (most recent call last):                                                                                                                                                                                                         
  File "scripts/proxy_interceptor.py", line 72, in response                                                                                                                                                                                
    features['response_time'] = flow.round_trip_time                                                                                                                                                                                       
                                ^^^^^^^^^^^^^^^^^^^^                                                                                                                                                                                       
AttributeError: 'HTTPFlow' object has no attribute 'round_trip_time'                                                                                                                                                                       
127.0.0.1:52420: GET http://testfire.net/images/gradient.jpg
              << 200 OK 894b
[16:23:22.379][127.0.0.1:52482] server connect testfire.net:80 (65.61.137.117:80)
[16:23:22.380][127.0.0.1:52466] server connect testfire.net:80 (65.61.137.117:80)
[16:23:22.381][127.0.0.1:52426] server connect testfire.net:80 (65.61.137.117:80)
[16:23:22.382][127.0.0.1:52456] server connect testfire.net:80 (65.61.137.117:80)
[16:23:22.392][127.0.0.1:52480] server connect testfire.net:80 (65.61.137.117:80)
[16:23:22.397][127.0.0.1:52440] server connect testfire.net:80 (65.61.137.117:80)
[16:23:22.632] Addon error: 'HTTPFlow' object has no attribute 'round_trip_time'
Traceback (most recent call last):                                                                                                                                                                                                         
  File "scripts/proxy_interceptor.py", line 72, in response                                                                                                                                                                                
    features['response_time'] = flow.round_trip_time                                                                                                                                                                                       
                                ^^^^^^^^^^^^^^^^^^^^                                                                                                                                                                                       
AttributeError: 'HTTPFlow' object has no attribute 'round_trip_time'                                                                                                                                                                       
127.0.0.1:52426: GET http://testfire.net/images/home3.jpg
              << 200 OK 10.2k
[16:23:22.634] Addon error: 'HTTPFlow' object has no attribute 'round_trip_time'
Traceback (most recent call last):                                                                                                                                                                                                         
  File "scripts/proxy_interceptor.py", line 72, in response                                                                                                                                                                                
    features['response_time'] = flow.round_trip_time                                                                                                                                                                                       
                                ^^^^^^^^^^^^^^^^^^^^                                                                                                                                                                                       
AttributeError: 'HTTPFlow' object has no attribute 'round_trip_time'                                                                                                                                                                       
127.0.0.1:52482: GET http://testfire.net/images/logo.gif
              << 200 OK 4.9k
[16:23:22.643] Addon error: 'HTTPFlow' object has no attribute 'round_trip_time'
Traceback (most recent call last):                                                                                                                                                                                                         
  File "scripts/proxy_interceptor.py", line 72, in response                                                                                                                                                                                
    features['response_time'] = flow.round_trip_time                                                                                                                                                                                       
                                ^^^^^^^^^^^^^^^^^^^^                                                                                                                                                                                       
AttributeError: 'HTTPFlow' object has no attribute 'round_trip_time'                                                                                                                                                                       
127.0.0.1:52466: GET http://testfire.net/images/pf_lock.gif
              << 200 OK 76b
[16:23:22.647] Addon error: 'HTTPFlow' object has no attribute 'round_trip_time'
Traceback (most recent call last):                                                                                                                                                                                                         
  File "scripts/proxy_interceptor.py", line 72, in response                                                                                                                                                                                
    features['response_time'] = flow.round_trip_time                                                                                                                                                                                       
                                ^^^^^^^^^^^^^^^^^^^^                                                                                                                                                                                       
AttributeError: 'HTTPFlow' object has no attribute 'round_trip_time'                                                                                                                                                                       
127.0.0.1:52456: GET http://testfire.net/images/home1.jpg
              << 200 OK 7.7k
[16:23:22.668] Addon error: 'HTTPFlow' object has no attribute 'round_trip_time'
Traceback (most recent call last):                                                     
