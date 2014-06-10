__author__ = 'vivek.gour'


def test1():
    import urllib
    import json
    import httplib
    import requests

    conn = httplib.HTTPConnection("blackdiamond")
    args = urllib.urlencode({'userName':'UNAME', 'password':'PWD'})
    r1 = conn.request("post", "/rest-service/auth-v1/login", args)

    r2 = conn.getresponse()

    print r1,r2,r2.status,r2.reason


def test2():
    import requests
    import json

    github_url = "http://cevauat.uat.invoize.info/"
    data = json.dumps({'name':'test', 'description':'some test repo'})
    r = requests.post(github_url, data, auth=('hitesh.joshi@searce.com', 'searce'))

    print r.json


test2()