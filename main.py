import cv2
import numpy as np
import yaml
import csv
import os
import glob
import json

# 設定ファイルを読み込む関数
def load_config(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        return yaml.safe_load(f)

# CSVファイルを作成する関数
def create_csv_file(file_path):
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['scene', 'ext', 'target', 'x', 'y'])

# JSONデータに情報を追加する関数
def add_to_json_data(data, img_path, color, cx, cy):
    data.append({
        'scene': os.path.basename(img_path).split('.')[0],
        'ext': os.path.splitext(img_path)[1][1:],
        'target': color,
        'x': cx,
        'y': cy
    })

# JSONファイルに書き込む関数
def write_to_json_file(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# 画像を処理する関数
def process_images(input_path, output_csv, output_json, colors):
    json_data = []
    for img_path in glob.glob(os.path.join(input_path, '*')):
        img = cv2.imread(img_path)
        for color, value in colors.items():
            lower = np.array(value, dtype=np.uint8)
            upper = np.array(value, dtype=np.uint8)
            mask = cv2.inRange(img, lower, upper)
            moments = cv2.moments(mask)
            if moments['m00'] != 0:
                cx = int(moments['m10'] / moments['m00'])
                cy = int(moments['m01'] / moments['m00'])
                with open(output_csv, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([os.path.basename(img_path).split('.')[0], os.path.splitext(img_path)[1][1:], color, cx, cy])
                add_to_json_data(json_data, img_path, color, cx, cy)
    write_to_json_file(output_json, json_data)

# 設定ファイルを読み込む
config = load_config('config.yaml')
# 入力パスを取得
input_path = config['input_path']
# 出力パスを取得
output_path = config['output_path']
# CSVファイルのパスを取得
output_csv = os.path.join(output_path, config['output_csv'])
# JSONファイルのパスを取得
output_json = os.path.join(output_path, config['output_json'])
# 色の辞書を取得
colors = config['colors']
# CSVファイルを作成
create_csv_file(output_csv)
# 画像を処理
process_images(input_path, output_csv, output_json, colors)
