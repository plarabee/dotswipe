#!/usr/bin/python3
# categories.py - modules to handle categories in dotswipeit

import requests
import sys

root = 'http://dotshare.it/category/'

subdomain = {  'irssi': 'chat/irssi/', 'weechat': 'chat/weechat/', 'emacs-colors': 'emacs/colors/', 
               'emacs-config': 'emacs/config/', 'mc': 'fms/mc/', 'ranger': 'fms/ranger/',
               'conky': 'info/conky/', 'dzen2': 'info/dzen2/', 'misc': 'misc/misc/',
               'ncmpcpp': 'mpd/ncmpcpp', 'bmpanel': 'panels/bmpanel/', 'lxpanel': 'panels/lxpanel/',
               'pypanel': 'panels/pypanel/', 'tint2': 'panels/tint2/', 'bash': 'shells/bash/',
               'tcsh': 'shells/tcsh/', 'zsh': 'shells/zsh/', 'terms-colors': 'terms/colors/',
               'screen': 'terms/screen/', 'tmux': 'terms/tmux/', 'vim-colors': 'vim/colors/',
               'vim-rc': 'vim/rc/', 'awesome': 'wms/awesome/', 'bspwm': 'wms/bspwm/', 'dwm': 'wms/dwm/',
               'fluxbox': 'wms/fluxbox/', 'fvwm': 'wms/fvwm/', 'herbstluft': 'wms/herbstluft/',
               'i3': 'wms/i3/', 'monster': 'wms/monster/', 'openbox': 'wms/openbox/',
               'ratpoison': 'wms/ratpoison/', 'spectrwm': 'wms/spectrwm/', 'stumpwm': 'wms/stumpwm/',
               'wmfs': 'wms/wmfs/', 'xmonad': 'wms/xmonad/' }

def get_category_url(category):

    if category in subdomain.keys():
        return root + subdomain[category]
    
    else:
        print('Category not found!')
        sys.exit()