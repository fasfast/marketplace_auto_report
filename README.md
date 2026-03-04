# 🗂️ Marketplace Auto Report Generator

> **Upload banyak file CSV dari platform manapun — Shopee, Tokopedia, Lazada, TikTok Shop — digabung otomatis dan langsung bisa download summary Excel.**

🔗 **[➡️ Coba Langsung (Live Demo)](https://marketplace-auto-report.streamlit.app)**

---

## 🎯 Cocok untuk Siapa?

- Admin toko yang kelola **lebih dari 1 platform** sekaligus
- UMKM yang capek copy-paste laporan tiap hari
- Pemilik toko yang ingin **summary omzet harian otomatis**

---

## ✨ Fitur Unggulan

| Fitur | Keterangan |
|---|---|
| 📂 Upload Multi-File | Upload banyak CSV sekaligus dari platform berbeda |
| 🔍 Auto-Deteksi Platform | Nama file `shopee.csv` otomatis terbaca sebagai Shopee |
| 📈 Grafik Omzet Harian | Tren penjualan semua platform dalam 1 grafik |
| 🏪 Perbandingan Platform | Lihat platform mana yang paling menghasilkan |
| 🏆 Top 5 Produk Terlaris | Produk terlaku dari semua platform |
| 📊 Hari Terbaik & Platform Terkuat | Insight otomatis tanpa perlu hitung manual |
| 💾 Export Excel Lengkap | Summary siap kirim ke bos atau akuntan |
| 📥 Contoh File CSV | Tersedia file demo untuk langsung dicoba |

---

## 🖼️ Tampilan Dashboard

> *(Screenshot menyusul setelah deploy)*

---

## 🚀 Cara Pakai

1. Buka **[Live Demo](https://marketplace-auto-report.streamlit.app)**
2. Download contoh file CSV dari sidebar *(opsional)*
3. Upload semua file CSV laporan marketplace sekaligus
4. Dashboard otomatis terbentuk 🎉
5. Klik **Download Summary Excel** untuk simpan hasil

---

## 📋 Format File CSV

File CSV harus punya kolom berikut:

```
tanggal, produk, qty, harga, total
2024-01-01, Kaos Polos, 2, 85000, 170000
```

**Kolom wajib:** `tanggal`, `total`
**Kolom opsional:** `produk`, `qty`, `harga`

> **Tips penamaan file:** Beri nama file sesuai platform agar otomatis terdeteksi.
> Contoh: `shopee_januari.csv`, `tokopedia_jan.csv`, `lazada.csv`

---

## 🏪 Platform yang Didukung

- 🟠 Shopee
- 🟢 Tokopedia
- 🔵 Lazada
- 🎵 TikTok Shop
- ✅ Platform lain *(nama platform diambil dari nama file)*

---

## 🛠️ Tech Stack

- **Python** — bahasa pemrograman utama
- **Streamlit** — framework web app
- **Pandas** — pengolahan & penggabungan data
- **XlsxWriter** — export ke Excel

---

## 💬 Butuh Custom Fitur?

Butuh fitur tambahan seperti:
- ➕ Laporan laba rugi & HPP
- ➕ Filter tanggal & produk
- ➕ Notifikasi WhatsApp otomatis
- ➕ Integrasi langsung API Shopee/Tokopedia
- ➕ Dashboard khusus bisnis kamu

**Hubungi saya:**
- 📱 WhatsApp: [+62 xxx-xxxx-xxxx](https://wa.me/62xxxxxxxxxx)
- 📧 Email: fasfast@proton.me
- 🐙 GitHub: [@fasfast](https://github.com/fasfast)

---

## 📄 Lisensi

Project ini open source untuk keperluan belajar.
Untuk penggunaan komersial, silakan hubungi pembuat.

---

<div align="center">
  Dibuat dengan ❤️ oleh <b><a href="https://github.com/fasfast">Fasfast</a></b>
</div>
