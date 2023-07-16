import time

import uiautomator2 as u2

# 通过wifi连接
d = u2.connect("192.168.1.4")
print(d.info)


# 读取文件中的微信账号
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


# 通过搜索加好友
def addFriends(wechatID):
    c(resourceId="com.tencent.mm:id/l3").set_text(wechatID)
    c(resourceId="com.tencent.mm:id/n0").click()
    time.sleep(1)
    if c.exists(text="该用户不存在"):
        print(wechatID, "该用户不存在")
        c(resourceId="com.tencent.mm:id/kz").click()
    elif c.exists(text="添加到通讯录"):
        c(resourceId="com.tencent.mm:id/ct").click()
        time.sleep(1)
        if c.exists(text="发消息"):
            print(wechatID, "已经是您的好友")
            c.press("back")
            c(resourceId="com.tencent.mm:id/kz").click()
        elif c.exists(text="验证申请"):
            c(resourceId="com.tencent.mm:id/e49").set_text("111")
            c(resourceId="com.tencent.mm:id/ki").click()
            print(wechatID, "发送加好友请求成功")
            time.sleep(1)
            if c.exists(text="验证申请"):
                print(wechatID, "请求有点频繁")
                c.press("back")
            c.press("back")
            c(resourceId="com.tencent.mm:id/kz").click()
    elif c.exists(text="发消息"):
        print(wechatID, "已经是您的好友")
        c.press("back")
        c(resourceId="com.tencent.mm:id/kz").click()


# 主函数
def main():
    # 模拟点击右上角"+"按钮
    c(resourceId="com.tencent.mm:id/jb", className="android.widget.ImageView", instance=1).click()
    time.sleep(1)
    # 模拟点击添加朋友
    c(resourceId="com.tencent.mm:id/cx", text=u"添加朋友").click()
    time.sleep(1)
    # 模拟点击输入框
    c(resourceId="com.tencent.mm:id/d_4").click()
    file_path = u'freshId.txt'
    list = readWechatID(file_path)
    for i in list:
        time.sleep(1)
        addFriends(i)


