from selenium.webdriver.support.wait import WebDriverWait


class Base():

# 在base类中,封装常用的公共方法
    #实例化driver,方便后面调用driver,实例参数
    def __init__(self,driver):
        self.driver=driver

# 封装元素定位的方法   loc下的底层是By.XPATH的方法(self,by=By.XPATH,values=), 得出的结果就是元组解包后的样子,所以现在用"*"loc 来代替
    # 这边的显示等待中用tinmeout  和 poll_frequency 是想要整个代码的灵活性
    def base_find_element(self,loc,timeout=30,poll=0.5):

        # 显式等待是因为会出现 tousi(提示的黑底白字的框),用显示等待给提示框时间
        # retunre 是因为元素封装完之后需要返回元素
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))

#封装点击的方法  继续调用定位元素的方法base_find_element,loc解包
    def base_click(self,loc):
        self.base_find_element(loc).click()

#封装输入的方法  继续调用定位元素的方法base_find_element,loc解包,text代表输入文本
    def base_input(self,loc,text):

        # 查找元素
        el = self.base_find_element(loc)

        # 清除内容  不管是输入什么都要首先清除
        el.clear()

        # 输入内容
        el.send_keys(text)