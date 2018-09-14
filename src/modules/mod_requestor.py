import requests
from datetime import datetime

class Requestor:
    """Get Near Earth Object data for the specified <target_date>"""
    def __init__(self):
        self.baseurl = "https://api.nasa.gov"
        self.apikey = "lfy8lmrDIcARiePyXnZBqAS1WnW0Dgz9Lir9UYgd"

    def get_neodata(self, target_date):
        """Get Near Earth Object data for the specified <target_date>"""
        urlTemplate = self.baseurl + \
                      "/neo/rest/v1/feed?start_date={target_date}&end_date={target_date}&api_key={apikey}"
        requestURL = urlTemplate.format(target_date=target_date, apikey=self.apikey)
        return self.makegetcall(requestURL)

    def makegetcall(self, url):
        """Runs HTTP get request and returns JSON string"""
        r = requests.get(url)
        return r.text


if __name__ == '__main__':
    currentdate = datetime.now().strftime('%Y-%m-%d')
    req = Requestor()
    print(req.get_neodata(currentdate))
