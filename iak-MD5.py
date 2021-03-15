#-*- encoding=UTF8 -*-
import re
import requests
from requests_toolbelt.utils import dump
import urllib3

list_null = []
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54",
    "Referer":"https://baidu.com/",
}

def cmd5(key):
    url = 'https://cmd5.com'
    data = {
        '__VIEWSTATE':'',
        'ctl00$ContentPlaceHolder1$TextBoxInput':key,
        'ctl00$ContentPlaceHolder1$InputHashType':'md5',
        'ctl00$ContentPlaceHolder1$Button1':'%E6%9F%A5%E8%AF%A2'
    }
    #在headers['cookie']中添加你的cookie，避免频繁查寻，导致的查询失败
    headers['cookie'] = ''
    headers['Referer'] = 'https://cmd5.com'
    try:  
        req = requests.post(url,headers=headers,data=data,timeout=5)
        reqaq = re.findall('onmouseover=\"toggle\(\);\"\>(.*?)\<\/span\>',req.text)
        if (reqaq == list_null):
            print('CMD5查询失败，请过稍后重试或检查您的参数')
        else:
            print('CMD5查询结果： '+str(reqaq[0]))
    except:
        pass

def ttmd5(key):
    url = str('http://www.ttmd5.com/do.php?c=Decode&m=getMD5&md5=')+key
    req = requests.get(url, headers=headers)
    try :
        reqaq = re.findall('plain\"\:\"(.*?)\"',req.text)
        if (reqaq == list_null):
            print('ttmd5查询失败，请过稍后重试或检查您的参数')
        else:
            print('ttmd5查询结果： '+str(reqaq[0]))
    except:
        pass

def t007(key):
    url = 'http://www.t007.cn/home/index/doEnDecode'
    data = {
        "type":'1',
        'txtInput':key,
        'salt':'',
        'ciphertype_id':'1',
        'rnd':'0.42960200194831666'
        }
    #在headers['cookie']中添加你的cookie
    headers['cookie'] = ''
    try:
        req = requests.post(url, data=data, headers=headers)
        req.encoding='utf-8'
        reqaq = (req.text.encode('utf-8').decode('unicode_escape'))
        reqaq1 =  re.findall('\：(.*?)\"\}',reqaq)
        if (reqaq1 == list_null):
            print('t007查询失败，请过稍后重试或检查您的参数')
        else:
            print('t007查询结果： '+str(reqaq1[0]))
    except:
        pass

def nitrxgen(key):
    url = 'https://www.nitrxgen.net/md5db/'+str(key)+'.json'
    try:
        requests.packages.urllib3.disable_warnings()
        req = requests.get(url, headers=headers,verify=False)
        reqaq = re.findall('pass\"\:\"(.*?)\"\,',req.text)
        if (reqaq == list_null):
            print('nitrxgen查询失败，请过稍后重试或检查您的参数')
        else:
            print('nitrxgen查询结果： '+str(reqaq[0]))
    except:
        pass

def md5_my_addr(key):
    url = 'http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php'
    data = {
        'md5':key,
        'x':'16',
        'y':'6'
    }
    try:
        req = requests.post(url, headers=headers,data=data)
        reqaq = re.findall(r"string</span>: (.*)</div>",req.text)
        if (reqaq == list_null):
            print('md5_my_addr查询失败，请过稍后重试或检查您的参数')
        else:
            print('md5_my_addr查询结果： '+str(reqaq[0]))
    except:
        pass

def md5_tellyou(key):
    url = "http://md5.tellyou.top/MD5Service.asmx/HelloMd5"
    data = "Ciphertext=" + key
    headers["X-Forwarded-For"] = "192.168.1.1"
    try:
        req = requests.post(url,data=data,headers=headers1)
        reqaq = re.findall('org\/\"\>(.*?)\<\/string\>',req.text)
        if (reqaq == list_null):
            print('md5_tellyou查询失败，请过稍后重试或检查您的参数')
        else:
            print('md5_tellyou查询结果： '+str(reqaq[0]))
    except:
        pass

def md5_mmkey(key):
    url = 'http://md5.mmkey.com/'
    data = {
        "md5":key,
        'lx':"chkmysql",
        "chkmd5":"%B2%E9%D1%AF"
        }
    try:
        req = requests.post(url, data=data, headers=headers)
        req.encoding = "gb2312"
        reqaq = re.findall('size=3>(.*?)</font>',req.text)
        reqaq = re.findall(':(.*)',reqaq[0])
        if (reqaq == list_null):
            print('md5_mmkey查询失败，请过稍后重试或检查您的参数')
        else:
            print('md5_mmkey查询结果： '+str(reqaq[0]))
    except:
        pass

def md5_gromweb(key):
    url = 'https://md5.gromweb.com/?md5='+str(key)
    try:
        req = requests.get(url, headers=headers)
        reqaq = re.findall('long-content\ string\"\>(.*)\<\/em\>',req.text)
        if (reqaq == list_null):
            print('md5_gromweb查询失败，请过稍后重试或检查您的参数')
        else:
            print('md5_gromweb查询结果： '+str(reqaq[0]))
    except:
        pass

def md5_gongjuji(key):
    url = 'http://md5.gongjuji.net/common/md5dencrypt?UpperCase='+str(key)
    try:
        req = requests.get(url, headers=headers)
        reqaq = re.findall('PlainText\"\:\"(.*?)\"\,',req.text)
        if (reqaq == list_null):
            print('md5_gongjuji查询失败，请过稍后重试或检查您的参数')
        else:
            print('md5_gongjuji查询结果： '+str(reqaq[0]))
    except:
        pass

def md5_du15(key):
    url = 'http://md5.du15.com/index.asp?action=look'
    data ={
        'md5text':key,
        'look':'+%B2%E9%D1%AF+'
    }
    try:
        req = requests.post(url, data=data, headers=headers)
        reqaq = re.findall('rr2"\ (.*)(\s*)\<\/div\>',req.text)
        reqaq1 = str(reqaq[0])
        reqaq = re.findall('value="(.*)\"',reqaq1)
        reqaq = reqaq[0].replace(' ','')
        if (reqaq == list_null):
            print('md5_du15查询失败，请过稍后重试或检查您的参数')
        else:
            print('md5_du15查询结果： '+str(reqaq))
    except:
        pass

def bugbank(key):
    url = "https://www.bugbank.cn/api/md5"
    data = "md5text=" + key
    try:
        req = requests.post(url,data=data,headers=headers)
        reqaq = re.findall('answer\"\:\"(.*?)\"',req.text)
        if (reqaq == list_null):
            print('bugbank查询失败，请过稍后重试或检查您的参数')
        else:
            print('bugbank查询结果： '+str(reqaq[0]))
    except:
        pass

def cmd5_la(key):
    url = 'https://cmd5.la/user/checkit_u.php?t=0.8252039297519655'
    data = {
        "pwd":key,
        'jiejia':"jie"
        }
    #在headers['cookie']中添加你的cookie
    headers['cookie'] = ""
    try:
        req = requests.post(url, data=data, headers=headers)
        reqaq = re.findall('\:(.*)',req.text)
        if (reqaq == list_null):
            print('cmd5_la查询失败，请过稍后重试或检查您的参数')
        else:
            print('cmd5_la查询结果： '+str(reqaq[1]))
    except:
        pass

def xmd5(key):
    url = 'http://www.xmd5.org/md5/search.asp?hash='+str(key)+'&xmd5=MD5+%BD%E2%C3%DC&open=on&checkcode2=5e5c73eb3d3d3cc0a745603f79dd1239'
    #在headers['cookie']中添加你的cookie
    headers['cookie'] = ""
    headers['Referer'] = "http://www.xmd5.org/"
    try:
        req = requests.get(url, headers=headers,allow_redirects=False)
        reqaq = re.findall('info=(.*?)\"\>',req.text)
        if (reqaq == list_null):
            print('xmd5查询失败，请过稍后重试或检查您的参数')
        else:
            print('xmd5查询结果： '+str(reqaq[0]))
    except:
        pass

def main(key):
    function = [cmd5,ttmd5,t007,nitrxgen,md5_my_addr,md5_tellyou,md5_mmkey,md5_gromweb,md5_gongjuji,md5_du15,bugbank,cmd5_la,xmd5]
    for i in range(len(function)):
        func = function[i]
        func(key)

if __name__ == "__main__":
    print('请避免频繁查询！！！')
    print('请在cmd5/t007/cmd5_la/xmd5/中设置您对应网站的cookie值')
    key = input('请输入你要查询的值：')
    main(key)