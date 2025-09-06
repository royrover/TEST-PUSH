from datetime import datetime

OUTPUT_FILE = "output.txt"
content = f"อัปเดตล่าสุด: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ เขียนไฟล์ {OUTPUT_FILE} สำเร็จ")
