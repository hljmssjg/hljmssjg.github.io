import os
import re
import yaml
import datetime

POSTS_DIR = "_posts"

def slugify(value):
    value = value.lower()
    value = re.sub(r"[^\w\s-]", "", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value.strip("-")

def extract_front_matter(lines):
    if not lines or lines[0].strip() != "---":
        return None, None

    # 找结尾 --- ，支持多种换行格式
    end_idx = None
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return None, None

    yaml_block = "".join(lines[1:end_idx])
    rest_content = "".join(lines[end_idx+1:])

    try:
        meta = yaml.safe_load(yaml_block)
    except yaml.YAMLError:
        return None, None

    return meta, rest_content

def build_new_front_matter(meta):
    # 只保留需要的字段
    title = meta.get("title", "")
    if isinstance(title, str):
        title = title.strip(' "\'')
    date = meta.get("date", "")
    blurb = meta.get("blurb", "")
    if isinstance(blurb, str):
        blurb = blurb.strip(' "\'')
    og_image = meta.get("og_image", "")

    front = [
        "---",
        "layout: post",
        f'title: "{title}"',
        f"date: {date}",
        f'blurb: "{blurb}"',
        f"og_image: {og_image}",
        "---",
        "",
    ]
    return "\n".join(front)

def rename_posts():
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith(".md"):
            continue

        path = os.path.join(POSTS_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        meta, rest = extract_front_matter(lines)
        if meta is None or "date" not in meta or meta["date"] is None:
            print(f"Skipped (no valid date): {filename}")
            continue

        # 确认日期格式有效
        try:
            # 允许日期后带时间
            date_obj = datetime.datetime.strptime(str(meta["date"]), "%Y-%m-%d %H:%M:%S")
        except ValueError:
            try:
                # 只日期格式
                date_obj = datetime.datetime.strptime(str(meta["date"]), "%Y-%m-%d")
            except ValueError:
                print(f"Skipped (invalid date format): {filename}")
                continue

        title = meta.get("title", "")
        if not title:
            print(f"Skipped (no title): {filename}")
            continue
        if isinstance(title, str):
            title = title.strip(' "\'')

        slug = slugify(title)
        new_filename = f"{date_obj.strftime('%Y-%m-%d')}-{slug}.md"
        new_path = os.path.join(POSTS_DIR, new_filename)

        if new_path == path:
            print(f"Already named correctly: {filename}")
            continue
        if os.path.exists(new_path):
            print(f"Skipped (target exists): {new_filename}")
            continue

        # 生成新的 front matter 和内容
        new_front = build_new_front_matter(meta)
        new_content = new_front + rest

        # 写回文件
        with open(new_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        # 删除旧文件
        os.remove(path)
        print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":
    rename_posts()
