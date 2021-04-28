#!usr/bin/env python3
import os
import sys

import requests
import re
import optparse
import subprocess
import time


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="url", help="Target URL")
    parser.add_option('-m', '--manual', help="Enables manual mode", action="store_true")
    (option, arguments) = parser.parse_args()
    if not option.url:
        parser.error("[-] Please specify an URL, use --help for more info")
    return option


options = get_arguments()
url = options.url
print("\n\n")
subprocess.call(["chmod", "777", url + ".html"])
subprocess.call(["rm", url + ".html"])
subprocess.call(["clear"])
os.system("rm " + url + ".*")
print("                        ______                       _         _____                  _                   ")
print("                       / _____)                     | |       (____ \                | |                  ")
print("                      | /  ___   ___    ___    ____ | |  ____  _   \ \   ___    ____ | |  _   ____   ____ ")
print("                      | | (___) / _ \  / _ \  / _  || | / _  )| |   | | / _ \  / ___)| | / ) / _  ) / ___)")
print("                      | \____/|| |_| || |_| |( ( | || |( (/ / | |__/ / | |_| || |    | |< ( ( (/ / | |    ")
print("                       \_____/  \___/  \___/  \_|| ||_| \____)|_____/   \___/ |_|    |_| \_) \____)|_|    ")
print("                                             (_____|                                      By: safe6Sec ")
print("\n\n")
f = open(str(url) + ".html", "at")
f1 = open(str(url) + ".txt", "at")
f.write(
    '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"> <title>Results from GoogleDorker by nerrorsec</title> </head> <body><br>')

if options.manual:
    def manual():
        global f
        print("[+]Registering data into the file.\n")
        time.sleep(5)
        f.write("<h2>Manual mode - Check the links manually.</h2>")
        f.write("<br>")
        f.write('<h2>Possible Directory listing</h2>')
        f.write('<a href="https://www.google.com/search?q=site:' + url + '+intitle:index.of&hl=en">Click Here</a>')
        f.write("<br>")
        f.write('<h2>Possible Configuration files</h2>')
        f.write(
            '<a href="https://www.google.com/search?q=site:' + url + '+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini&hl=en">Click Here</a>')
        f.write("<br>")
        f.write('<h2>Possible Database files</h2>')
        f.write(
            '<a href="https://www.google.com/search?q=site:' + url + '+ext:sql+|+ext:dbf+|+ext:mdb&hl=en">Click Here</a>')
        f.write("<br>")
        f.write('<h2>Possible Log files</h2>')
        f.write('<a href="https://www.google.com/search?q=site:' + url + '+ext:log&hl=en">Click Here</a>')
        f.write("<br>")
        f.write('<h2>Possible Backup and Old files</h2>')
        f.write(
            '<a href="https://www.google.com/search?q=site:' + url + '+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup&hl=en">Click Here</a>')
        f.write("<br>")
        f.write('<h2>Possible Login pages</h2>')
        f.write('<a href="https://www.google.com/search?q=site:' + url + '+inurl:login&hl=en">Click Here</a>')
        f.write("<br>")
        f.write('<h2>Possible SQL Errors</h2>')
        f.write(
            '<a href="https://www.google.com/search?q=site:' + url + '+intext:%22sql+syntax+near%22+|+intext:%22syntax+error+has+occurred%22+|+intext:%22incorrect+syntax+near%22+|+intext:%22unexpected+end+of+SQL+command%22+|+intext:%22Warning:+mysql_connect()%22+|+intext:%22Warning:+mysql_query()%22+|+intext:%22Warning:+pg_connect()%22&hl=en">Click Here</a>')
        f.write("<br>")
        f.write('<h2>Possible Publicly Exposed Documents</h2>')
        f.write(
            '<a href="https://www.google.com/search?q=site:' + url + '+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv&hl=en">Click Here</a>')
        f.write("<br>")
        f.write('<h2>phpinfo()</h2>')
        f.write(
            '<a href="https://www.google.com/search?q=site:' + url + '+ext:php+intitle:phpinfo+%22published+by+the+PHP+Group%22&hl=en">Click Here</a>')
        f.write("<br>")
        f.close()
        print("File successfully created.\n")


    manual()

else:

    def process_google():
        global f
        print("Dorking via Google")
        print("\n")
        f.write("<h1>Results from Google</h1>")
        f.write("<br>")
        print("[#]Checking for Directory listing vulnerabilities")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }

        requesturl = 'https://www.google.com/search?q=site:' + url + '+intitle:index.of&hl=en'
        requesturl1 = 'https://www.baidu.com/s?wd=site:' + url + '+intitle:index.of'
        response = requests.get(requesturl, headers=headers, timeout=5)
        response1 = requests.get(requesturl1, headers=headers, timeout=5)
        # print(requesturl1)
        # print(response1.text)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        notfound1 = re.search('抱歉没有找到', str(response1.content.decode(response1.encoding).encode('utf-8')))
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible Directory listing</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")

            f1.flush()

        if notfound1:
            print("[-]No results found\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible Directory listing</h2>')
            f.write('<a href="' + requesturl1 + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")
            f1.flush()

        time.sleep(5)

        print("[#]Checking for Configuration files exposed")
        requesturl = 'https://www.google.com/search?q=site:' + url + '+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini&hl=en'
        # requesturl1 = 'https://www.baidu.com/s?wd=site:' + url + '+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini&hl=en'
        response = requests.get(requesturl, headers=headers, timeout=5)
        # response1 = requests.get(requesturl1, headers=headers, timeout=5)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        #  notfound1 = re.search('抱歉没有找到', response1.text)
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible Configuration files</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")

            f1.flush()

        # if notfound1:
        #     print("[-]No results found\n")
        # else:
        #     print("[+]Registering data into the file.\n")
        #     f.write('<h2>Possible Configuration files</h2>')
        #     f.write('<a href="' + requesturl1 + '">Click Here</a>')
        #     f.write("<br>")

        time.sleep(5)

        print("[#]Checking for Database files exposed")
        requesturl = 'https://www.google.com/search?q=site:' + url + '+ext:sql+|+ext:dbf+|+ext:mdb&hl=en'
        # requesturl1 = 'https://www.baidu.com/s?wd=site:' + url + '+ext:sql+|+ext:dbf+|+ext:mdb&hl=en'
        response = requests.get(requesturl, headers=headers, timeout=5)
        # response1 = requests.get(requesturl1, headers=headers, timeout=5)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        # notfound1 = re.search('抱歉没有找到', response1.text)
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible Database files</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")

            f1.flush()

        #
        # if notfound1:
        #     print("[-]No results found\n")
        # else:
        #     print("[+]Registering data into the file.\n")
        #     f.write('<h2>Possible Database files</h2>')
        #     f.write('<a href="' + requesturl1 + '">Click Here</a>')
        #     f.write("<br>")

        time.sleep(5)

        print("[#]Checking for Log files exposed")
        requesturl = 'https://www.google.com/search?q=site:' + url + '+ext:log&hl=en'
        # requesturl1 = 'https://www.baidu.com/s?wd=site:' + url + '+ext:log&hl=en'
        response = requests.get(requesturl, headers=headers, timeout=5)
        # response1 = requests.get(requesturl1, headers=headers, timeout=5)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        # notfound1 = re.search('抱歉没有找到', response1.text)
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible Log files</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")

            f1.flush()

        # if notfound1:
        #     print("[-]No results found\n")
        # else:
        #     print("[+]Registering data into the file.\n")
        #     f.write('<h2>Possible Log files</h2>')
        #     f.write('<a href="' + requesturl1 + '">Click Here</a>')
        #     f.write("<br>")

        time.sleep(5)

        print("[#]Checking for 敏感文件")
        requesturl = 'https://www.google.com/search?q=site:' + url + '+filetype:pdf+|+filetype:doc+|+filetype:xls+|+filetype:txt+|+filetype:log+|+filetype:sql+|+filetype:conf&hl=en'
        requesturl1 = 'https://www.baidu.com/s?wd=site:' + url + '+filetype:pdf+|+filetype:doc+|+filetype:xls+|+filetype:txt+|+filetype:log+|+filetype:sql+|+filetype:conf'
        response = requests.get(requesturl, headers=headers, timeout=5)
        response1 = requests.get(requesturl1, headers=headers, timeout=5)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        notfound1 = re.search('抱歉没有找到', str(response1.content.decode(response1.encoding).encode('utf-8')))
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible 敏感文件 files</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")

            f1.flush()

        if notfound1:
            print("[-]No results found\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible 敏感文件 files</h2>')
            f.write('<a href="' + requesturl1 + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")

            f1.flush()

        time.sleep(5)

        print("[#]Checking for 测试")
        requesturl = 'https://www.google.com/search?q=site:' + url + '+inurl:test+|+inurl:testceshi+|+intitle:测试&hl=en'
        requesturl1 = 'https://www.baidu.com/s?wd=site:' + url + '+inurl:test+|+inurl:ceshi+|+intitle:测试'
        response = requests.get(requesturl, headers=headers, timeout=5)
        response1 = requests.get(requesturl1, headers=headers, timeout=5)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        notfound1 = re.search('抱歉没有找到', str(response1.content.decode(response1.encoding).encode('utf-8')))
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible test files</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")

            f1.flush()

        if notfound1:
            print("[-]No results found\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible test files</h2>')
            f.write('<a href="' + requesturl1 + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")

            f1.flush()

        time.sleep(5)

        print("[#]Checking for Backup and old files")
        requesturl = 'https://www.google.com/search?q=site:' + url + '+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup&hl=en'
        # requesturl1 = 'https://www.baidu.com/s?wd=site:' + url + '+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup&hl=en'
        response = requests.get(requesturl, headers=headers, timeout=5)
        # response1 = requests.get(requesturl1, headers=headers, timeout=5)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        # notfound1 = re.search('抱歉没有找到', response1.text)
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible Backup and Old files</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")

            f1.flush()

        #
        # if notfound1:
        #     print("[-]No results found\n")
        # else:
        #     print("[+]Registering data into the file.\n")
        #     f.write('<h2>Possible Backup and Old files</h2>')
        #     f.write('<a href="' + requesturl1 + '">Click Here</a>')
        #     f.write("<br>")

        time.sleep(5)

        print("[#]Checking for Login pages")
        requesturl = 'https://www.google.com/search?q=site:' + url + '+inurl:login+|+inurl:admin+|+inurl:system+|+inurl:guanli+|+inurl:denglu&hl=en'
        requesturl1 = 'https://www.baidu.com/s?wd=site:' + url + '+inurl:login+|+inurl:admin+|+inurl:system+|+inurl:guanli+|+inurl:denglu'
        response = requests.get(requesturl, headers=headers, timeout=5)
        response1 = requests.get(requesturl1, headers=headers, timeout=5)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        notfound1 = re.search('抱歉没有找到', str(response1.content.decode(response1.encoding).encode('utf-8')))
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible Login pages</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")

            f1.flush()

        if notfound1:
            print("[-]No results found\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible Login pages</h2>')
            f.write('<a href="' + requesturl1 + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")

            f1.flush()

        time.sleep(5)

        print("[#]Checking for SQL errors")
        requesturl = 'https://www.google.com/search?q=site:' + url + '+intext:%22sql+syntax+near%22+|+intext:%22syntax+error+has+occurred%22+|+intext:%22incorrect+syntax+near%22+|+intext:%22unexpected+end+of+SQL+command%22+|+intext:%22Warning:+mysql_connect()%22+|+intext:%22Warning:+mysql_query()%22+|+intext:%22Warning:+pg_connect()%22&hl=en'
        requesturl1 = 'https://www.baidu.com/s?wd=site:' + url + '+intext:%22sql+syntax+near%22+|+intext:%22syntax+error+has+occurred%22'
        response = requests.get(requesturl, headers=headers, timeout=5)
        response1 = requests.get(requesturl1, headers=headers, timeout=5)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        notfound1 = re.search('抱歉没有找到', str(response1.content.decode(response1.encoding).encode('utf-8')))
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible SQL Errors</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")

            f1.flush()

        if notfound1:
            print("[-]No results found\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible SQL Errors</h2>')
            f.write('<a href="' + requesturl1 + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")

            f1.flush()

        time.sleep(5)

        print("[#]Checking for Publicly exposed documents ")
        requesturl = 'https://www.google.com/search?q=site:' + url + '+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv&hl=en'
        requesturl1 = 'https://www.baidu.com/s?wd=site:' + url + '+filetype:doc+|+filetype:docx+|+filetype:pdf+|+filetype:ppt+|+filetype:pptx+|+filetype:csv'
        response = requests.get(requesturl, headers=headers, timeout=5)
        response1 = requests.get(requesturl1, headers=headers, timeout=5)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        notfound1 = re.search('抱歉没有找到', str(response1.content.decode(response1.encoding).encode('utf-8')))
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible Publicly Exposed Documents</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")

            f1.flush()

        if notfound1:
            print("[-]No results found\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible Publicly Exposed Documents</h2>')
            f.write('<a href="' + requesturl1 + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")

            f1.flush()

        time.sleep(5)

        print("[#]Checking for phpinfo() ")
        requesturl = 'https://www.google.com/search?q=site:' + url + '+ext:php+intitle:phpinfo+%22published+by+the+PHP+Group%22&hl=en'
        requesturl1 = 'https://www.baidu.com/s?wd=site:' + url + '+intitle:phpinfo+%22published+by+the+PHP+Group%22'

        response = requests.get(requesturl, headers=headers, timeout=5)
        response1 = requests.get(requesturl1, headers=headers, timeout=5)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        notfound1 = re.search('抱歉没有找到', str(response1.content.decode(response1.encoding).encode('utf-8')))
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>phpinfo()</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")

            f1.flush()

            # f.close()

        if notfound1:
            print("[-]No results found\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>phpinfo()</h2>')
            f.write('<a href="' + requesturl1 + '">Click Here</a>')
            f.write("<br>")
            f1.write(requesturl1 + "\n")

            f1.flush()
        f.close()
        f1.close()


    process_google()
