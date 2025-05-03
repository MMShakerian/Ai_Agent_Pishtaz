import sqlite3
import re
from openai import OpenAI

# ست کردن API Key


# اتصال به دیتابیس
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# گرفتن اسامی ستون‌ها از دیتابیس
def get_column_names():
    cursor.execute("PRAGMA table_info(barnameha);")
    columns = [row[1] for row in cursor.fetchall()]
    return columns

# استخراج SQL از پاسخ مدل
def extract_sql_from_response(text):
    match = re.search(r"```sql\s*(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return text.strip()

# تولید کوئری SQL از سوال کاربر
def generate_sql_query(user_question):
    column_names = get_column_names()
    column_list = ", ".join(column_names)

    prompt = f"""
شما یک مدل تبدیل متن به SQL هستید.
کاربر سوال زیر را پرسیده است. لطفاً فقط و فقط کوئری SQL مربوطه را تولید کنید که روی جدولی به نام barnameha اجرا شود.

سوال: \"{user_question}\"

قوانین:
- فقط SQL بنویس، هیچ توضیحی اضافه نکن.
- نام جدول \"barnameha\" است.
- نام ستون‌ها دقیقاً یکی از موارد زیر است:
{column_list}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "شما یک مدل تبدیل سوال به SQL هستید."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    raw_sql = response.choices[0].message.content.strip()
    clean_sql = extract_sql_from_response(raw_sql)
    return clean_sql

# اجرای کوئری روی دیتابیس
def execute_sql(sql_query):
    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        return f"خطا در اجرای کوئری: {e}"

# اجرای برنامه
if __name__ == "__main__":
    while True:
        user_question = input("❓ سوال خود را وارد کنید (یا 'exit' برای خروج): ")
        if user_question.lower() == 'exit':
            break

        sql_query = generate_sql_query(user_question)
        print(f"\n🛠 کوئری تولید شده:\n{sql_query}\n")

        results = execute_sql(sql_query)
        print(f"📋 نتایج:\n{results}\n")
