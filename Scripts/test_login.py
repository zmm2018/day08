
# 导包,如果用控制台运行的话,PYTEST找不到根目录,只会找同级目录,sys.path.append就是把当前文件的根目录添加到pytest的path中
import os,sys
sys.path.append(os.getcwd())


from Base.get_driver import get_driver
from Page.page_login import PageLogin


class TestLogin():

    # 初始化方法
    # 把开始运行的前置代码中的driver 实例化 搞一个变量  get_driver中的返回值也就是dreiver给page_login的类,self.login(login就是个变量)就是driver,
    def setup_class(self):
        self.login=PageLogin(get_driver())

    # 结束方法
    def teardown_class(self):
        self.login.driver.quit()

    # 测试方法
    # 函数的参数中,把page_login中输入框的文本写到这边,运用page的方法
    def test_login(self,username="1330003033",pwd="136474"):
        self.login.page_input_username(username)
        self.login.page_input_password(pwd)
        self.login.page_click_login_btn()


# 这是右键运行的方法,不用导包os
# if __name__ == '__main__':
#     pytest.mark("-s test_login.py")