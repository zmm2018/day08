import yaml,sys,os

def read_yaml():
    with open(os.getcwd() + os.sep+"Data" +os.sep+"test_login")as f:
        return yaml.load(f)

if __name__ == '__main__':


arrs=[]
for i in get_yaml1().values():
    arrs.append((i.get("username"),i.get("password"),i.get("expect_toast")))

print(arrs)