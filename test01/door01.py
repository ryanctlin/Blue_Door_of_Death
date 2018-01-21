from park.park import Park

park = Park(
    '108.61.209.209',
    4002,
    '578e820911f24e039733b45e4882b73e301f813a0d2c31330dafda84534ffa23',
    '1.1.1'
)

info = park.accounts().account(address='DHkEspm6H1XVwqajxDwQa99fYERMxw4w3R')
#print(info)

query = park.transactions().transactions({'recipientId': 'DHkEspm6H1XVwqajxDwQa99fYERMxw4w3R'})
#print(query)


temp1 = []
for key, value in query.items():
    aValue = value
    temp1.append(aValue)

#print(temp1[1])
#print(len(temp1[1]))

transactid = []
senderList = []
timestamp = []
if (len(temp1[1])>0):
    for item in temp1[1]:
        #print(item['senderId'])
        transactid.append(item['id'])
        senderList.append(item['senderId'])
        timestamp.append(item['timestamp'])

print(transactid)
print(senderList)
print(timestamp)