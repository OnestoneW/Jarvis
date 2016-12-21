import requests

def process_requests(url, option, user=None, password=None):
    """A function to process an http-request and return the http-response as option=(text, json)"""

    if user is None and option=="text":
        r = requests.get(url)
        content_text = r.text
        return content_text

    elif user is not None and option=="text":
        r1 = requests.get(url, auth=(user, password))
        content_text1 = r1.text
        return content_text1

    elif user is None and option=="json":
        r2 = requests.get(url)
        conten_json = r2.json()
        return conten_json

    elif user is not None and option=="json":
        r3 = requests.get(url, auth=(user, password))
        conten_json1 = r3.json()
        return conten_json1

if __name__ == "__main__":
    req = process_requests("https://www.math.uzh.ch/my/index.php?id=25", "text")
    print(req)