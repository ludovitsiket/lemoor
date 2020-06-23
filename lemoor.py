import csv


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


def main():
    addr = 'addr.csv'
    data = read_file(addr)
    print(data)


main()
