def application(environ, start_response):
    """Simplest possible application object"""
    body = b'<h3>Hello WSGI with Python 2 or 3<h3>'
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [body]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    make_server('0.0.0.0', 8000, application).serve_forever()