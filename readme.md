> python -m venv venv


##### Write to files
```python
import requests

url = "http://xkcd.com"

def run_app():
    response = requests.get(url)
    print(response.text)
    if response.status_code == 200:
        with open("index.html", "w") as file:
            file.write(response.text)
    return response

run_app()

```