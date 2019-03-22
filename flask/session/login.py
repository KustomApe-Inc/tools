from flask import Flask, session, render_template, request, url_for, redirect

app = Flask(__name__)


# トップページ
@app.route('/')
def index():
    if 'user_id' in session:
        return 'sucess! user_id: ' + str(session['user_id'])
    else:
        return 'not login'


# ログイン
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user_id'] = request.form['user_id']
        return redirect(url_for('index'))
    return render_template('login.html')


# ログアウト
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))


# セッションを使うために、任意のキーを記述してください。
app.secret_key = 'A9I8A7C6A5D4E3M2Y1'

if __name__ == "__main__":
    app.run(debug=True)