print('well come sbi bank')
print('insert atm card')
print('choose telugu(1),english(2),hindi(3)')
pin=int(input('enter pin'))
transction=int(input('enter type of transction'))
if transction==1:
    print('withdraw')
    if amount<=10000:
        print('collect u r cash')
elif transction==2:
    print('deposit') 
elif transction==3:
    print('checking')
elif transction==4:
    print('change pin') 
    if new12pin=='yes':
        print('changed u r pin') 
elif transction==5:
    print('exit')                    