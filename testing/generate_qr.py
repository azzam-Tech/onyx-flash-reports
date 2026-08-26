import base64
import binascii
import qrcode
import os
from datetime import datetime

def generate_tlv(tag, value):
    # Convert string value to bytes (UTF-8 encoding is required by ZATCA)
    if isinstance(value, str):
        value_bytes = value.encode('utf-8')
    else:
        value_bytes = value
        
    tag_byte = bytes([tag])
    length_byte = bytes([len(value_bytes)])
    return tag_byte + length_byte + value_bytes

def generate_zatca_qr(seller_name, vat_number, timestamp, total_amount, vat_amount, output_path):
    # 1. Seller Name
    tlv1 = generate_tlv(1, seller_name)
    # 2. VAT Registration Number
    tlv2 = generate_tlv(2, vat_number)
    # 3. Timestamp (ISO 8601 format)
    tlv3 = generate_tlv(3, timestamp)
    # 4. Invoice Total (with VAT)
    tlv4 = generate_tlv(4, str(total_amount))
    # 5. VAT Total
    tlv5 = generate_tlv(5, str(vat_amount))
    
    # Concatenate all TLVs
    full_tlv = tlv1 + tlv2 + tlv3 + tlv4 + tlv5
    
    # Convert to Base64
    qr_base64 = base64.b64encode(full_tlv).decode('utf-8')
    
    # Generate QR Code Image
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_base64)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    
    return qr_base64

if __name__ == "__main__":
    # Example Data for generating a valid ZATCA QR code
    seller_name = "مؤسسة عاصمة المجد للتجارة - سرين"
    vat_number = "302145687600003"
    timestamp = "2026-08-08T18:09:00Z"
    total_amount = "13225.00"
    vat_amount = "1725.00"
    
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'Results')
    output_path = os.path.join(output_dir, "Zatca_Sample_QR.png")
    
    base64_str = generate_zatca_qr(seller_name, vat_number, timestamp, total_amount, vat_amount, output_path)
    
    print(f"QR Code Base64 Data:\n{base64_str}\n")
    print(f"QR Code image saved to: {output_path}")
