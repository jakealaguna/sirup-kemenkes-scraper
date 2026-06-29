from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20)

driver.maximize_window()
driver.get("https://sirup.inaproc.id/sirup/caripaketctr/index")

print("""
=========================================

PILIH MANUAL

1. Tahun 2026
2. Kementerian Kesehatan
3. Klik Cari
4. Ubah jumlah baris menjadi 100

Setelah tabel muncul tekan ENTER.

=========================================
""")

input()

wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody tr"))
)

hasil = []

halaman = 1

while True:

    print(f"\nMengambil halaman {halaman}")

    rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

    for row in rows:

        cols = row.find_elements(By.TAG_NAME, "td")

        if len(cols) < 12:
            continue

        hasil.append({
            "No": cols[0].text,
            "Paket": cols[1].text,
            "Pagu": cols[2].text,
            "Jenis Pengadaan": cols[3].text,
            "PDN": cols[4].text,
            "UMK": cols[5].text,
            "Metode": cols[6].text,
            "Pemilihan": cols[7].text,
            "K/L": cols[8].text,
            "Satker": cols[9].text,
            "Lokasi": cols[10].text,
            "ID": cols[11].text,
        })

    print("Total data :", len(hasil))

    try:

        next_btn = driver.find_element(
            By.XPATH,
            "//a[contains(.,'Selanjutnya')]"
        )

        parent = next_btn.find_element(By.XPATH, "..")

        if "disabled" in parent.get_attribute("class"):
            break

        driver.execute_script("arguments[0].click();", next_btn)

        halaman += 1

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody tr"))
        )

    except Exception as e:
        print(e)
        break

df = pd.DataFrame(hasil)

df.to_excel("kemenkes_2026.xlsx", index=False)

print("\n===================================")
print("SELESAI")
print("Jumlah data :", len(df))
print("File : kemenkes_2026.xlsx")
print("===================================")

driver.quit()