import http.client

conn = http.client.HTTPConnection("127.0.0.1")

conn.request("GET", "/threads/%7Bthread_id%7D")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))