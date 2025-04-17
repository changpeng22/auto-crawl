import smtplib
from email.message import EmailMessage
import markdown
import os
# 配置信息
smtp_server = "smtp.163.com"
smtp_port = 465
sender_email = os.getenv("EMAIL_USERNAME")
sender_password = os.getenv("EMAIL_PASSWORD")
receiver_email = os.getenv("TO_EMAIL")

# 读取 Markdown 文件
md_file_path = "README.md"
with open(md_file_path, "r", encoding="utf-8") as f:
    md_content = f.read()

# 将 Markdown 转为 HTML
html_content = markdown.markdown(md_content)

# 构建邮件
msg = EmailMessage()
msg['Subject'] = '📄 Markdown 邮件正文示例'
msg['From'] = sender_email
msg['To'] = receiver_email

# 设置纯文本备用内容（可选）
msg.set_content("这是 Markdown 内容的 HTML 渲染版本，请使用支持 HTML 的客户端查看。")

# 设置 HTML 正文
msg.add_alternative(html_content, subtype='html')

# 发送邮件
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(msg)

print("✅ 邮件已发送（HTML 来自 Markdown）")
