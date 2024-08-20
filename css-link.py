import os
from bs4 import BeautifulSoup

def modify_link_href(file_path):
  """修改 HTML 文件中 link 标签的 href 属性值。

  Args:
    file_path: HTML 文件的路径。
  """
  for encoding in ['utf-8', 'gbk']:  # 尝试 utf-8 和 gbk 编码
    try:
      with open(file_path, 'r', encoding=encoding) as f:
        html_content = f.read()

      soup = BeautifulSoup(html_content, 'html.parser')

      # 找到所有 link 标签，并检查其 href 属性是否包含 "style.css"
      link_tags = soup.find_all('link', href=lambda href: href and "../css/style.css" in href)
      
      if link_tags:  # 找到匹配的 link 标签
        for link_tag in link_tags:
          link_tag['href'] = "../css/style.css"  # 修改 href 属性值

        # 将修改后的 HTML 写回到文件
        with open(file_path, 'w', encoding=encoding) as f:
          f.write(str(soup))

        print(f"文件: {file_path} - link href 修改成功")
      else:
        print(f"文件: {file_path} - 未找到需要修改的 link 标签")

      break  # 如果成功读取并修改，则跳出循环

    except UnicodeDecodeError:
      continue  # 如果解码失败，尝试下一个编码

def main():
  """修改 bugs 文件夹中 1000 个 HTML 文件中的 link href 属性值。"""
  folder_path = 'bugs'
  file_count = 0

  for filename in os.listdir(folder_path):
    if filename.endswith('.html'):
      file_path = os.path.join(folder_path, filename)
      modify_link_href(file_path)

      file_count += 1
      if file_count >= 1048:
        break

if __name__ == "__main__":
  main()
