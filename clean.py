import os
import re
import yaml

POSTS_DIR = "_posts"
FIELDS_TO_CLEAN = ["title", "blurb"]

def clean_quotes():
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith(".md"):
            continue

        path = os.path.join(POSTS_DIR, filename)

        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if lines[0].strip() != "---":
            continue

        # 找到 front matter 结束位置
        end_idx = None
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == "---":
                end_idx = i
                break
        if end_idx is None:
            continue

        yaml_block = ''.join(lines[1:end_idx])
        rest_of_file = ''.join(lines[end_idx+1:])

        try:
            meta = yaml.safe_load(yaml_block)
        except yaml.YAMLError:
            print(f"⚠️  YAML解析失败: {filename}")
            continue

        changed = False
        for key in FIELDS_TO_CLEAN:
            if key in meta and isinstance(meta[key], str):
                original = meta[key]
                cleaned = re.sub(r'^["\']+(.*?)["\']+$', r'\1', original.strip())
                if cleaned != original:
                    meta[key] = cleaned
                    changed = True

        if changed:
            # 重新构建 YAML
            new_yaml = yaml.dump(meta, allow_unicode=True, sort_keys=False)
            new_content = f"---\n{new_yaml}---\n{rest_of_file}"

            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Cleaned quotes in: {filename}")
        else:
            print(f"✔️ No change needed: {filename}")

if __name__ == "__main__":
    clean_quotes()
