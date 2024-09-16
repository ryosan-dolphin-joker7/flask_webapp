# flask_appパッケージからアプリケーション作成関数をインポート
from flask_app import create_app

# アプリケーションを作成
app = create_app()

# エントリーポイント：ローカルで実行する場合に使う
if __name__ == '__main__':
    # デバッグモードでFlaskアプリを起動（開発中はTrue、本番ではFalse推奨）
    app.run(host='0.0.0.0', port=5000, debug=True)
