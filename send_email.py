import requests
import re
def download_github_markdown(github_blob_url, save_path):
    # 将 blob 链接替换为 raw
    raw_url = github_blob_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    
    response = requests.get(raw_url)
    
    if response.status_code == 200:
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"✅ 文件已保存为 {save_path}")
    else:
        print(f"❌ 下载失败，状态码: {response.status_code}")

# 示例使用
url = "https://github.com/dw-dengwei/daily-arXiv-ai-enhanced/blob/main/data/2025-04-16.md"
save_file = "2025-04-16.md"

download_github_markdown(url, save_file)



import re

def filter_md_by_div_blocks(text, keep_keywords):
    # 找出所有 <div id=...></div>
    div_tags = re.findall(r"<div id=.*?></div>", text)
    parts = re.split(r"<div id=.*?></div>", text)

    # 安全检查：div_tags 的数量应比 parts 少 1（前面可能有 intro）
    assert len(parts) == len(div_tags) + 1 or len(parts) == len(div_tags)

    # 重组结构，并筛选
    filtered_blocks = []
    filtered_blocks.append(parts[0])

    for div_tag, content in zip(div_tags, parts[1:]):
        if any(keyword in content for keyword in keep_keywords):
            filtered_blocks.append(div_tag + content)

    return "\n".join(filtered_blocks)

with open(save_file, "r", encoding="utf-8") as f:
    md_text = f.read()

# 保留 cs.AI 和 cs.RO
keep_keywords = [f"cs.{flag} [[Back]](#toc)" for flag in ["CL","AI", "CV"]]
filtered_text = filter_md_by_div_blocks(md_text, keep_keywords)

# 保存
with open("filtered_output.md", "w", encoding="utf-8") as f:
    f.write(filtered_text)

print("✅ 处理完成，已保存为 filtered_output.md")

    
