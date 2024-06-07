import os
import requests
from django.conf import settings

def send_otp_email(to_email, otp):
    print(f'{settings.EMAIL_HOST_USER}  {settings.EMAIL_PASSWORD}')
    return requests.post(
        f"https://api.mailgun.net/v3/{os.getenv('EMAIL_HOST_USER')}/messages",
        auth=("api", os.getenv('EMAIL_PASSWORD')),
        data={
            "from": f"YourApp <mailgun@{os.getenv('EMAIL_HOST_USER')}>",
            "to": [to_email],
            "subject": "Your OTP Code",
            "text": f"Your OTP code is {otp}"
        }
    )
