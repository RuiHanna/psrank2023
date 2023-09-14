from flask import Flask, render_template, request
app = Flask(__name__)

# 登录


@app.route("/login")
def register():
    return render_template("login.html")

# 公告


@app.route("/login/announcement", methods=["POST", 'GET'])
def announcement():
    name = request.form.get("name")
    password = request.form.get("password")
    global identity
    identity = request.form.get("identity")
    print("name:{}\npassword:{}\nidentity:{}\n".format(name, password,
                                                       identity))
    if identity == "super_admin":
        return render_template("super_make_announcement.html")
    elif identity == "user" or identity == 'admin':
        return render_template("announcement.html")
    else:
        return render_template("login.html")


# 公告转 用户或管理员

@app.route("/user_admin", methods=['GET', 'POST'])
def user_admin():
    if identity == "user":
        return render_template("user_mine.html")
    else:
        return render_template("admin_home_application.html")

# 公告-搜索


@app.route("/announcement/search")
def announcement_search():
    return render_template("announcement.html")


# ---------------------------------------------------------------------------------------------------------#
# 超级管理员-创建公告


@app.route("/super_admin/make_announcement", methods=['GET', 'POST'])
def make_announcement():
    return render_template("super_make_announcement.html")

# 超级管理员-创建公告-历史记录


@app.route("/super_admin/announcement_history", methods=['GET', 'POST'])
def announcement_history():
    return render_template("super_announcement_history.html")

# 超级管理员-编辑管理员


@app.route("/super_admin/edit_admin", methods=['GET', 'POST'])
def edit_admin():
    return render_template("super_edit_admin.html")

# 超级管理员-系统通知


@app.route("/super_admin/message")
def message():
    return render_template("super_message.html")

# 超级管理员-活动消息


@app.route("/super_admin/ranking_message", methods=['POST', 'GET'])
def ranking_message():
    if request.method == 'GET':
        return render_template("super_ranking_message.html")
    else:
        name = request.form.get("name")
        intro = request.form.get("introduction")
        start_time = request.form.get("start_time")
        end_time = request.form.get("end_time")
        print("name:{}\nintroduction:{}\nstart_time:{}\nend_time:{}\n".format(
            name, intro, start_time, end_time))
        return render_template("super_ranking_message.html")

# ---------------------------------------------------------------------------------------------------------#

# 用户-我的


@app.route("/user/mine", methods=['GET', 'POST'])
def user_mine():
    return render_template("user_mine.html")


# 用户-创建小组

@app.route("/user/make_group")
def user_make_group():
    return render_template("user_make_group.html")


# 用户-系统通知

@app.route("/user/message")
def user_message():
    return render_template("user_message.html")


# 用户-活动排名

@app.route("/user/ranking_message", methods=['GET', 'POST'])
def user_rank():
    return render_template("user_rank.html")

# 用户-审核


@app.route("/user/check", methods=['GET', 'POST'])
def user_check():
    return render_template("user_check.html")
# ---------------------------------------------------------------------------------------------------------#


# 管理员-主页-申请


@app.route("/admin/home/application", methods=['GET', 'POST'])
def admin_home_application():
    return render_template("admin_home_application.html")


# 管理员-主页-活动排名


@app.route("/admin/home/rank")
def admin_home_rank():
    return render_template("admin_home_rank.html")


# 管理员-主页-系统通知


@app.route("/admin/home/message")
def admin_home_message():
    return render_template("admin_home_message.html")
# ---------------------------------------------------------------------------------------------------------#


# 管理员-裁判-个人


@app.route("/admin/judgement/person")
def admin_judgement_person():
    return render_template("admin_judgement_person.html")


# 管理员-裁判-小组


@app.route("/admin/judgement/group")
def admin_judgement_group():
    return render_template("admin_judgement_group.html")

# ---------------------------------------------------------------------------------------------------------#

# 管理员-审核-待审批


@app.route("/admin/checker/yet")
def admin_checker_yet():
    return render_template("admin_checker_yet.html")


# 管理员-审核-已审批


@app.route("/admin/checker/already")
def admin_checker_already():
    return render_template("admin_checker_already.html")

# ---------------------------------------------------------------------------------------------------------#

# 管理员-游戏-添加游戏


@app.route("/admin/game/add")
def admin_game_add():
    return render_template("admin_game_add.html")


# 管理员-游戏-设置规则


@app.route("/admin/game/rule")
def admin_game_rule():
    return render_template("admin_game_rule.html")


if __name__ == '__main__':
    app.run()
