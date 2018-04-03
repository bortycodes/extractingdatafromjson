import urllib.request, urllib.error
import json

while True:
    url = input('Enter location: ')
    if len(url) < 1: break

    data = urllib.request.urlopen(url).read()
    info = json.loads(data)

    print('Retrieving ', url)
    print('Retrieved ', len(data), ' characters')

    count = 0
    sum = 0
    for item in info['comments']:
        sum += item['count']
        count += 1

    print('Count: ', count)
    print('Sum: ', sum)

#http://py4e-data.dr-chuck.net/comments_85472.json SUM 2456
#http://py4e-data.dr-chuck.net/comments_42.json SUM 2553