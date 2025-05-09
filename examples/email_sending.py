import smtplib
from email.mime.text import MIMEText


mail_address = 'l2sh.timetable@yandex.ru'
mail_login = 'l2sh.timetable'
mail_password = ''
mail_to = ''


smtpObj = smtplib.SMTP('smtp.yandex.ru', 587)
smtpObj.starttls()
smtpObj.login(mail_login, mail_password)

mail_theme = 'Верификация'
mess = MIMEText(f'<h3>Никому не сообщайте! Ваш код подтверждения:</h3> '
                f'<h2>7777</h2> '
                f'<h4>Если Вы не запрашивали код подтверждения, ПРОИГНОРИРУЙТЕ это письмо!</h4>',
                'html')
mess['From'] = mail_address
mess['To'] = mail_to
mess['Subject'] = mail_theme
smtpObj.sendmail(mail_address, mail_to, mess.as_string())
smtpObj.quit()
