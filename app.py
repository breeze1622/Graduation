from flask import Flask, render_template, request
from data import salary_list

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    # 返回网页文件
    return render_template('index.html')


@app.route('/login', methods=["POST"])
def hello_login():
    # 登录到服务器获取用户名与密码，然后进行校验，再记录信息
    # print(request.form)
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)

    # 添加固定用户名和密码进行验证
    valid_username = "admin"
    valid_password = "4321"

    if username == valid_username and password == valid_password:
        # 登录成功之后返回后台页面
        return render_template('admin.html', salary_list=salary_list)
    else:
        # 密码错误，显示对话框或返回错误信息
        error_message = "密码错误"
        return render_template('login.html', error_message=error_message)



@app.route('/delete/<name>')
def hello_delete(name):  # put application's code here
    # 删除逻辑 先找到信息,然后再删除
    for salary in salary_list:
        if salary['name'] == name:
            salary_list.remove(salary)
    return render_template('admin.html',
                           salary_list=salary_list)


@app.route('/change/<name>')
def hello_change(name):  # put application's code here
    for salary in salary_list:
        if salary['name'] == name:
            # 在前端进行修改
            return render_template('change.html',
                                   user=salary)

    return render_template('admin.html',
                           salary_list=salary_list)


@app.route('/changed/<name>', methods=["POST"])
def hello_changed(name):
    """进行修改 得到提交的信息"""
    for salary in salary_list:
        if salary['name'] == name:
            salary['name'] = request.form.get('name')
            salary['department'] = request.form.get('department')
            salary['position'] = request.form.get('position')
            salary['salary'] = request.form.get('salary')

    return render_template('admin.html',
                           salary_list=salary_list)


@app.route('/add')
def hello_add():
    return render_template('add.html')


@app.route('/add2', methods=['POST'])
def hello_add2():
    salary = {}
    # 获取浏览器发送过来的数据
    salary['name'] = request.form.get('name')
    salary['department'] = request.form.get('department')
    salary['position'] = request.form.get('position')
    salary['salary'] = request.form.get('salary')
    # 将数据保存
    salary_list.insert(0, salary)
    # 返回保存之后的页面
    return render_template('admin.html',
                           salary_list=salary_list)

if __name__ == '__main__':
    app.run()
