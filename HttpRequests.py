import requests
from requests.auth import HTTPBasicAuth, AuthBase
from requests.adapters import HTTPAdapter

response=requests.get('https://www.google.com/')
# in conditional expression it will evaluate to True if the status code was between 200 and 400, and False otherwise.
# if we want we can fetch status code also from response object
if response:
    print('success')
else:
    print('error')

#response in bytes
response.content

#if encoding attribute is specified in response header then 'text' property will convert out raw data
#into that encoding format other wise we have to specify encoding before response.text
response.encoding='utf-8'     #optional
response.text

#get json data
# or we can deserialize above text string data into json using method  'json.loads()'
response.json()

#accessing headers
response.headers['content-type']


#request wih query strings and headers

#in params we can pass dictionary or list of tuples (list of tuples:- [('q','requests+lang:py')]  )
res=requests.get( 'https://api.github.com/search/repositories',params={'q':'requests+language:python'},    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)
jsonRes=res.json()
#fetching repo desc from json response
repository=jsonRes['items'][0]

#post request
res=requests.post('https://httpbin.org/post', data={'key': 'value'})

#authentication
requests.get('https://api.github.com/user', auth=HTTPBasicAuth('username', 'sdsd') )

#custom auth mechanism
class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
        return r


requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token'))

#disable ssl certificate verification
requests.get('https://api.github.com', verify=False)

# set time out
# this will time out after 4.05 sec
requests.get('https://api.github.com',timeout=4.05)
#this will run successfully if request establishes a connection(request sent to resource) in 2 sec and receives data within 5 sec of the connection being established
requests.get('https://api.github.com',timeout=(2, 5))
# if request time out then it will raise a 'Timeout' exception

#using sessions for requests
# with the help if sessions we can use same header setting for multiple requests


# 'with' keyword works as using() in c# . it helps to dispose given methods automatically when its works finished
with requests.Session() as session:
    session.aut=('username','password')
    res=session.get_adapter('www.google.com')

res.headers

# setting retires for requests
#Transport Adapters let you define a set of configurations per service you’re interacting with
github_adapter=HTTPAdapter(max_retires=3)
session=requests.Session()
session.mount('google.com',github_adapter)
try:
    session.get('google.com')
except ConnectionError as ce:
    print(ce)