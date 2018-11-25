from appium import webdriver

# 用函数  实例化driver
def get_driver():
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # app的信息
    desired_caps['appPackage'] = 'com.vcooline.aike'
    desired_caps['appActivity'] = '.umanager.LoginActivity'

    # 声明我们的driver对象   返回到下面的代码中
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)