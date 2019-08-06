#!/usr/bin/python3

import os
import re
import requests

TAG_RE = re.compile(r'<[^>]+>')
id_head = '/dots/'
id_foot = '/">'
category_match = '<td><a href='
url_head = 'http://dotshare.it/dots/'
url_foot = '/0/raw/'
download_name = os.path.expanduser('~/dotfile_')

def remove_tags(text):
    return TAG_RE.sub('', text)


def get_id(text):
    return (text.split(id_head))[1].split(id_foot)[0]


def display_dotfiles(url):
    r = requests.get(url)

    for line in r.text.split('\n'):
        if category_match in line:
            if id_head in line:
                # print id
                print(get_id(line).strip(), end='\t')
                #print title
                print('| %s' % remove_tags(line).strip(), end=' ')
            else:
                #print author
                print('by %s' % remove_tags(line).strip())


def get_download_path():
    i = 1

    while(True):
        if os.path.exists(download_name + str(i)):
            i += 1
        else:
            break

    return download_name + str(i)


def download_dotfiles(category, file_id):
    url = url_head + file_id + url_foot
    download_path = get_download_path()

    print('Downloading %s to %s...' % (url, download_path))

    dotfile = requests.get(url)
    with open(download_path, 'w+') as writer:
        writer.write(dotfile.text)

    print('Done.')
