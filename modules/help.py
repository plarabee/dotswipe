#!/usr/bin/python3

def display_help():
    print('dotswipe - a simple cli interface for dotshare.it\n')
    print('USAGE:')
    print('dotswipe - displays this message')
    print('dotswipe [category] - displays list of dot files, author, and id')
    print('dotswipe [category] [id] - downloads and installs dotfile to the user\'s home directory\n')
    print('CATEGORIES:')
    print('irssi\t\tweechat\t\temacs-colors\temacs-config')
    print('mc\t\tranger\t\tconky\t\tdzen2')
    print('misc\t\tncmpcpp\t\tbmpanel\t\tlxpanel')
    print('pypanel\t\ttint2\t\tbash\t\ttcsh')
    print('zsh\t\tterms-colors\tscreen\t\ttmux')
    print('vim-colors\tvim-rc\t\tawesome\t\tbspwm')
    print('dwm\t\tfluxbox\t\tfvwm\t\therbstluft')
    print('i3\t\tmonster\t\topenbox\t\tratpoison')
    print('spectrwm\tstumpwm\t\twmfs\t\txmonad')
