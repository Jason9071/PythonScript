from web3 import Web3, EthereumTesterProvider
import json

f = open("whitelist.txt", "r", encoding="utf-8")
adr = f.read()

f.close()
adrs = adr.split()

f = open("whitelist.json", "w", encoding="utf-8")
count = 0
wl = '['

wtf = []
i = 2 ;
for a in adrs :
    if ( Web3.isAddress(a) == False ) :
        wtf.append([a, i])
    else :
        wl = wl + '"' + a + '", '
        count = count + 1
       
    i = i + 1
print(count)
wl = wl[0:len(wl)-2]
wl = wl + ']'
wlJson = {
    "whitelist" : wl
}
wlJsonStr = json.dumps(wlJson, indent=4)
f.write(wlJsonStr)
f.close()

for w in wtf :
    print(w)
