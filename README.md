# ファイルを共有できるツール

これは、同じ LAN 内でファイルを共有できるツールです。

![logo](https://raw.githubusercontent.com/rihitosan/file_kyouyuu/main/logo.png)

## 使い方

① [参照]ボタンを押してファイルを選ぶ 。

②スマートフォンで表示されている QR コードを読み込む

③[共有(ウィンドウを閉じる)]ボタンを押す

④スマートフォンから QR コードの URL にアクセスする

## 注意

[共有(ウィンドウを閉じる)]ボタンを押さない限り、他の端末にファイルは共有されません。


ファイルを共有するときは共有する他の端末と同じネットワークに接続してください。


## 実行

改造するには Python 3 が必要です。

必要なライブラリ(インストール方法)

pip install flask

pip install qrcode

## py2exe または、cx_freeze で exe 化

exe 化するには、flask（jinja2）の依存関係でエラーが出てしまう可能性があるので、

```
(python がインストールされているディレクトリ)\Lib\site-packages\jinja2\__init__.py
```
に、 ```import ext``` を追加してください。

そして、このコマンドで exe ファイルが出来ます。


py2exe
```
python setup_py2exe.py py2exe
```

cx_freeze
```
python setup_cx.py build
```

py2exe, cx_freeze Python 3.9 で動作確認 

# Pyinstaller で exe 化

```
pyinstaller --onefile --noconsole --icon=icon.ico main.py
```

5 月 15 日 Uniant 内でこのプロジェクトの開発が活発でないためこのリポジトリを公開しました。by rihitosan
