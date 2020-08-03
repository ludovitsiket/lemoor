import csv
import urllib
import urllib.request as url
import sys


def read_file(addr):
    content = []
    with open(addr, 'r') as f:
        for row in csv.DictReader(f):
            return content.append(row)


def cred(data):
    ip, name, pwd = [], [], []
    x = 0
    while x < len(data):
        ip.append(data[x]['address'])
        name.append(data[x]['name'])
        pwd.append(data[x]['password'])
        x += 1
    return (ip, name, pwd)


def cisco_cmd():
    cmd = ['enable', 'show running-config', 'show vlan summary',
           'show vlan brief', 'write memory']
    return cmd


def connection(ip, name, pwd):
    cred_dict = {}
    print(ip)
    if 'http' not in ip:
        ip = 'http://' + ip
    cred_dict[name] = bytes(pwd, encoding='utf-8')
    with url.urlopen(ip, cred_dict, timeout=1) as response:
        print('OK')
        return response


def http_connect(data):
    try:
        if data is None:
            print('Check your addr.csv file if it is correct.')
            sys.exit()
        ip, name, pwd = cred(data)
        x = 0
        while x < len(data):
            if pwd[x] is not None:
                connection(ip[x], name[x], pwd[x])
            else:
                print('IP address ' + ip[x] + ' has no credentials.')
            x += 1
    except (urllib.error.URLError, KeyboardInterrupt, FileNotFoundError,
            TypeError) as e:
        print(e)
        sys.exit()


def main():
    addr = 'addr.csv'
    data = read_file(addr)
    http_connect(data)


if __name__ == '__main__':
    main()
