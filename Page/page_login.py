from selenium.webdriver.common.by import By

from Base.base import Base

loc_username = By.ID,"com.vcooline.aike:id/etxt_username"
loc_password = By.ID,"com.vcooline.aike:id/etxt_pwd"
loc_bth = By.ID,"com.vcooline.aike:id/btn_login"

# 这个类继承base中的类
class PageLogin(Base):

    # 封装输入手机号,text代表输入文本  输入是 input
    def page_input_username(self,text):

        # 注意:text中的值,是固定的,test_login中的是动态的
        # 调用的base类 封装的输入方法  因为继承Base，所以直接通过self.xxxx,调用定位元素的变量,后面写出要输入的内容
        self.base_input(loc_username,text)


    # 封装输入密码   输入是 input
    def page_input_password(self,text):

        #调用的base类 封装的输入方法
        self.base_input(loc_password,text)


    # 封装点击登录  登录是点击 click
    def page_click_login_btn(self):
        self.base_click(loc_bth)