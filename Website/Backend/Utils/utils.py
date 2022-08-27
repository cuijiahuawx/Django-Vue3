from django.core.mail import EmailMessage
import random
import string

def send_email(data):
    email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
    print(f"{data['email_subject']}已发送")
    email.send()

def gen_code():
    # string.ascii_letters,所有大写+小写字母
    # string.ascii_lowercase,所有小写字母
    # string.ascii_uppercase,所有大写字母
    # string.digital,10个数字
    code1 = string.ascii_letters
    code2 = string.ascii_lowercase
    code3 = code1 + code2
    # random.sample随机取值,取4个
    code4 = random.sample(code3,4)
    # 连接输出
    code = ''.join(code4)
    return code
