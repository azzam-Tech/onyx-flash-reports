import math

def do_tafqeet(total_amount):
    try:
        from num2words import num2words
    except ImportError:
        return f"{total_amount} ريال سعودي"
        
    try:
        # Avoid floating point precision issues by rounding first
        total = round(float(total_amount), 2)
        riyal = int(total)
        halala = int(round((total - riyal) * 100))
        
        riyal_text = num2words(riyal, lang='ar')
        halala_text = num2words(halala, lang='ar')
        
        result = "فقط "
        if riyal > 0:
            result += f"{riyal_text} ريالاً سعودياً"
        
        if halala > 0:
            if riyal > 0:
                result += " و "
            result += f"{halala_text} هللة"
            
        result += " لا غير."
        return result
    except Exception as e:
        return f"{total_amount} ريال سعودي"
