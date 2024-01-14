import os
import csv
import sys
import json
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

def get_cases(path):
    try:
        with open(path, 'r', encoding='utf-8') as fr:
            return [row for row in csv.DictReader(fr)]
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

def generate_python_script_and_write(template_path, result_path, **kwargs):
    try:
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(template_path)
        with open(result_path, 'a') as f:
            f.write(template.render(**kwargs) + "\n\n")
    except Exception as e:
        print(f"Error generating python script: {e}")

def demo_generate(case_path, json_dir):
    cases = get_cases(case_path)
    for case in cases:
        try:
            result_path = f"{json_dir}/{case['req_key']}/test_{case['req_key']}.py"
            parent_dir = os.path.dirname(result_path)
            os.makedirs(parent_dir, exist_ok=True)

            # 生成作者信息和依赖
            author_data = {"author": case["author"], "date": datetime.now()}
            generate_python_script_and_write("author.j2", result_path, **author_data)
            generate_python_script_and_write("dependence.j2", result_path)

            # 生成测试用例
            req_data = {
                "title": case["desc"],
                "params": {"req_key": case['desc'], "binary_data": [], "req_json": "{a: b}"},
                "expect": {}
            }

            # 生成json文件
            json_file = f"{json_dir}/{case['req_key']}/{case['region']}/{case['desc']}.{case['region']}.json"
            os.makedirs(os.path.dirname(json_file), exist_ok=True)
            json.dump([req_data], open(json_file, "w", encoding='utf-8'), ensure_ascii=False)

            data = {
                'desc': case['desc'],
                'env_type': case['region'],
                'file_path': json_file.split('/')[-1].split(".")[0],
                'filename': case['desc'],
            }
            generate_python_script_and_write("code.j2", result_path, **data)
        except Exception as e:
            print(f"Error processing case '{case['req_key']}': {e}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <case_path> <json_dir>")
        sys.exit(1)

    case_path = sys.argv[1]
    json_dir = sys.argv[2]
    demo_generate(case_path, json_dir)

