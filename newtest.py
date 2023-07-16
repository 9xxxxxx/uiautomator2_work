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
print(result)
print(list(set(result)))
