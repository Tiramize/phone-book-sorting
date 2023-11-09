import re
pattern = r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7, 10}$'
phone = input('Введите и телефона -> ')
print('phone =', phone, type (phone))
if re.fullmatch(pattern, phone): 
    print('Correct number')
else:
    print('Incorrect number')
    exit(1)
phone_book = [ phone, '8(495) 430-23-97', '+7-4-9-5-43-023-97', '4-3-0-2-3-9-7', '8-495-430', '8(918) 523-84-95']
print('phone book = ', phone_book, type (phone_book)) 
phone_book1 = [s.replace('-','').replace('(', '').replace(')','').replace(' ', '')
            for s in phone_book]
print('phone book1 = ', phone_book1, type (phone_book1))
for i in range(len(phone_book1)):
if len(phone_book1[i]) == 7:
      phone_book1[i]='+7495' + phone_book1[1]
elif len(phone_book1[i]) == 10:
      phone_book1[i]='+7' + phone_book1[1]
elif len(phone_book1[i]) == 11:
      phone_book1[i]='+7' + phone_book1[1][1:]
#phone book1[1] phone book1[1].replace('8' +7 1 print('phone book1=', phone book1, type (phone_book1))
print('phone book1 = ', phone_book1, type(phone_book1))
for i in range(1, len(phone_book1)):
if phone_book1[0] == phone_book1[i]:
print ("YES")
else:
print ("NO")