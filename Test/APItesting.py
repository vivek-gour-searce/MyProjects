__author__ = 'vivek.gour'


def test1():
    import requests

    r = requests.get('https://www.google.co.in', auth=('user', 'pass'))
    print r.status_code
    print r.headers['content-type']
    print r.encoding
    print r.text
    print r.json()

    url = "https://www.google.co.in"
    r = requests.get(url)
    print r.cookies['APISID']


def test2():
    import json
    import requests

    r = requests.get('http://httpbin.org/stream/20', stream=True)

    for line in r.iter_lines():

        # filter out keep-alive new lines
        if line:
            print json.loads(line)


test2()