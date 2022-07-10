# Log2JSON
Converts a log of format |DATE|SESSIONID|MESSAGE| to json file:

## How to use

1. Clone repository
2. Install requirements 
3. Run python script

```bash
git clone https://github.com/advxrsary/Log2JSON.git

cd Log2JSON

pip install -r 'requirements.txt'

python3 Log2JSON.py 'log-file' 'output-file'
```
4. At the moment you need to manually remove comma at the last line of output file
```bash
},] ----> }]
```

## Known Issues
+ Comma at the end of the .json
+ Duration is not calculated yet

## Before
```log
2021-05-01T00:00:07.319452  A87246FB7082775D  status=rejected
2021-05-01T00:00:12.187672  E0039D9A55225872  to=<sarah.brown@example.com>
2021-05-01T00:00:12.387427  09E8698600CF8B32  from=<charles.brown@example.com>
2021-05-01T00:00:13.309684  0E9D8BAD6F58CF42  status=sent
2021-05-01T00:00:13.963835  2A9F9D3BA61EE478  message-id=<aebad43f-81ea-4ced-9edb-d1a6ac7552d5@TWJZEN7KX3>
2021-05-01T00:00:14.178614  09E8698600CF8B32  to=<barbara.brown@example.com>
2021-05-01T00:00:14.788593  B8FA2DB700058444  status=sent
2021-05-01T00:00:24.953721  63EFB9B68FE16222  client=2001:db8::1ea9:6da0:cd41
2021-05-01T00:00:25.670689  09E8698600CF8B32  status=rejected
2021-05-01T00:00:25.852578  80AE5FEE2A046EF8  message-id=<d41fb35b-e516-4559-8cc2-583fbaa2051b@PKCKUO0ORJ>
```
## After
```json
[
  {
    "time": {
        "start": "2021-05-01T00:00:07.117297",
        "duration": "0:00:18.553392"
    },
    "sessionid": "09E8698600CF8B32",
    "client": "10.192.162.239",
    "messageid": "<3455937c-58c9-4dae-b057-692d4dd26684@PKCKUO0ORJ>",
    "address": {
        "from": "<charles.brown@example.com>",
        "to": "<barbara.brown@example.com>"
    },
    "status": "rejected"
  }
]
```


..o0O Made by advxrs4ry O0o..
