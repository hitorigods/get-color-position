# インストール手順

管理者権限でコマンドプロンプトもしくは PowerShell を開く

## Python をインストール

※インストール済みなら不要

```
$ python -m pip install --upgrade pip
```

## ライブラリをインストール

```
$ pip install opencv-python numpy PyYAML
```

# 設定

`config.yaml` が設定ファイル

# 実行

```
$ python main.py
```

# 補足

- 画像の左上隅が原点 (0, 0)で x と y 方向のピクセル数を格納
- ファイルは`UTF-8`、改行コードは`LF`形式
- 出力ファイルは`output_path`に指定したフォルダ内に保存されます
- CSV と JSON の両方の形式で出力されます
- CSV と JSON の出力データには、読み込んだ画像のファイル名（拡張子を除く）、拡張子、色名、x 座標、y 座標が含まれます
