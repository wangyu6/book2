import pickle
dbfile = open('people-pickle','rb')
db = pickle.load(dbfile)
dbfile.close()
db['sue']['pay'] = 20
db['tom']['name'] = 'tom tom'
dbfile = open('people-pickle','wb')
pickle.dump(db,dbfile)
dbfile.close()
