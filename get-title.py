import os
from bs4 import BeautifulSoup

def extract_title_from_html(file_path):
  """从 HTML 文件中提取标题，并去除 "| WooYun.org"。

  Args:
    file_path: HTML 文件的路径。

  Returns:
    处理后的 HTML 文件标题，如果找不到标题则返回 None。
  """
  for encoding in ['utf-8', 'gbk']:  # 尝试 utf-8 和 gbk 编码
    try:
      with open(file_path, 'r', encoding=encoding) as f:
        html_content = f.read()
      soup = BeautifulSoup(html_content, 'html.parser')
      title = soup.find('title')
      if title:
        title_text = title.text.strip()
        title_text = title_text.replace(" | WooYun.org", "")
        return title_text
    except UnicodeDecodeError:
      continue  # 如果解码失败，尝试下一个编码
  return None  # 如果所有编码都失败，返回 None

def main():
  """读取 bugs 文件夹内的 100 个 HTML 文件，提取标题并保存到 res.txt。"""
  folder_path = 'bugs'
  file_count = 0

  with open('res.txt', 'w', encoding='utf-8') as f: 
    for filename in os.listdir(folder_path):
      if filename.endswith('.html'):
        file_path = os.path.join(folder_path, filename)
        title = extract_title_from_html(file_path)
        f.write(f"序号: {file_count}, 文件: {filename}, 标题: {title}\n")  # 写入到 res.txt

        file_count += 1
        if file_count >= 1048:
          break

if __name__ == "__main__":
  main()
