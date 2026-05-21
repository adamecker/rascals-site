import time, urllib.request, urllib.error, json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SmartProxy(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(length)
        url = "https://generativelanguage.googleapis.com" + self.path
        
        req = urllib.request.Request(url, data=data, method='POST')
        for k, v in self.headers.items():
            if k.lower() not in ['host']:
                req.add_header(k, v)
        
        max_retries = 6
        for attempt in range(max_retries):
            try:
                resp = urllib.request.urlopen(req)
                status, headers, body = resp.status, resp.headers, resp.read()
                break 
                
            except urllib.error.HTTPError as e:
                status, headers, body = e.code, e.headers, e.read()
                
                if status == 429:
                    wait_time = 60.0 # Safe fallback
                    try:
                        # Parse Google's JSON error response
                        error_json = json.loads(body.decode('utf-8'))
                        details = error_json.get('error', {}).get('details', [])
                        
                        for detail in details:
                            if detail.get('@type') == 'type.googleapis.com/google.rpc.RetryInfo':
                                delay_str = detail.get('retryDelay', '')
                                if delay_str.endswith('s'):
                                    # Converts "36.71s" or "45s" into a float
                                    wait_time = float(delay_str[:-1])
                                    break
                    except Exception as parse_err:
                        print(f"JSON Parse fallback. Error: {parse_err}")
                    
                    # Add a tiny 0.5s buffer to ensure we clear the exact millisecond threshold
                    wait_time += 0.5 
                    print(f"Google requested wait. Proxy paused for {wait_time}s (Attempt {attempt+1}/{max_retries})")
                    time.sleep(wait_time)
                    continue # Loop around and resend the request natively
                else:
                    # If it's a 400 or 500 error, pass it back to Aider immediately
                    break

        self.send_response(status)
        for k, v in headers.items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

print("Starting Smart Retry Proxy on port 4000...")
HTTPServer(('0.0.0.0', 4000), SmartProxy).serve_forever()
