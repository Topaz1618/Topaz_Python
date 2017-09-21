# Author:Topaz
def handle_index():
    f = open('View/index.html',mode='rb')
    data = f.read()
    f.close()
    data = data.replace('@uuuuu'.encode('utf-8'),'biubiuibiu'.encode('utf-8'))
    return [data,]
    return [b'<h1>Hello, index!</h1>']

def handle_date():
    return [b'<h1>Hello, date!</h1>']