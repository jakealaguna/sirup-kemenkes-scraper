# SiRUP Kementerian Kesehatan Scraper

Python automation untuk mengambil seluruh data paket pengadaan **Kementerian Kesehatan** dari website **SiRUP INAPROC** secara otomatis dan menyimpannya ke dalam format Microsoft Excel.

---

## Features

- Mengambil seluruh halaman secara otomatis
- Mendukung 100 data per halaman
- Menyimpan hasil ke Excel (.xlsx)
- Menggunakan Selenium WebDriver
- Mudah dijalankan di komputer lain

---

## Technology

- Python
- Selenium
- Pandas
- OpenPyXL
- WebDriver Manager

---

## Installation

Clone repository

```bash
git clone https://github.com/USERNAME/sirup-kemenkes-scraper.git
```

Masuk ke folder

```bash
cd sirup-kemenkes-scraper
```

Install library

```bash
python -m pip install -r requirements.txt
```

---

## Usage

Jalankan program

```bash
python ambil_kemenkes.py
```

Kemudian:

1. Pilih Tahun Anggaran
2. Pilih Kementerian Kesehatan
3. Klik Cari
4. Pilih 100 data per halaman
5. Tekan ENTER di PowerShell

Program akan mengambil seluruh data secara otomatis.

---

## Output

```
kemenkes_2026.xlsx
```

---

## Disclaimer

Repository ini dibuat untuk tujuan pembelajaran dan otomatisasi pengambilan data yang tersedia secara publik. Penggunaan tetap harus mematuhi ketentuan layanan dari website sumber.

---

## License

MIT License