from flask import Blueprint, render_template, request, redirect, url_for, flash
import sqlite3
# メールアドレスのバリデーションに必要なライブラリをインポート
from email_validator import validate_email, EmailNotValidError

# Blueprintを使ってルーティングをまとめる
app = Blueprint('app', __name__)

# データベースのパス
DATABASE = 'database.db'

# ホームページのルート
@app.route('/')
def index():
    # データベースに接続して本の情報を取得
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

    # 取得した本のリストをHTMLテンプレートに渡して表示
    return render_template('index.html', books=books)

# 本の登録フォームを表示するルート
@app.route('/form')
def form():
    return render_template('form.html')

# 本の登録を行うルート
@app.route('/register', methods=['POST'])
def register():
    title = request.form['title']
    author = request.form['author']
    year = request.form['year']

    # データベースに接続して本を登録
    conn = sqlite3.connect(DATABASE)
    conn.execute('INSERT INTO books VALUES (?, ?, ?)', [title, author, year])
    conn.commit()
    conn.close()

    # ホームページにリダイレクト
    return redirect(url_for('app.index'))

# 問い合わせフォームを表示するルート
@app.route("/Request_form", methods=['GET', 'POST'])
def Request_form():
    # クッキーやセッションを設定する部分はコメントアウトされていますが、必要なら使用可能
    # response = make_response(render_template("Request_form.html"))
    # response.set_cookie("flaskbook key", "flaskbook value")
    # session["username"] = "ichiro"
    
    # フォームのテンプレートを表示
    return render_template("Request_form.html")

# 問い合わせ完了ページを処理するルート
@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # フォームからデータを取得
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        # 入力のバリデーション
        is_valid = True
        if not username:
            flash("ユーザ名は必須です")
            is_valid = False

        if not email:
            flash("メールアドレスは必須です")
            is_valid = False
        else:
            try:
                validate_email(email)
            except EmailNotValidError:
                flash("正しいメールアドレスの形式で入力してください")
                is_valid = False

        if not description:
            flash("問い合わせ内容は必須です")
            is_valid = False

        # バリデーションエラーがあれば再度フォームにリダイレクト
        if not is_valid:
            return redirect(url_for("app.Request_form"))

        # メール送信処理を追加（send_email関数が設定されている前提）
        # send_email(
        #    email,
        #    "問い合わせありがとうございました。",
        #    "contact_mail",
        #    username=username,
        #    description=description,
        # )

        # 問い合わせ完了メッセージを表示してリダイレクト
        flash("問い合わせ内容をメールで送信しました。ありがとうございました。")
        return redirect(url_for("app.contact_complete"))

    # 問い合わせ完了ページを表示
    return render_template("contact_complete.html")
