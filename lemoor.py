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


def cred(data):
    ip, name, pwd = [], [], []
    x = 0
    while x < len(data):
        ip.append(data[x]['address'])
        name.append(data[x]['name'])
        pwd.append(data[x]['password'])
        x += 1
    return (ip, name, pwd)


def connection(ip):
    try:
        ip = check_correct_url(ip)
        print(ip)
        dz = url.urlopen(ip, timeout=2)
        print(dz)
    except urllib.error.URLError as e:
        print(e)


def check_correct_url(param):
    if "http" not in param:
        param = "http://" + param
    return param


def http_connect(data):
    try:
        ip, name, pwd = cred(data)
        print(ip)
        x = 0
        while x < len(data):
            connection(ip[x])
            x += 1
    except (KeyboardInterrupt, FileNotFoundError) as e:
        print(e)


def main():
    addr = 'addr.csv'
    data = read_file(addr)
    http_connect(data)


main()
