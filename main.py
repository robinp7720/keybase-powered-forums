from os import listdir
from os.path import isfile, join

users = ['racer500','robinp']
posts = {}


for user in users:
    posts[user] = [f for f in listdir('/keybase/public/'+user+"/keybase-forums/") if isfile(join(mypath, f))]
    print(posts[user])
