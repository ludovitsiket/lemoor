import csv
import urllib
import urllib.request as url


def read_file(addr):
    x = []
    with open(addr, 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            x.append(row)
    return x


def append_data(ip, name, pwd, data, x):
    ip.append(data[x]['address'])
    name.append(data[x]['name'])
    pwd.append(data[x]['password'])


def cred(data):
    ip, name, pwd = [], [], []
    x = 0
    while x < len(data):
        append_data(ip, name, pwd, data, x)
        x += 1
    return (ip, name, pwd)


def connection(ip):
    try:
        to_url(ip)
    except urllib.error.URLError as e:
        print(e)


def to_url(ip):
    ip = check_correct_url(ip)
    print(ip)
    url.urlopen(ip, timeout=1)


def check_correct_url(param):
    if "http" not in param:
        param = "http://" + param
    return param


def con_cyclus(data, ip, name, pwd):
    x = 0
    while x < len(data):
        connection(ip[x])
        x += 1


def http_connect(data):
    try:
        ip, name, pwd = cred(data)
        con_cyclus(data, ip, name, pwd)
    except (KeyboardInterrupt, FileNotFoundError) as e:
        print(e)


def scrap_data(ip):
    with url.urlopen(ip) as response:
        html = response.read()
    return html


def main():
    addr = 'addr.csv'
    data = read_file(addr)
    http_connect(data)


main()
