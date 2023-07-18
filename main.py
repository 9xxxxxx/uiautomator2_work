# coding: utf-8
import time
import uiautomator2 as u2

d = u2.connect()


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


def checkuserstatus(wechatid):
    if d.xpath('//*[@resource-id="com.tencent.mm:id/j5_"]/android.widget.ImageView[1]').exists:
        print(wechatid, "该用户不存在")
        d(resourceId="com.tencent.mm:id/apy").click()
        return


def addFriends(wechatid):
    # doneidlist = readWechatID(done_path)
    # if wechatid in doneidlist:
    #     print(f'this id ({wechatid}) already added')
    #     return
    # 点击账号输入框激活输入，聚焦输入光标
    d(resourceId="com.tencent.mm:id/eg6").click()
    time.sleep(1)
    # 输入要添加的号码
    d.xpath('//*[@resource-id="com.tencent.mm:id/eg6"]').set_text(wechatid)
    # #输入完毕点击下方出现的搜索:xxxxxxxxxxxx
    d.xpath('//*[@resource-id="com.tencent.mm:id/j6x"]/android.widget.RelativeLayout[1]').click()
    # 判断用户状态
    # 等待虚拟页面加载完毕
    time.sleep(3)
    if not d(text='添加到通讯录').exists:
        print(wechatid + '  ' + "该用户不存在")
        return
    # #点击接下来要进行的操作按钮 这里是点击添加到通讯录
    d(resourceId="com.tencent.mm:id/khj").click()
    # 设置好友申请内容
    d(resourceId="com.tencent.mm:id/j0w").set_text(verifyContent)
    time.sleep(2)
    # 点击发送
    d(resourceId="com.tencent.mm:id/e9q").click()
    time.sleep(3)
    # 点击返回到添加好友页面
    d.xpath('//*[@resource-id="com.tencent.mm:id/g1"]').click()
    time.sleep(1)


def filterepeat():
    result = readWechatID(r"doneId.txt")
    result = list(set(result))
    with open(r'doneId.txt', 'w+', encoding='utf-8') as file:
        for i in result:
            file.write(i + '\n')


def main():
    # 点击右上角+号
    d(resourceId="com.tencent.mm:id/hy6").click()
    time.sleep(1)
    #  点击添加好友
    d.xpath('//android.widget.ListView/android.widget.LinearLayout[2]').click()
    time.sleep(1)
    # 聚焦输入框
    d(resourceId="com.tencent.mm:id/j69").click()
    time.sleep(1)
    phonelist = readWechatID(file_path)
    try:
        for i in phonelist:
            addFriends(i)
            phonelist.pop(phonelist.index(i))
    finally:
        with open('./freshId.txt', 'w', encoding='utf-8') as done_file:
            done_file.truncate(0)
            for i in phonelist:
                done_file.write(i + '\n')


if __name__ == '__main__':
    # 输出设备信息
    print(d.info)
    # 设置申请内容
    verifyContent = '您好，低价飞天茅台质量99.9%,对标正品，降低招待成本，提升饭桌规格！'
    # 设置文件路径
    done_path = u"./doneId.txt"
    file_path = u'./freshId.txt'
    # 主程序
    main()
