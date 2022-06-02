import datetime as dt


def decode(text):
    res = ''
    for i in range(len(text)):
        new_symb = ord(text[i])
        if ord('a') <= new_symb <= ord('z'):
            if i % 2 == 0:
                new_symb -= seconds
                if new_symb < ord('a'):
                    new_symb = ord('z') - (ord('a') - new_symb) + 1
            else:
                new_symb += seconds
                if new_symb > ord('z'):
                    new_symb = ord('a') + new_symb - ord('z') - 1
        res += chr(new_symb)
    return res


def code(text):
    res = ''
    for i in range(len(text)):
        new_symb = ord(text[i])
        if ord('a') <= new_symb <= ord('z'):
            if i % 2 == 0:
                new_symb += seconds
                if new_symb > ord('z'):
                    new_symb = ord('a') + new_symb - ord('z') -1
            else:
                new_symb -=  seconds
                if new_symb < ord('a'):
                    new_symb = ord('z') - (ord('a') - new_symb) + 1
        res += chr(new_symb)
    return res 


seconds = dt.datetime.now().second
print("TIME:", seconds)
while seconds > 26:
    seconds -= 26
# print(seconds)
# cur_date = dt.date.today().day
text = input('Enter text: ')
res = code(text)
print("Result:", res)
password = int(input('Enter seconds: '))
while password > 26:
    password -= 26
seconds = password
decode = decode(res)
print("MSG", decode)
