p=input()
plist=[0,0,0,0,0,0,0,0]
#상 하 좌 우 (오왼)(상하)
if 'a' in p:
    plist[1]=1
    plist[3]=1
    plist[4]=1
    plist[5]=1
if 'h' in p:
    plist[0]=1
    plist[2]=1
    plist[6]=1
    plist[7]=1
if 'b' in p:
    plist[4]=1
    plist[5]=1
if 'g' in p:
    plist[6]=1
    plist[7]=1
if '1' in p:
    plist[0]=1
    plist[1]=1
    plist[4]=1
    plist[6]=1
if '8' in p:
    plist[2]=1
    plist[3]=1
    plist[5]=1
    plist[7]=1
if '2' in p:
    plist[0]=1
    plist[1]=1
if '7' in p:
    plist[2]=1
    plist[3]=1
print(plist.count(0))