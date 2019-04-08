import requests

response = requests.post(
    url='https://dig.chouti.com/link/vote?linksId=25104426',
    cookies={
        'gpsd': 'ec80df5a8061c915b62f94c2f4204d83',
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
)

print(response.text)
