__author__ = 'guoweichen'
def get_ip(ip):
    a = ip.split('.')
    if len(a) == 4:
        i=0
        for b in a:
            if b.isdigit() == True:
                if 0 <= int(b) <= 255:
                    i=i+1
                    pass
                else:
                    return {'code':1,'data':ip,'result':'error'}
                    break
            else:
                return {'code':1,'data':ip,'result':'error'}
                break
        if i == 4:
            return {'code':0,'data':ip,'result':'true'}
    else:
        return {'code':1,'data':ip,'result':'error'}

'''
reponse = get_ip()
print reponse
'''