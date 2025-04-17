import requests
import re
import smtplib
import os
from email.message import EmailMessage

def download_github_markdown(github_blob_url):
    raw_url = github_blob_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    
    response = requests.get(raw_url)

    content = " "
    if response.status_code == 200:
        with open(save_path, "w", encoding="utf-8") as f:
            content = response.text
        print(f"✅ 文件已保存为 {save_path}")
    else:
        print(f"❌ 下载失败，状态码: {response.status_code}")
    return content

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

def send_markdown_email(
    smtp_server, smtp_port,
    sender_email, sender_password,
    receiver_email,
    subject
):
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    # 添加内容
    msg.set_content(filtered_text)

    # 发送邮件
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

    print(f"✅ 邮件已发送")
    
url = f"https://github.com/dw-dengwei/daily-arXiv-ai-enhanced/blob/main/data/{datetime.now().strftime("%Y-%m-%d")}.md"
content = download_github_markdown(url)

# 保留
keep_keywords = [f"cs.{flag} [[Back]](#toc)" for flag in ["CL","AI", "CV"]]
filtered_text = filter_md_by_div_blocks(content, keep_keywords)
print("✅ md文件处理完成")

send_markdown_email(
    smtp_server="smtp.163.com",          
    smtp_port=465,
    sender_email=os.getenv("SEND_EMAIL"),
    sender_password=os.getenv("SEND_EMAIL_ENTROPY"),
    receiver_email=os.getenv("RECEIVE_EMAIL"),
    subject="每日 arXiv 摘要",
)

    
