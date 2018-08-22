from flask_httpauth import HTTPBasicAuth
from flask import Flask, render_template    #此行修改
app = Flask(__name__)
auth = HTTPBasicAuth()

app = Flask(__name__)

users = [
    {'username': 'Tom', 'password': '111111'},
    {'username': 'Michael', 'password': '123456'},
    {'username': 'admin', 'password': '333333'}
]


@auth.get_password
def get_password(username):
    for user in users:
        if user['username'] == username:
            return user['password']
    return None

# @app.route('/')
# @auth.login_required
# def index():
#     return "Hello, %s!" % auth.username()

@app.route('/')
def hello_world():
    return render_template('plan.html')     #此行修改

# 以下增加
#首页，8：00后显示当日计划，8：00前显示昨日计划
@app.route('/view_plan/')
def view_plan():
    return render_template('plan.html')           #此行修改

#历史计划的查询，输入日期，即可显示历史日期的计划
@app.route('/view_date/<date>')  #增加<date>
def view_date(date):               #把date传入显示函数
    return render_template('plan.html')           #此行修改

#车辆检修记录及基本信息。
@app.route('/view_carriage/<carnum>') #增加<carnum>
def view_carriage(carnum):              #把carnum传入显示函数
    return render_template('carriage.html')       #此行修改


@app.route("/jinjia2")
def jinjia2demo():
    return render_template("jinjia2.html", a_variable='hello jinjia2', b_variable = 'I am Yonghan',
                           navigation=["http://baidu.com", "http://www.goolge.com"])

# 以上增加
if __name__ == '__main__':
    app.run()

