from datetime import datetime
from .models import OTPDevice

class OTPHandler:
    @staticmethod
    def validate_otp(otp, stored_otp):
        return otp == stored_otp

    @staticmethod
    def get_otp(user):
        otp_device = OTPDevice.objects.filter(user=user, expires_at__gte=datetime.now()).last()
        if otp_device:
            return otp_device.otp
        return None