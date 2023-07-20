def readWechatID(filePath):
    lines = []
    with open(filePath, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            lines.append(line)
    return lines

result = readWechatID(r"./doneId.txt")
count = 0
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
for i in range(60):
    print(i)