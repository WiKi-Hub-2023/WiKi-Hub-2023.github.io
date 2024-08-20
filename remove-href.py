import os
import re
from bs4 import BeautifulSoup

def remove_a_href(file_path):
  """将 HTML 文件中所有 a 标签的 href 属性值设置为空字符串。

  Args:
    file_path: HTML 文件的路径。
  """
  for encoding in ['utf-8', 'gbk']:
    try:
      with open(file_path, 'r', encoding=encoding) as f:
        html_content = f.read()

        # 使用正则表达式删除目标标签及其内容
        # html_content = re.sub(r'https://static.wooyun.org', '', html_content, flags=re.DOTALL)
        # html_content = re.sub(r'<div class="wxewm">.*?</div>', '', html_content, flags=re.DOTALL)
        # 使用正则表达式替换目标链接
        new_link = '<li><a href="../index.html" style="color:red;font-size:35px;">返回漏洞列表页</a></li>'
        html_content = re.sub(r'<li><a href="http://wooyun.org/notice/">公告</a></li>', new_link, html_content, flags=re.DOTALL)


        # 将修改后的 HTML 写回到文件
        with open(file_path, 'w', encoding=encoding) as f:
          f.write(html_content)

        print(f"文件: {file_path} - li已替换")


      break  # 如果成功读取并修改，则跳出循环

    except UnicodeDecodeError:
      continue  # 如果解码失败，尝试下一个编码

def main():
  """将 bugs 文件夹中所有 HTML 文件中 a 标签的 href 属性值设置为空字符串。"""
  folder_path = 'bugs'

  # 获取文件夹内所有 HTML 文件的列表
  html_files = [f for f in os.listdir(folder_path) if f.endswith('.html')]

  # 处理所有 HTML 文件
  for filename in html_files:
    file_path = os.path.join(folder_path, filename)
    remove_a_href(file_path)

if __name__ == "__main__":
  main()
