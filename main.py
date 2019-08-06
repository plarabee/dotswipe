#!/usr/bin/python3
# dotswipeit.py - A simple cli for browsing and install dotfiles from dotshare.it

import sys
from modules.help import display_help
from modules.categories import get_category_url
from modules.dotfiles import display_dotfiles, download_dotfiles

if len(sys.argv) == 1:
    display_help()

elif len(sys.argv) == 2:
    url = get_category_url(sys.argv[1])
    display_dotfiles(url)

elif len(sys.argv) == 3:
    download_dotfiles(sys.argv[1], sys.argv[2])

else:
    print('Too many arguments!')
