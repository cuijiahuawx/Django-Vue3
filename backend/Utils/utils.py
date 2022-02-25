from django.core.mail import EmailMessage

def send_email(data):
    email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
    print(f"{data['email_subject']}已发送")
    email.send()
