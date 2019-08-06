#!/usr/bin/python3
# categories.py - modules to handle categories in dotswipeit

import requests
import sys

root = 'http://dotshare.it/category/'

def get_category_url(category):

    if category.lower() == 'irssi':
        sub = 'chat/irssi/'
    elif category.lower() == 'weechat':
        sub = 'chat/weechat/'
    elif category.lower() == 'emacs-colors':
        sub = 'emacs/colors/'
    elif category.lower() == 'emacs-config':
        sub = 'emacs/config/'
    elif category.lower() == 'mc':
        sub = 'fms/mc/'
    elif category.lower() == 'ranger':
        sub = 'fms/ranger/'
    elif category.lower() == 'conky':
        sub = 'info/conky/'
    elif category.lower() == 'dzen2':
        sub = 'info/dzen2/'
    elif category.lower() == 'misc':
        sub = 'misc/misc/'
    elif category.lower() == 'ncmpcpp':
        sub = 'mpd/ncmpcpp/'
    elif category.lower() == 'bmpanel':
        sub = 'panels/bmpanel/'
    elif category.lower() == 'lxpanel':
        sub = 'panels/lxpanel/'
    elif category.lower() == 'pypanel':
        sub = 'panels/pypanel/'
    elif category.lower() == 'tint2':
        sub = 'panels/tint2/'
    elif category.lower() == 'bash':
        sub = 'shells/bash/'
    elif category.lower() == 'tcsh':
        sub = 'shells/tcsh/'
    elif category.lower() == 'zsh':
        sub = 'shells/zsh/'
    elif category.lower() == 'terms-colors':
        sub = 'terms/colors/'
    elif category.lower() == 'screen':
        sub = 'terms/screen/'
    elif category.lower() == 'tmux':
        sub = 'terms/tmux/'
    elif category.lower() == 'vim-colors':
        sub = 'vim/colors/'
    elif category.lower() == 'vim-rc':
        sub = 'vim/rc/'
    elif category.lower() == 'awesome':
        sub = 'wms/awesome/'
    elif category.lower() == 'bspwm':
        sub = 'wms/bspwm/'
    elif category.lower() == 'dwm':
        sub = 'wms/dwm/'
    elif category.lower() == 'fluxbox':
        sub = 'wms/fluxbox/'
    elif category.lower() == 'fvwm':
        sub = 'wms/fvwm/'
    elif category.lower() == 'herbstluft':
        sub = 'wms/herbstluft/'
    elif category.lower() == 'i3':
        sub = 'wms/i3/'
    elif category.lower() == 'monster':
        sub = 'wms/monster/'
    elif category.lower() == 'openbox':
        sub = 'wms/openbox/'
    elif category.lower() == 'ratpoison':
        sub = 'wms/ratpoison/'
    elif category.lower() == 'spectrwm':
        sub = 'wms/spectrwm/'
    elif category.lower() == 'stumpwm':
        sub = 'wms/stumpwm/'
    elif category.lower() == 'wmfs':
        sub = 'wms/wmfs/'
    elif category.lower() == 'xmonad':
        sub = 'wms/xmonad/'
    else:
        print('ERROR: Category %s not found.' % category)
        sys.exit()

    return root + sub
