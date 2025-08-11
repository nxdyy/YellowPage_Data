import os
import yaml
import re
import time
import json
from pathlib import Path

script_dir = os.path.dirname(os.path.abspath(__file__))

def remove_non_numeric(string):
    return re.sub(r'\D', '', str(string))

def convert_phone_data(data, yaml_path):
    # 检查 basic 字段
    if 'basic' not in data:
        print(f"警告：{yaml_path} 缺少 basic 字段，已跳过。")
        return None

    basic = data['basic']
    name = basic.get('organization', '')
    # 头像路径推断
    rel_dir = os.path.relpath(os.path.dirname(yaml_path), os.path.join(script_dir, 'yellowpage_data'))
    img_name = os.path.splitext(os.path.basename(yaml_path))[0] + '.png'
    avatar_url = f"https://gitee.com/exthmui_chinasource/YellowPage_data/raw/Utsuho/data/{rel_dir.replace(os.sep, '/')}/{img_name}"

    # 电话
    phones = []
    for item in basic.get('cellPhone', []):
        if isinstance(item, dict):
            number = remove_non_numeric(item.get('number', ''))
            label = item.get('label', '')
        else:
            number = remove_non_numeric(item)
            label = ""
        phones.append({"number": number, "label": label})

    # 网站
    websites = []
    if 'url' in basic and basic['url']:
        websites.append({"url": basic['url'], "label": "官网"})

    return {
        "avatar": avatar_url,
        "phone": phones,
        "address": [],
        "website": websites,
        "name": name
    }

def process_directory(directory_path):
    directory = Path(os.path.join(script_dir, directory_path))
    all_data = []
    for file_path in directory.glob('**/*.yaml'):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = yaml.safe_load(f)
            item = convert_phone_data(content, str(file_path))
            if item:
                all_data.append(item)
    return all_data

if __name__ == "__main__":
    result = {
        "version": int(time.time()),
        "status": 0,
        "data": process_directory('yellowpage_data')
    }
    with open(os.path.join(script_dir, 'yellowpage_data.json'), 'w', encoding='utf-8') as out_file:
        json.dump(result, out_file, ensure_ascii=False, indent=4)
    print("已生成 yellowpage_data.json")