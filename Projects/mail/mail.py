import smtplib
from email.mime.text import MIMEText

recvEmail = "kmx1995@naver.com" # 받을 이메일
sendEmail = "kmx1995@naver.com" # 보낼 이메일
password = "wngh0621*" # 비밀번호
# password = "**********" # 비밀번호

smtpName = "smtp.naver.com" #smtp 서버 주소(네이버)
# smtpName = "smtp.gmail.com" #smtp 서버 주소(구글)
smtpPort = 587 #smtp 포트 번호

text = "똥이나 드셔" # 보낼 본문 내용
msg = MIMEText(text) 

msg['Subject'] ="받어라!" #메일 제목
msg['From'] = sendEmail 
msg['To'] = recvEmail
print(msg.as_string())

s=smtplib.SMTP( smtpName , smtpPort ) #메일 서버 연결
s.starttls() #TLS 보안 처리
s.login( sendEmail , password ) #로그인
s.sendmail( sendEmail, recvEmail, msg.as_string() ) #메일 전송, 문자열로 변환하여 보냅니다.
s.close() #smtp 서버 연결을 종료합니다.