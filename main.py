import urllib2 as u
import time
import data

#There's probably a built in function for this but I'm too lazy to find it so I'll write my own
def read_string(string, size, pos=0):
    output = ''
    while (pos < size):
        output += string[pos]
        pos += 1
    return output

#just for fun
def http_new_get(url):
    response = u.urlopen(url).read()
    return response

#pfft no
def attemptGift():
    response = http_new_get("http://l3.ajf.me//gg2/giveGift.php?key="+currentGiftKey+"&token="+myToken+"&server_key="+serverKey)
    print "attempted gift"
    print response


    
#vars
current_time = int(round(time.time() * 1000))
startTime = current_time
myName = "arctic"
myKey = "vk6lxQx3xkUBfiv"
serverStartResponse = http_new_get("http://l3.ajf.me/gg2/serverStart.php")
serverKey = read_string(serverStartResponse, 15)
currentGiftKey = read_string(serverStartResponse, 15, 16)
myToken = http_new_get("http://l3.ajf.me/gg2/getToken.php?user_name=arctic&user_key=vk6lxQx3xkUBfiv")
myLoadout = http_new_get("http://l3.ajf.me/gg2/getLoadout.php?token="+myToken+"&server_key="+serverKey)

#other stuff
# name1 = "123456"
# key1 = "jFhwE3lHp9JLwBH"
# token1 = http_new_get("http://l3.ajf.me/gg2/getToken.php?user_name="+name1+"&user_key="+key1)
# loadout1 = http_new_get("http://l3.ajf.me/gg2/getLoadout.php?token="+token1+"&server_key="+serverKey)

# name2 = "DrunkenSteve"
# key2 = "wsgm03qVeG1K6xM"
# token2 = http_new_get("http://l3.ajf.me/gg2/getToken.php?user_name="+name2+"&user_key="+key2)
# loadout2 = http_new_get("http://l3.ajf.me/gg2/getLoadout.php?token="+token2+"&server_key="+serverKey)

# name3 = "arctic2"
# key3 = "spYU4WsINihCGpe"
# token3 = http_new_get("http://l3.ajf.me/gg2/getToken.php?user_name="+name3+"&user_key="+key3)
# loadout3 = http_new_get("http://l3.ajf.me/gg2/getLoadout.php?token="+token3+"&server_key="+serverKey)

# name4 = "arctic2"
# key4 = "spYU4WsINihCGpe"
# token4 = http_new_get("http://l3.ajf.me/gg2/getToken.php?user_name="+name4+"&user_key="+key4)
# loadout4 = http_new_get("http://l3.ajf.me/gg2/getLoadout.php?token="+token4+"&server_key="+serverKey)
    
for n in data.usernames[:len(data.usernames)]:
    http_new_get("http://l3.ajf.me/gg2/getLoadout.php?token="+n+"&server_key="+serverKey)
    print n
    
for p in data.keys[:len(data.keys)]:
    http_new_get("http://l3.ajf.me/gg2/getLoadout.php?token="+p+"&server_key="+serverKey)
    
#init
print "Arctic's Lightweight Itemserver Miner Alpha v0.01"
#print "My Loadout:",myLoadout
print "Server Start Response",serverStartResponse
print "My Token:", myToken
print "current_time:",current_time

giftDelay = current_time+1000*60*15

x = 1
"""while x == 1:
    if (int(round(time.time() * 1000)) > giftDelay):
        attemptGift()"""

#Refresh Token
if (startTime + 1000*60*60*2 < (int(round(time.time() * 1000)))):
    startTime = int(round(time.time() * 1000))
    myToken = http_new_get("http://l3.ajf.me/gg2/refreshToken.php?user_name="+myName+"&user_key="+serverKey+"&token="+myToken)
    print "Token refreshed"
    print "New Token:",myToken

#do stuff 

# nope, this shit dont work
#print 'ALIM is now harvesting items, please be patient and use this time to watch some anime or "other" things'
#attemptGift()

#TODO: print out message every time a gift is outputted

raw_input()



# C:\Users\Jason\Documents\GitHub\ItemServer-Harvester>main
# 'main' is not recognized as an internal or external command,
# operable program or batch file.

# C:\Users\Jason\Documents\GitHub\ItemServer-Harvester>main.py
  # File "C:\Users\Jason\Documents\GitHub\ItemServer-Harvester\main.py", line 89

    # ^
# SyntaxError: EOF while scanning triple-quoted string literal

# C:\Users\Jason\Documents\GitHub\ItemServer-Harvester>main.py
# Arctic's Lightweight Itemserver Miner Alpha v0.01
# Server Start Response aMPFnu6Ff4fVPbzqFMAeCJIEtGcINQ
# My Token: vW6cNZwXD1QW1b6
# current_time: 1397794224334
