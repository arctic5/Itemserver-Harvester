import urllib2
import time
def read_string(string, size):
    return string[:size]
def read_string_from_back(string, size):
    return string[size*-1:]
def http_new_get(url):
    return urllib2.urlopen(url).read()
def reelInTheGift():
    print http_new_get("http://l3.ajf.me/gg2/giveGift.php?key="+currentGiftKey+"&token="+myToken+"&server_key="+serverKey)
print "Arctic's Lightweight Itemserver Miner Alpha v0.01"
print "ALIM is now harvesting items"
myName = "arctic"
myKey = "vk6lxQx3xkUBfiv"
loop = 1
while loop == 1:
    #vars
    serverStartResponse = http_new_get("http://l3.ajf.me/gg2/serverStart.php")
    serverKey = read_string(serverStartResponse, 15)
    currentGiftKey = read_string_from_back(serverStartResponse, 15)
    myToken = http_new_get("http://l3.ajf.me/gg2/getToken.php?user_name=arctic&user_key=vk6lxQx3xkUBfiv")
    myLoadout = http_new_get("http://l3.ajf.me/gg2/getLoadout.php?token="+myToken+"&server_key="+serverKey) 
    #wait 16 minutes before spawning a gift
    time.sleep(960)
    reelInTheGift()