import urllib2
import time

def read_string(string, size):
    return string[:size]
def read_string_from_back(string, size):
    return string[size*-1:]
def slice_string(string, size):
    return string[size:]
def http_new_get(url):
    return urllib2.urlopen(url).read()
def try_to_claim_gift(currentGiftKey, myToken, serverKey):
    #wait 15 minutes before spawning a gift
    time.sleep(930)
    itemname = slice_string(http_new_get("http://l3.ajf.me/gg2/giveGift.php?key="+currentGiftKey+"&token="+myToken+"&server_key="+serverKey),16)
    if (len(itemname) == 0):
        print "Error in claiming gift"
        print "Retrying in another 15 minutes"
    else:
        print itemname
print "Arctic's Lightweight Itemserver Miner Alpha v0.03"
myToken = ''
while (len(myToken) != 15):
    myName = raw_input("Enter your username: ")
    myKey = raw_input("Enter your userkey: ")
    myToken = http_new_get("http://l3.ajf.me/gg2/getToken.php?user_name="+myName+"&user_key="+myKey)
    if (len(myToken) != 15):
        print ("Incorrect login")
print "ALIM is now harvesting items"
loop = 1
while (loop == 1):
    #vars
    myToken = http_new_get("http://l3.ajf.me/gg2/getToken.php?user_name="+myName+"&user_key="+myKey)
    serverStartResponse = http_new_get("http://l3.ajf.me/gg2/serverStart.php")
    serverKey = read_string(serverStartResponse, 15)
    currentGiftKey = read_string_from_back(serverStartResponse, 15)
    myLoadout = http_new_get("http://l3.ajf.me/gg2/getLoadout.php?token="+myToken+"&server_key="+serverKey) 
    try_to_claim_gift(currentGiftKey, myToken, serverKey)