from main import *

# try:
#     for i in result:
#         result.pop(result.index(i))
#         count += 1
#         if count >= 5:
#             break
# finally:
#     with open(r'doneId.txt', 'w+', encoding='utf-8') as file:
#         file.truncate(0)
#         for i in result:
#             file.write(i + '\n')


file_path = 'ChatId.txt'


def phonenumberchange():
    line = readwechatid(file_path)
    newline = line[:10]
    newline = list(newline)
    # int_str = [int(x) for x in newline]
    print(newline)
    workdone = []
    for i in newline:
        l = list(i)
        if l[-4] == '8':
            l[-4] = '9'
        elif l[-4] == '7':
            l[-4] = '8'
        elif l[-4] == '6':
            l[-4] = '7'
        elif l[-4] == '5':
            l[-4] = '6'
        elif l[-4] == '4':
            l[-4] = '5'
        elif l[-4] == '3':
            l[-4] = '4'
        elif l[-4] == '2':
            l[-4] = '3'
        elif l[-4] == '1':
            l[-4] = '2'
        elif l[-4] == '0':
            l[-4] = '1'
        i = ''.join(l)
        workdone.append(i)
        print(newline)
    with open('newid.txt', 'w', encoding='utf-8') as file:
        for i in workdone:
            file.write(i + '\n')


phonenumberchange()
