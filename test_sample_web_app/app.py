import json

from flask import Flask, render_template, request

from utils import server_communication
from utils.user_attr import UserAttr

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.errorhandler(404)
def error_404(error):
    return render_template("page_404.html"), 404


@app.route("/")
def root():
    return render_template("welcome.html")


@app.route("/new_user/")
def new_user():
    return render_template("new_user.html")


@app.route("/all_users/")
def all_users():
    response = server_communication.get_users()

    if not response or response.status_code != 200:
        return render_template("all_users.html", load_users_error=True)

    try:
        user_table = [(user[UserAttr.USERNAME], user[UserAttr.NAME], user[UserAttr.SURNAME], user[UserAttr.EMAIL],
                       user[UserAttr.BIRTHDAY], user[UserAttr.ADDRESS]) for user in json.loads(response.text)]
    except:
        return render_template("all_users.html", load_users_error=True)

    return render_template("all_users.html", users=user_table)


@app.route("/add_user", methods=["POST"])
def add_user():
    user_info = {}

    user_attributes = UserAttr().get_all()
    for user_attr in user_attributes:
        user_data = request.form.get(user_attr)
        if not user_data:
            return render_template("new_user.html", some_empty_user_data=True)
        user_info[user_attr] = user_data

    response = server_communication.add_user(user_info)
    if response == None:
        return render_template("new_user.html", server_is_down=True)
    elif response.status_code == 201:
        return render_template("new_user.html", user_added=True)
    elif response.status_code == 400:
        return render_template("new_user.html", invalid_user_data=True)
    else:
        # response.status_code == 500 or any other problem
        return render_template("new_user.html", save_user_error=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", use_reloader=False)
