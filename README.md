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

改造するには python3が必要です。

必要なライブラリ(インストール方法)

pip install flask

pip install qrcode

## py2exe または、cx_freezeでexe化

exe化するには、flask(jinja2)の依存関係でエラーが出てしまう可能性があるので、

```
pythonがインストールされているディレクトリ\Lib\site-packages\jinja2\__init__.py
```
に、 ```import ext```を追加してください。

そして、このコマンドでexeファイルが出来ると思います。


py2exe
```
python setup_py2exe.py py2exe
```

cx_freeze
```
python setup_cx.py build
```

py2exe,cx_freeze python3.9で動作確認 
