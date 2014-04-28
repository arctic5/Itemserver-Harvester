import urllib2 as u
import time
import data

#There's probably a built in function for this but I'm too lazy to find it so I'll write my own
def read_string(string, size):
    return string[:size]
def read_string_from_back(string, size):
    return string[size*-1:]

#just for fun
def http_new_get(url):
    response = u.urlopen(url).read()
    return response

#pfft no
def attemptGift():
    response = http_new_get("http://l3.ajf.me/gg2/giveGift.php?key="+currentGiftKey+"&token="+myToken+"&server_key="+serverKey)
    print "attempted gift"
    print response


    
#vars
current_time = int(round(time.time() * 1000))
startTime = time.time()*1000
myName = "arctic"
myKey = "vk6lxQx3xkUBfiv"
serverStartResponse = http_new_get("http://l3.ajf.me/gg2/serverStart.php")
serverKey = read_string(serverStartResponse, 15)
currentGiftKey = read_string_from_back(serverStartResponse, 15)
myToken = http_new_get("http://l3.ajf.me/gg2/getToken.php?user_name=arctic&user_key=vk6lxQx3xkUBfiv")
myLoadout = http_new_get("http://l3.ajf.me/gg2/getLoadout.php?token="+myToken+"&server_key="+serverKey)

#load other accounts
for n in data.usernames[:len(data.usernames)]:
    http_new_get("http://l3.ajf.me/gg2/getLoadout.php?token="+n+"&server_key="+serverKey)
    print n
    
for p in data.keys[:len(data.keys)]:
    http_new_get("http://l3.ajf.me/gg2/getLoadout.php?token="+p+"&server_key="+serverKey)
    print p
    
#init
print "Arctic's Lightweight Itemserver Miner Alpha v0.01"
#print "My Loadout:",myLoadout
print "Server Start Response",serverStartResponse
print "Length of server key:",len(serverKey)
print "Length of first gift key:",len(currentGiftKey)
print "Server key:",serverKey
print "Initial gift key:",currentGiftKey
print "My Token:", myToken
print "current_time:",time.time()*1000
giftDelay = (time.time()*1000)+1000*60*15

x = 1
while x == 1:
    if (time.time()*1000 > giftDelay):
        attemptGift()
        giftDelay = (time.time()*1000)+1000*60*15
        x = 0

#this does not work is not needed yet
#Refresh Token
# if (startTime + 1000*60*60*2 < time.time()*1000):
    # startTime = time.time()*1000
    # myToken = http_new_get("http://l3.ajf.me/gg2/refreshToken.php?user_name="+myName+"&user_key="+serverKey+"&token="+myToken)
    # print "Token refreshed"
    # print "New Token:",myToken
raw_input()
