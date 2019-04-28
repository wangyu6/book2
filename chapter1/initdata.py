# vector bob={'name':'bob smith','age':'42','pay':'3000','job':'dev'}
bob={'name':'bob smith','age':'42','pay':'3000','job':'dev'}
sue={'name':'sue','age':'41','pay':'2999','job':'dev1'}
tom={'name':'tom','age':'41','pay':'2998','job':'dev2'}
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom 
if __name__ == '__main__':
    for key in db:
        print('key','=>\n',db[key])