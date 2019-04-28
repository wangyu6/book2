import pickle
# from make_db_file import loadDbase
dbfile = open('people-pickle','rb')
db = pickle.load(dbfile)
# dbfile.close()
# db['sue']['pay'] *= 20
for key in db:
    print(key,'=>\n',db[key])
# pickle.dump(db,dbfile)
dbfile.close()
# print(db['sue']['name'])