from park.park import Park
import time
from FacialRecognition import facerec
#from user02 import user02


#-------------Function defintions----------------------------------------

def clockInit():
    park = Park(
        '108.61.209.209',
        4002,
        '578e820911f24e039733b45e4882b73e301f813a0d2c31330dafda84534ffa23',
        '1.1.1'
    )
    info = park.accounts().account(address='DHkEspm6H1XVwqajxDwQa99fYERMxw4w3R')
    blocklist = park.blocks().blocks()
    height = blocklist['count']
    #print(height)
    timeblock = park.blocks().blocks({'height': height})
    blocks = timeblock['blocks'][0]
    startTime = blocks['timestamp']
    #print(startTime)

    return startTime


def getquery(door_address):
    park = Park(
        '108.61.209.209',
        4002,
        '578e820911f24e039733b45e4882b73e301f813a0d2c31330dafda84534ffa23',
        '1.1.1'
    )

    #info = park.accounts().account(address='DHkEspm6H1XVwqajxDwQa99fYERMxw4w3R')
    #query = park.transactions().transactions({'recipientId': 'DHkEspm6H1XVwqajxDwQa99fYERMxw4w3R'})

    info = park.accounts().account(address= door_address) #set door address for park
    query = park.transactions().transactions({'recipientId': door_address, 'orderBy': 'timestamp:DESC'}) #find all transactions with door address as recipient

    #Extract information from query
    temp1 = []
    for key, value in query.items():
        aValue = value
        temp1.append(aValue)

    return temp1

def verify(temp1, user_address, timelimit, startTime): #import timestamp
    transactid = []
    senderlist = []
    timestamp = []
    for item in temp1[1]:
        #print(item['senderId'])
        transactid.append(item['id'])
        senderlist.append(item['senderId'])
        timestamp.append(item['timestamp'])

    #print(transactid)
    #print(senderlist)
    #print(timestamp)

    #Check if any of the transactions were sent by user
    lastIndex = -1
    for index, senderid in enumerate(senderlist):
        if senderid == user_address:
            lastIndex = index

    #If lastIndex was not overwritten with final transaction from user, i.e. there was no transaction
    if lastIndex == -1:
        return False #deny access

    #Check for time elapsed
    lastTime = timestamp[lastIndex]
    #print(lastTime)
    #print(transactid[lastIndex])

    #print(lastTime-startTime)
    if (lastTime-startTime) < timelimit and (lastTime-startTime) >= 0:
        return True
    else:
        return False

#--------------------Door Blockchain Function------------------------------------
def door02(Auth):
    timelimit = 1800
    countdown = 18
    door_address = 'DHkEspm6H1XVwqajxDwQa99fYERMxw4w3R'
    #user_address = 'DLf7YJA68w5bSX781HjqszxkfkQzEGAB8m'
    user_address = Auth
    #print(user_address)

    #Query and verification
    startTime = clockInit()

    #debug------------
    #time.sleep(30)

    temp1 = getquery(door_address=door_address)
    result = verify(temp1=temp1, user_address=user_address, timelimit=timelimit, startTime=startTime)
    #print(result)

    #Check decision
    # if result == True:
    #     print("WELCOME!")
    #     return True
    #-------------------

    while countdown > 0:
        temp1 = getquery(door_address = door_address)
        result = verify(temp1=temp1, user_address=user_address, timelimit=timelimit, startTime=startTime)
        #print(result)

        #Check decision
        if result == True:
            print("WELCOME!")
            return True

        time.sleep(10)
        countdown-= 1

    print("ACCESS DENIED") #will only activate if timer elapses


#----------------Main Function-----------------
person = facerec()
#print(person)

#Authorised Accounts
Auth = {'Theo': 'DLf7YJA68w5bSX781HjqszxkfkQzEGAB8m'}

door02(Auth[person])
