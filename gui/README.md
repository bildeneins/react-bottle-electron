# bottle + react + electron streaming
Bottleでカメラ映像をストリーミングしながら並列でリクエストを受け付けるサンプルです。
必要なライブラリのインストール
```shell
$ pip install bottle, gunicorn, gevent
```
バックエンドの起動
```shell
$ cd core
$ gunicorn -w 4 -b 0.0.0.0:8080 -k gevent app:app
```
フロントエンドのsetup
```shell
$ cd gui
$ yarn
```
フロントエンドの移動
```shell
$ yarn start
```

## MACでのエラーについて
Macにて実行時fork()が使えないという旨のエラーが出ることがあります。
下の記事に従って解決できます。
https://qiita.com/lichtshinoza/items/ed03f42614ee5605974d
