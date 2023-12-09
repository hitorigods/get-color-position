# 連番画像に存在する特定色の座標の取得

- 画像の左上隅が原点 (0, 0)で x と y 方向のピクセル数を格納
- `config.yaml` が設定ファイル
- CSV と JSON の両方の形式で出力し、読み込んだ画像のファイル名（拡張子を除く）、拡張子、カラーキー、x 座標、y 座標が含まる
- ファイルは`UTF-8`、改行コードは`LF`形式
- 色指定は`RGB値`で定義

# インストール手順

管理者権限でコマンドプロンプトもしくは PowerShell を開く

## Python をインストール

```
python -m pip install --upgrade pip
```

## ライブラリをインストール

```
pip install opencv-python numpy PyYAML
```

# 実行

```
python main.py
```
