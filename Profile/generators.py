import random
import string
from Profile.models import OTPDevice

class OTPGenerator:
    @staticmethod
    def generate_otp():
        return ''.join(random.choices(string.digits, k=6))

    @staticmethod
    def generate_unique_otp():
        otp = OTPGenerator.generate_otp()
        while OTPDevice.objects.filter(otp=otp).exists():
            otp = OTPGenerator.generate_otp()
        return otp