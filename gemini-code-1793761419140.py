import random
import string

def generate_password(length=12):
    # รวมตัวอักษรพิมพ์เล็ก พิมพ์ใหญ่ ตัวเลข และอักขระพิเศษ
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # สุ่มเลือกตัวอักษรตามความยาวที่กำหนด
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("=== 🔐 โปรแกรมสร้างรหัสผ่านปลอดภัย ===")
    try:
        length_input = input("กรอกความยาวรหัสผ่านที่ต้องการ (ค่าเริ่มต้น 12): ")
        length = int(length_input) if length_input.strip() else 12
        
        if length < 4:
            print("⚠️ แนะนำให้ความยาวอย่างน้อย 4 ตัวอักษรขึ้นไปนะ!")
        else:
            pwd = generate_password(length)
            print(f"✨ รหัสผ่านที่คุณได้คือ: {pwd}")
            
    except ValueError:
        print("❌ กรุณากรอกเป็นตัวเลขเท่านั้น!")