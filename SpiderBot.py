import requests
from bs4 import BeautifulSoup
import re
import sys
import bcolors, argparse

def banner():
    print(bcolors.BLUE + """
          
                        ░██████╗██████╗░██╗██████╗░███████╗██████╗░██████╗░░█████╗░████████╗
                        ██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
                        ╚█████╗░██████╔╝██║██║░░██║█████╗░░██████╔╝██████╦╝██║░░██║░░░██║░░░
                        ░╚═══██╗██╔═══╝░██║██║░░██║██╔══╝░░██╔══██╗██╔══██╗██║░░██║░░░██║░░░
                        ██████╔╝██║░░░░░██║██████╔╝███████╗██║░░██║██████╦╝╚█████╔╝░░░██║░░░
                        ╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░
                                                                                 Coded By: NG
           """)
if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] == '-c'):
        try:
            input_url = sys.argv[2]

            parser = argparse.ArgumentParser()
            parser.add_argument("-c", required=True)
            parser.add_argument("-help")
            args = parser.parse_args()

            code = requests.get(input_url)
            soup = BeautifulSoup(code.text,'html.parser')

            links = [a.attrs.get('href') for a in soup.select('a')]
            str_links = str(links)
            reg = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
            l = re.findall(reg, str_links)
            dup_items = set()
            uniq_items = []

            for x in l:
               if x not in dup_items:
                    uniq_items.append(x)
                    dup_items.add(x)
                    dup_items_newLines = "\n".join(dup_items)
                    dup_items_newLines_replace = re.sub('\'','',dup_items_newLines)
            print(dup_items_newLines_replace)
        except:
            banner()
            print(bcolors.ERR + 'Please enter python  SpiderBot.py -c <URl which you want to crawl> ')
    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: SpiderBot.py [-h] -c URL' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-c Crawler,   --enter URL which you want to crawl' '\n' )
else:
    banner()
    print(bcolors.ERR + 'Please select at least 1 option from -c or -h, with a valid URL')

