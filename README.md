# SiRUP Kementerian Kesehatan Scraper

Python-based automation tool for collecting public procurement package data from the SiRUP INAPROC website and exporting the results to Microsoft Excel.

## Features

- Automated extraction of procurement package data
- Supports pagination (100 records per page)
- Exports data to Excel (.xlsx)
- Built with Selenium WebDriver
- Easy to run on different computers

## Technologies

- Python
- Selenium
- Pandas
- OpenPyXL
- WebDriver Manager

## Installation

Clone this repository:

```bash
git clone https://github.com/jakealaguna/sirup-kemenkes-scraper.git
```

Move into the project directory:

```bash
cd sirup-kemenkes-scraper
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the scraper:

```bash
python ambil_kemenkes.py
```

Then:

1. Select the fiscal year.
2. Select **Kementerian Kesehatan**.
3. Click **Cari**.
4. Set the table to display **100 rows per page**.
5. Press **ENTER** in PowerShell.

The program will automatically scrape all available pages and save the result as:

```text
kemenkes_2026.xlsx
```

## Disclaimer

This project is intended for educational purposes and automation of publicly available data. Users are responsible for ensuring compliance with the terms of use of the source website.

## License

MIT License
