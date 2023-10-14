import sys

from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from pyfiglet import figlet_format

font_names = ['starwars', 'block', 'caligraphy', 'doh', 'alphabet', 'banner', 'isometric1', 'larry3d']

for font_name in font_names:
    ascii_art = figlet_format('EATER', font=font_name)
    cprint(ascii_art, 'yellow', attrs=['bold'])