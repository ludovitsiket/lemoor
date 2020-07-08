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


def connection(ip, name, pwd):
    try:
        print(ip)
        if 'http' not in ip:
            ip = 'http://' + ip
        with url.urlopen(ip, timeout=1) as response:
            html = response.read()
            print(html)
    except (urllib.error.URLError, ValueError) as e:
        print(e)


def http_connect(data):
    try:
        ip, name, pwd = cred(data)
        x = 0
        while x < len(data):
            connection(ip[x], name[x], pwd[x])
            x += 1
    except (KeyboardInterrupt, FileNotFoundError) as e:
        print(e)


def main():
    addr = 'addr.csv'
    data = read_file(addr)
    http_connect(data)


main()
