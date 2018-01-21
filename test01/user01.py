from park.park import Park

def
park = Park(
    '108.61.209.209',
    4002,
    '578e820911f24e039733b45e4882b73e301f813a0d2c31330dafda84534ffa23',
    '1.1.1'
)
info = park.accounts().account(address='DLf7YJA68w5bSX781HjqszxkfkQzEGAB8m')
#print(info)

transaction = park.transactions().create('DHkEspm6H1XVwqajxDwQa99fYERMxw4w3R', '100000000', 'Open Door', 'fragile speed doctor grace idea give soda echo worry enhance raw rug')
