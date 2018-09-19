class User():
    def __init__(self,id,name,password,token):
        self.id = id
        self.name = name
    def save(self):
        print('-----保存用户---')

    def login(self):
        print('登陆成功')