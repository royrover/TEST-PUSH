from datetime import datetime
import os

# ชื่อไฟล์
OUTPUT_FILE = "output.txt"

# แสดงโฟลเดอร์ปัจจุบัน (debug)
print("Current working directory:", os.getcwd())

# สร้างเนื้อหาไฟล์
content = f"อัปเดตล่าสุด: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

# เขียนไฟล์
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ เขียนไฟล์ {OUTPUT_FILE} สำเร็จ")
