'''Usage:
   pyhead.py <url> -m <method> [-f --follow STRING] [-a --agent AGENTSTRING]
   pyhead.py -h --help
   
Options:
   -m --method     Select HTTP Method (HEAD, GET, POST, PUT, DELETE, OPTIONS, TRACE).
   -f --follow     Follow 301 redirect(True or False). Default = True
   -a --agent      Set User Agent string.
   -h --help       Show this menu.
'''
import docopt
import requests

def results(r):
    print(f'{r.status_code} {r.reason}')
    for i,n  in r.headers.items():
        print(f'{i}: {n}')  

def request(args):
    print('\nChecking URL: {0}\nMethod: {1}\n'.format(args['<url>'], args['<method>'].upper()))
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36'}
    #Add option to select differnt agents.
    if args['--agent'] == True:headers = {'User-Agent': args['AGENTSTRING']}
    redir = True
    if args['--follow'] == 1:redir = False
    try:
        r = requests.request(args['<method>'], args['<url>'], allow_redirects=redir, headers=headers)
        results(r)
    except requests.exceptions.RequestException as e:
        print(e)

if __name__ == '__main__':
    try:
        args = docopt.docopt(__doc__)
        request(args)
        #Handle invalid option
    except docopt.DocoptExit as e:
	    print(e.usage)