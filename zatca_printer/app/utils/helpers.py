import time
import base64
from functools import wraps

def timed_cache(seconds: int):
    def decorator(func):
        cache = {}
        @wraps(func)
        def wrapper(*args, **kwargs):
            force_refresh = kwargs.pop('force_refresh', False)
            key = str(args) + str(kwargs)
            now = time.time()
            
            if not force_refresh and key in cache:
                result, timestamp = cache[key]
                if now - timestamp < seconds:
                    return result
                    
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        return wrapper
    return decorator

def decrypt_onyx_password(encrypted_pwd):
    if not encrypted_pwd: return ""
    L = len(encrypted_pwd)
    return "".join(chr(ord(c) - L) for c in encrypted_pwd)

def encrypt_onyx_password(plain_pwd):
    if not plain_pwd: return ""
    L = len(plain_pwd)
    return "".join(chr(ord(c) + L) for c in plain_pwd)

def generate_tlv(tag, value):
    if isinstance(value, str):
        value_bytes = value.encode('utf-8')
    else:
        value_bytes = value
    return bytes([tag, len(value_bytes)]) + value_bytes

def generate_zatca_qr_base64(seller_name, vat_number, timestamp, total_amount, vat_amount):
    tlv1 = generate_tlv(1, seller_name)
    tlv2 = generate_tlv(2, vat_number)
    tlv3 = generate_tlv(3, timestamp)
    tlv4 = generate_tlv(4, str(total_amount))
    tlv5 = generate_tlv(5, str(vat_amount))
    full_tlv = tlv1 + tlv2 + tlv3 + tlv4 + tlv5
    return base64.b64encode(full_tlv).decode('utf-8')
