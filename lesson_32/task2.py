import json
import requests
import urllib.request

url = urllib.request.urlopen('https://api.pushshift.io/reddit/comment/search/')
obj = json.load(url)

if __name__ == "__main__":

    with open('data.json', 'w') as outfile:
        i = 0
        while i < 10:
            obj1 = obj['data'][i]['author']
            obj2 = obj['data'][i]['body']
            print("Author: {}\nComments: {}\n{:*^50}".format(obj1, obj2, 'next comment'))
            i += 1
            json.dump(obj1, outfile)
            json.dump(obj2, outfile)
