# Configuring color variables
yellow = '\u001b[1;93m'
cyan = '\u001b[1;96m'
red = '\u001b[1;91m'
green = '\u001b[1;92m'
white = '\u001b[1;37;40m'

import requests
import argparse
screen = '''
'########::'########::'##::::'##:'########:'########::::::::::'####:'########:
 ##.... ##: ##.... ##: ##:::: ##:... ##..:: ##.....:::::::::::. ##::... ##..::
 ##:::: ##: ##:::: ##: ##:::: ##:::: ##:::: ##::::::::::::::::: ##::::: ##::::
 ########:: ########:: ##:::: ##:::: ##:::: ######:::'#######:: ##::::: ##::::
 ##.... ##: ##.. ##::: ##:::: ##:::: ##:::: ##...::::........:: ##::::: ##::::
 ##:::: ##: ##::. ##:: ##:::: ##:::: ##:::: ##::::::::::::::::: ##::::: ##::::
 ########:: ##:::. ##:. #######::::: ##:::: ########::::::::::'####:::: ##::::
........:::..:::::..:::.......::::::..:::::........:::::::::::....:::::..:::::
                       URL Brute-Force Tool
       >>>>>>>>>>>>>>>>>[By BHARAT SINGH]<<<<<<<<<<<<<<<<<<
'''
print(f"{yellow}{screen}{white}")

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', type=str, required=True, help='The URL to bruteforce')
parser.add_argument('-w', '--wordlist', type=str, required=True, help='The wordlist to use')
parser.add_argument('-s', '--status_code', type=int, help='The expected status code for a valid directory')
parser.add_argument('--show-status', action='store_true', help='Show the status code of the output')
args = parser.parse_args()

# Request Headers
headers = {
  'User-Agent': 'Kali Linux'
}

#Checking if URL schema exists in the url
if ('http' in args.url) or ('https' in args.url):
	pass
else:
	print('Please enter a URL Schema')
	sys.exit()

# Open wordlist file
with open(args.wordlist, 'r') as wordlist_file:
  # Iterate through each word in the wordlist
  for word in wordlist_file:
    # Strip newline characters from the word
    word = word.strip()
    # Construct the URL to test
    test_url = f'{args.url}/{word}'
    # Make the request
    try:
      response = requests.get(test_url, headers=headers)
      # Check the status code
      if response.status_code == args.status_code:
        if args.show_status:
          print(f'[+] Found directory: {test_url} >>> ({response.status_code})')
        else:
          print(f'[+] Found directory: {test_url}')
      else:
        if args.show_status:
          print(f'[-] {test_url} >>> ({response.status_code})')
        else:
          print(f'[-] {test_url}')
    except requests.exceptions.RequestException as e:
      print(f'[!] {e}')