Please add a ``config.ini`` have content like this:

```
[DEFAULT]
api_key = {YOUR KEY GOES HERE}
api_secret = {YOUR SECRET GOES HERE}
base_url = https://paper-api.alpaca.markets
``` 

and run the code by 

```
uvicorn stockViewer:app --port 8000
```

