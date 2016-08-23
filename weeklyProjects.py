#!/usr/local/bin/python3
import requests
from urllib.parse import urlencode
from urllib.parse import unquote
import json
from datetime import datetime, timedelta
import subprocess

def getHtml(url):
    try:
        r = requests.get(url)
        return r.json()
    except Exception as e:
        print(str(e))

def makeUrl(baseUrl, q, sort, order='desc'):
    # q is a keyword list
    # sort is one of stars, forks, or updated
    # order default: desc
    
    # some handle to q
    # if there are dicts in q, then convert it to string
    keywords = []
    for each in q:
        if type(each) is dict:
            each = json.dumps(each)
        keywords.append(each)

    removeChars = '\"{} '
    # remove '"', '{', '}' and ' ' characters
    qString = '+'.join(keywords)
    for each in qString:
        if each in removeChars:
            qString = qString.replace(each, '')

    params = {
                'q': qString,
                'sort': sort,
                'order': order
            }

    url = baseUrl + '?' + urlencode(params)
    # convert hex to string
    url = unquote(url)
    return url

def parse(text):
    
    items = text['items']
    with open('week', 'w') as f:
    
        # items is a list, which elements are dict data
        for each in items:
            item = {}
            item['full_name'] = each['full_name']
            item['language'] = each['language']
            item['star_count'] = each['stargazers_count']
            item['html_url'] = each['html_url']
            item['description'] = each['description']

            # file operation
#            line = json.dumps(item, ensure_ascii=False) + '\n'
            for key, value in item.items():
                line = '{}: {}\n'.format(key, value)
                f.write(line)
            f.write('\n')


        f.close()

    openFile()


def openFile(filename='week'):
    # use less command to open file
    command = 'less ' + filename
    subprocess.call(command, shell=True)


def main():
    baseUrl = 'https://api.github.com/search/repositories'

    dateFormat = '%Y-%m-%d'
    weekBefore = datetime.now() - timedelta(days=7)
    created = weekBefore.strftime(dateFormat)
    q = [{'created': '>'+created}, {'language': 'cpp'}, {'language': 'python'}]
    sort = 'stars'
    
    url = makeUrl(baseUrl, q, sort)

    text = getHtml(url)

    parse(text)

if __name__ == '__main__':
    main()

