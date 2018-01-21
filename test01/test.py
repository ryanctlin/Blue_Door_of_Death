from park.park import Park

park = Park(
    '108.61.209.209',
    4002,
    '578e820911f24e039733b45e4882b73e301f813a0d2c31330dafda84534ffa23',
    '1.1.1'
)
info = park.accounts().account(address='DHkEspm6H1XVwqajxDwQa99fYERMxw4w3R')
print(info)

#query = park.transactions().transaction('fb5ca7eb26ea13077351b8c16ecf459c0c670f6b8059860b890be84d0a30ed17')
query = park.transactions().transactions({'senderId': 'DLf7YJA68w5bSX781HjqszxkfkQzEGAB8m'})
print(query)
query1 = park.transactions().transactions({'senderId': 'DHkEspm6H1XVwqajxDwQa99fYERMxw4w3R'})
#print(query1)
#print(len(query['transactions']))

temp = []

for key, value in query.items():
    aValue = value
    temp.append(aValue)

print(temp)
print(len(temp))
#print(temp[1:][0][])

#temp1 = temp[1:][0][0]
#print(temp1['id'])

#transaction = park.transactions().create('DLf7YJA68w5bSX781HjqszxkfkQzEGAB8m', '1', 'wow this works', 'grief someone uniform snack unaware laundry bottom elegant carpet garbage typical vacant')