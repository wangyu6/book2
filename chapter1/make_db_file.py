from initdata import db
import pickle


dbfilename='people-file'
enddb = 'enddb'
endrec = 'endrec'
recsep = '=>'
# def storeDbase(db,dbfilename = dbfilename):
#     "将数据格式化保存为普通文件"
#     dbfile = open(dbfilename,'w')
#     for key in db:
#         print(key,file=dbfile)
    
#         for (name,value) in db[key].items():
#             print(name + recsep + repr(value) ,file = dbfile)
#         print(endrec, file=dbfile)
#     print(enddb,file=dbfile)
#     dbfile.close()

# def loadDbase(dbfilename=dbfilename):
#     "解析数据，重新构建数据库"
#     dbfile = open(dbfilename)
#     import sys
#     sys.stdin = dbfile
#     db = {}
#     key = input()
#     while key !=enddb:
#         rec = {}
#         field = input()
#         while field !=endrec:
#             name,value  =field.split(recsep)
#             rec[name] = eval(value)
#             field = input()
#         db[key] = rec
#         key = input()
#         return db
# if __name__ == '__main__':
#     from initdata  import db
#     storeDbase(db)

dbfile = open('people-pickle','wb')
pickle.dump(db,dbfile)
dbfile.close