# Flaskフレームワークをインポート
from flask import Flask

# Flaskアプリケーションを作成する関数
def create_app():
    app = Flask(__name__)

    # app.py内のルート（ルーティング処理）をインポート
    from .app import app as app_routes
    app.register_blueprint(app_routes)

    # db.pyで定義されたデータベース初期化を実行
    from .db import create_books_table
    create_books_table()

    return app  # 作成したFlaskアプリケーションを返す
