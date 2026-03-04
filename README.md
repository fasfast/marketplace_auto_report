# Marketplace Auto Report Generator

Automation tool untuk menggabungkan banyak file CSV laporan marketplace dan menghasilkan summary omzet otomatis.

## Features
- Detect multiple CSV files dalam folder
- Merge otomatis
- Convert kolom tanggal ke datetime
- Group berdasarkan tanggal
- Hitung total omzet per hari
- Export hasil ke Excel (summary_report.xlsx)

## How It Works
1. Letakkan semua file CSV ke dalam folder `data`
2. Jalankan:
   python main.py
3. File summary_report.xlsx akan otomatis dibuat

## Tech Stack
- Python
- Pandas
- OS module

## Purpose
Tool ini dibuat untuk membantu UMKM atau admin marketplace menghemat waktu dalam proses rekap laporan penjualan harian.

crated by : fasfast
