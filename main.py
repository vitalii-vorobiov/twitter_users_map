from flask import Flask
from flask import render_template
from flask import request
import user
import twitter2
import map_create

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/',methods=["POST"])
def input_page():
    user_id = request.form['user_id']
    num = request.form['friends']
    user_lst = user.main(user_id)
    friends_lst = twitter2.main(user_id, num)
    map_create.main(user_lst, friends_lst, num)
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    return render_template('map_html.html')


if __name__ == "__main__":
    app.run(debug=True)
