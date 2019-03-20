# -*- coding:gbk -*-
import requests,getopt,sys

token_url = 'https://api.zoomeye.org/user/login'
ip_port_list = []
get_url = ''
headers = ''

def query(q):
    global get_url
    get_url = 'https://api.zoomeye.org/host/search?query=%s'%q

def get_token(usr,pwd):
    global headers
    data = '{"username":"%s","password": "%s"}'%(usr,pwd)
    token = requests.post(token_url,data)
    headers = {'Authorization':'JWT '+token.json()['access_token']}

def get_payload(page):
    global headers
    page=page+1
    for j in range(1,page):
        searchrp = requests.get(get_url,headers=headers,params={'page': j})
        for i in range(len(searchrp.json()['matches'])):
            ip=searchrp.json()['matches'][i]['ip']
            port=searchrp.json()['matches'][i]['portinfo']['port']
            ip_port_list.append(str(ip)+':'+str(port))
        Total=searchrp.json()['total']
    print '[-Total-]: '+ str(Total)
    for i in ip_port_list:
        if len(ip_port_list) > 400:
            print 'your account limit 400 row'
            print '[*] ' + i
        else :
            print '[*] ' + i


if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:],"u:p:q:g:")
    tem=''
    for x,y in opts:
        if x == '-u':
            tem=y
        if x=='-p':
            get_token(tem,y)
        if x == '-q':
            query(q=y)
        if x == '-g':
            n=int(y)
            get_payload(n)