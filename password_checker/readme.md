#### Check if your email has been pawned

Go to the site below:
> haveibeenpwned.com


import requests
# ensure you hash the password first
# https://passwordsgenerator.net/sha1-hash-generator/ or use http://miraclesalad.com/webtools/md5.php
# password = CBFDAC6008F9CAB4083784CBD1874F76618D2A97
# enter the first five Hashed data = CBFDA
url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
res = requests.get(url)
print(res)


```python
import requests
import hashlib

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise  RuntimeError(f'Error fetching: {res.status_code}, check and try again' )
    return res

def read_res(response):
    print(response.text)
def pwend_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest()
    first5_chr, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_chr)
    print(first5_chr, tail, response)
    return read_res(response)

pwend_api_check('123')
```