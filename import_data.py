
import sqlite3

# اتصال به دیتابیس
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# ایجاد جدول
cursor.execute('''
CREATE TABLE IF NOT EXISTS barnameha (
    shomare_barname TEXT,
    tarikh TEXT,
    mabda TEXT,
    maghsad TEXT,
    baregir TEXT,
    noe_sanad_haml TEXT,
    noe_bar TEXT,
    melli_ranande TEXT,
    name_ranande TEXT,
    phone_ranande TEXT,
    ferestande_bar TEXT,
    phone_ferestande TEXT,
    noe_barname TEXT,
    komision_pishtaz REAL,
    safi_ranande REAL,
    paye_barname REAL,
    bimeh_bar REAL,
    taraf_pardakht TEXT,
    vaziat_vosool_ranande TEXT,
    vaziat_vosool_saheb_bar TEXT,
    kol_barname REAL,
    yaddasht TEXT,
    sahm_rahdari REAL,
    sahm_bimeh_takmili REAL,
    daramad_vaghei_pishtaz REAL,
    maliat REAL,
    bedehi_ranande REAL,
    talab_ranande REAL,
    bedehi_saheb_bar REAL,
    vaziat_field TEXT,
    zaman_sabt TEXT,
    zaman_taghir TEXT,
    shomare_sanad_ranande TEXT,
    shomare_sanad_saheb_bar TEXT,
    search_column TEXT
);
''')

# ذخیره تغییرات
conn.commit()
conn.close()

print("✅ جدول barnameha ساخته شد.")