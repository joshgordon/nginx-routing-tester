def simple_app(environ, start_response):
    print(environ["RAW_URI"])
    status = "200 OK"
    response_headers = [('content-type', 'text/plain')]
    start_response(status, response_headers)

    return [(environ["RAW_URI"] + "\n").encode("utf-8")]

