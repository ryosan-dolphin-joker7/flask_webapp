from flask_app import app
from flask import render_template, request,redirect, url_for
import sqlite3
DATABASE = 'database.db'

@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    db_books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()

    books = []
    for row in db_books:
        books.append({
            'title': row[0],
            'author': row[1],
            'year': row[2]
        })

    return render_template('index.html', books=books)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/register', methods=['POST'])
def register():
    title = request.form['title']
    author = request.form['author']
    year = request.form['year']

    conn = sqlite3.connect(DATABASE)
    conn.execute('INSERT INTO books VALUES (?, ?, ?)', [title, author, year])
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route("/Request_form", methods=['GET','POST'])
def Request_form():
    # レスポンスオブジェクトを取得する
    #response = make_response(render_template("Request_form.html"))

    # クッキーを設定する
    #response.set_cookie("flaskbook key", "flaskbook value")

    # セッションを設定する
    #session["username"] = "ichiro"

    # レスポンスオブジェクトを返す
    return render_template("Request_form.html")

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # form属性を使ってフォームの値を取得する
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        # 入力チェック
        is_valid = True
        if not username:
            flash("ユーザ名は必須です")
            is_valid = False

        if not email:
            flash("メールアドレスは必須です")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("メールアドレスの形式で入力してください")
            is_valid = False

        if not description:
            flash("問い合わせ内容は必須です")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))

        # メールを送る
        send_email(
            email,
            "問い合わせありがとうございました。",
            "contact_mail",
            username=username,
            description=description,
        )

        # 問い合わせ完了エンドポイントへリダイレクトする
        flash("問い合わせ内容はメールにて送信しました。問い合わせありがとうございます。")

        # contactエンドポイントへリダイレクトする
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")