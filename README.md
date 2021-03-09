# ファイルを共有できるツール

これは、同じlan内でファイルを共有できるtoolです。

![logo](https://raw.githubusercontent.com/rihitosan/file_kyouyuu/main/logo.png)

## 使い方

① [参照]ボタンを押してファイルを選ぶ 。
②スマホで表示されているQRコードを読み込む
③[共有(ウィンドウを閉じる)]ボタンを押す
④スマホからQRコードのURLにアクセスする

## 注意

[共有(ウィンドウを閉じる)]ボタンを押さない限り、他の端末にファイルは共有されません。


ファイルを共有するときは共有する他の端末と同じネットワークに接続してください。


## 実行

実行するには(今のところ) python3が必要です。

必要なライブラリ(インストール方法)

pip install flask

pip install qrcode
