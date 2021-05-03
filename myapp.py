import time

count = 0

def app(environ, start_response):
    global count

    print(f"start {count}")
    if count == 0:
        time.sleep(10)
    else:
        print("UNEXPECTED!!!!!")
        print("Second request should not be processed, because the client as timedout and closed the connection!")
        exit(1)

    resp = "Done {}".format(count)
    print(resp)
    data = resp.encode()
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    count = count + 1
    return iter([data])