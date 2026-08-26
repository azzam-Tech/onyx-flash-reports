import cv2
import sys
import base64
from pyzbar.pyzbar import decode

# Need to ensure pyzbar is installed or cv2 has QRCodeDetector
# Using cv2.QRCodeDetector first as it is standard in opencv
img_path = r"C:\Users\amarn\.gemini\antigravity-ide\brain\e688e573-846d-4e87-b775-315f1ae440a1\.user_uploaded\media_1787468779150.png"
img = cv2.imread(img_path)

if img is None:
    print("Could not read image.")
    sys.exit()

detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img)

if not data:
    # Try pyzbar if cv2 fails
    try:
        from pyzbar.pyzbar import decode
        decoded_objs = decode(img)
        if decoded_objs:
            data = decoded_objs[0].data.decode('utf-8')
    except Exception as e:
        print(f"pyzbar error: {e}")

if not data:
    print("No QR code detected.")
    sys.exit()

print(f"Raw QR Data: {data}\n")

# ZATCA QR is base64 encoded TLV
try:
    decoded_bytes = base64.b64decode(data)
    i = 0
    tags = {1: 'Seller Name', 2: 'VAT Registration', 3: 'Timestamp', 4: 'Total Amount', 5: 'VAT Amount', 6: 'Hash', 7: 'ECDSA Signature', 8: 'Public Key', 9: 'Certificate Signature'}
    
    print("--- ZATCA QR TLV Parsed Data ---")
    while i < len(decoded_bytes):
        tag = decoded_bytes[i]
        length = decoded_bytes[i+1]
        value = decoded_bytes[i+2 : i+2+length]
        
        tag_name = tags.get(tag, f"Tag {tag}")
        
        # Hex representation for Hash/Signatures, string for others
        if tag in (6, 7, 8, 9):
            val_str = base64.b64encode(value).decode('utf-8')
        else:
            try:
                val_str = value.decode('utf-8')
            except:
                val_str = value.hex()
                
        print(f"{tag_name}: {val_str}")
        
        i += 2 + length
except Exception as e:
    print(f"Failed to parse as ZATCA Base64 TLV: {e}")
