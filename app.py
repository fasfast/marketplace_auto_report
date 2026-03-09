import streamlit as st
import pandas as pd
import io
from datetime import datetime, timedelta
import random

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Auto Report Generator | Marketplace",
    page_icon="🗂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
    .stApp { background-color: #f0f4f8; }

    .hero {
        background: linear-gradient(135deg, #064e3b 0%, #059669 60%, #34d399 100%);
        border-radius: 20px;
        padding: 28px 32px;
        color: white;
        margin-bottom: 28px;
        box-shadow: 0 8px 32px rgba(5,150,105,0.28);
    }
    .hero h1 { font-size: 22px; font-weight: 800; margin-bottom: 6px; }
    .hero p  { font-size: 13px; opacity: 0.85; }

    .metric-card {
        background: white;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06), 0 4px 12px rgba(0,0,0,0.04);
        border-left: 4px solid;
        margin-bottom: 8px;
    }
    .metric-card.green  { border-color: #10b981; }
    .metric-card.blue   { border-color: #3b82f6; }
    .metric-card.orange { border-color: #f59e0b; }
    .metric-card.purple { border-color: #8b5cf6; }
    .metric-label { font-size: 11px; font-weight: 700; color: #6b7280; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px; }
    .metric-value { font-size: 22px; font-weight: 800; color: #111827; }
    .metric-sub   { font-size: 11px; color: #9ca3af; margin-top: 4px; }

    .section-title { font-size: 15px; font-weight: 700; color: #111827; margin: 20px 0 12px 0; }
    .info-box { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 12px; padding: 14px 18px; font-size: 13px; color: #166534; margin-bottom: 16px; }

    .stDownloadButton > button {
        background: linear-gradient(135deg, #059669, #047857) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 10px 24px !important;
        font-weight: 700 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 14px !important;
        width: 100% !important;
        box-shadow: 0 4px 12px rgba(5,150,105,0.3) !important;
    }

    div[data-testid="stSidebar"] { background: white; border-right: 1px solid #e5e7eb; }
    .contact-box { background: linear-gradient(135deg, #f0fdf4, #dcfce7); border: 1px solid #86efac; border-radius: 12px; padding: 14px; margin-top: 16px; font-size: 12px; color: #166534; }
    hr { border: none; border-top: 1px solid #e5e7eb; margin: 20px 0; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# SAMPLE DATA GENERATOR
# ─────────────────────────────────────────────
def generate_sample_csv(platform: str) -> bytes:
    random.seed(10 if platform == "shopee" else 20 if platform == "tokopedia" else 30)
    base = datetime.today() - timedelta(days=14)
    products = ["Kaos Polos", "Celana Jeans", "Jaket Hoodie", "Sepatu Sneakers", "Tas Ransel"]
    rows = []
    for i in range(14):
        for _ in range(random.randint(2, 6)):
            rows.append({
                "tanggal": (base + timedelta(days=i)).strftime("%Y-%m-%d"),
                "produk": random.choice(products),
                "qty": random.randint(1, 5),
                "harga": random.choice([85000, 120000, 180000, 250000, 95000]),
                "total": 0
            })
    df = pd.DataFrame(rows)
    df["total"] = df["qty"] * df["harga"]
    return df.to_csv(index=False).encode("utf-8")


# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🗂️ Auto Report Generator")
    st.markdown("---")
    st.markdown("**📁 Format CSV yang didukung:**")
    st.markdown("""
    - `tanggal` → format YYYY-MM-DD
    - `produk` → nama produk *(opsional)*
    - `qty` → jumlah terjual *(opsional)*
    - `total` → total pendapatan **(wajib)**
    """)
    st.markdown("---")
    st.markdown("**📥 Download Contoh File CSV**")
    for platform in ["shopee", "tokopedia", "lazada"]:
        st.download_button(
            f"📄 contoh_{platform}.csv",
            data=generate_sample_csv(platform),
            file_name=f"contoh_{platform}.csv",
            mime="text/csv"
        )
    st.markdown("""
    <div class="contact-box">
        <b>💬 Butuh bantuan?</b><br>
        Setup & custom fitur tersedia.<br><br>
        📱 <b>WA:</b> +62 85923746251<br>
        📧 <b>Email:</b> fasfast@email.com
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>🗂️ Marketplace Auto Report Generator</h1>
    <p>Upload banyak file CSV sekaligus dari platform manapun · Gabung otomatis · Export summary Excel dalam 1 klik</p>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# UPLOAD — MULTI FILE
# ─────────────────────────────────────────────
st.markdown('<div class="section-title">📂 Upload File CSV (bisa lebih dari 1)</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
    💡 Upload sekaligus semua file CSV dari Shopee, Tokopedia, Lazada, TikTok Shop, dll.
    Semua akan digabung otomatis. Download contoh file dari sidebar untuk coba demo.
</div>
""", unsafe_allow_html=True)

uploaded_files = st.file_uploader(
    "Upload semua file CSV laporan marketplace",
    type=["csv"],
    accept_multiple_files=True,
    help="Pilih beberapa file sekaligus dengan Ctrl+Click"
)


# ─────────────────────────────────────────────
# PROSES DATA
# ─────────────────────────────────────────────
if uploaded_files:
    try:
        all_dfs = []
        file_info = []

        for f in uploaded_files:
            df = pd.read_csv(f)
            if "total" not in df.columns:
                st.error(f"❌ File '{f.name}' tidak punya kolom 'total'. Skip.")
                continue
            # Deteksi nama platform dari nama file
            name_lower = f.name.lower()
            if "shopee" in name_lower:
                platform = "Shopee"
            elif "tokopedia" in name_lower or "tokped" in name_lower:
                platform = "Tokopedia"
            elif "lazada" in name_lower:
                platform = "Lazada"
            elif "tiktok" in name_lower:
                platform = "TikTok Shop"
            else:
                platform = f.name.replace(".csv", "").capitalize()

            df["platform"] = platform
            df["tanggal"]  = pd.to_datetime(df["tanggal"], errors="coerce")
            df["total"]    = pd.to_numeric(df["total"], errors="coerce").fillna(0)
            all_dfs.append(df)
            file_info.append({"File": f.name, "Platform": platform, "Baris": len(df), "Total": f"Rp {df['total'].sum():,.0f}"})

        if not all_dfs:
            st.error("❌ Tidak ada file valid yang bisa diproses.")
            st.stop()

        data = pd.concat(all_dfs, ignore_index=True)
        data = data.dropna(subset=["tanggal"])

        # SUMMARY
        harian_total   = data.groupby("tanggal")["total"].sum().reset_index()
        platform_total = data.groupby("platform")["total"].sum().reset_index()
        total_omzet    = data["total"].sum()
        total_transaksi = len(data)
        hari_terbaik   = harian_total.loc[harian_total["total"].idxmax()]
        rata_harian    = harian_total["total"].mean()

        # ── FILE INFO ─────────────────────────────
        st.markdown('<div class="section-title">📋 File yang Diproses</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame(file_info), use_container_width=True, hide_index=True)

        # ── METRICS ──────────────────────────────
        st.markdown('<div class="section-title">📈 Ringkasan Performa</div>', unsafe_allow_html=True)
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown(f"""<div class="metric-card green">
                <div class="metric-label">Total Omzet</div>
                <div class="metric-value">Rp {total_omzet:,.0f}</div>
                <div class="metric-sub">{len(uploaded_files)} file · {total_transaksi} transaksi</div>
            </div>""", unsafe_allow_html=True)
        with m2:
            st.markdown(f"""<div class="metric-card blue">
                <div class="metric-label">Rata-rata Harian</div>
                <div class="metric-value">Rp {rata_harian:,.0f}</div>
                <div class="metric-sub">{len(harian_total)} hari data</div>
            </div>""", unsafe_allow_html=True)
        with m3:
            st.markdown(f"""<div class="metric-card orange">
                <div class="metric-label">Hari Terbaik</div>
                <div class="metric-value">Rp {hari_terbaik['total']:,.0f}</div>
                <div class="metric-sub">{hari_terbaik['tanggal'].strftime('%d %b %Y')}</div>
            </div>""", unsafe_allow_html=True)
        with m4:
            top_platform = platform_total.loc[platform_total["total"].idxmax(), "platform"]
            top_omzet    = platform_total["total"].max()
            st.markdown(f"""<div class="metric-card purple">
                <div class="metric-label">Platform Terkuat</div>
                <div class="metric-value">{top_platform}</div>
                <div class="metric-sub">Rp {top_omzet:,.0f}</div>
            </div>""", unsafe_allow_html=True)

        # ── CHARTS ───────────────────────────────
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown('<div class="section-title">📉 Grafik Omzet Harian</div>', unsafe_allow_html=True)
            st.line_chart(harian_total.set_index("tanggal"), use_container_width=True, height=250)
        with col2:
            st.markdown('<div class="section-title">🏪 Omzet Per Platform</div>', unsafe_allow_html=True)
            st.bar_chart(platform_total.set_index("platform"), use_container_width=True, height=250)

        # ── TOP PRODUK ───────────────────────────
        if "produk" in data.columns:
            st.markdown('<div class="section-title">🏆 Top 5 Produk Terlaris</div>', unsafe_allow_html=True)
            top_produk = data.groupby("produk")["total"].sum().sort_values(ascending=False).head(5).reset_index()
            top_produk.columns = ["Produk", "Total Omzet"]
            top_produk["Total Omzet"] = top_produk["Total Omzet"].apply(lambda x: f"Rp {x:,.0f}")
            st.dataframe(top_produk, use_container_width=True, hide_index=True)

        # ── EXPORT ───────────────────────────────
        st.markdown("---")
        st.markdown('<div class="section-title">💾 Export Laporan Excel</div>', unsafe_allow_html=True)

        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
            data.to_excel(writer, sheet_name="Data Gabungan", index=False)
            harian_total.to_excel(writer, sheet_name="Omzet Harian", index=False)
            platform_total.to_excel(writer, sheet_name="Omzet Per Platform", index=False)
            if "produk" in data.columns:
                data.groupby("produk")["total"].sum().reset_index().to_excel(writer, sheet_name="Top Produk", index=False)

        col_dl, col_info = st.columns([1, 2])
        with col_dl:
            st.download_button(
                label="⬇️ Download Summary Excel",
                data=buffer,
                file_name=f"summary_report_{datetime.today().strftime('%Y%m%d')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        with col_info:
            st.markdown(f"""
            <div class="info-box" style="margin:0">
                ✅ {total_transaksi} transaksi dari {len(uploaded_files)} file · {len(harian_total)} hari data<br>
                Sheet: Data Gabungan, Omzet Harian, Omzet Per Platform, Top Produk
            </div>""", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Error: {e}")
        st.info("Pastikan format CSV sudah benar. Download contoh file dari sidebar.")

else:
    st.markdown("""
    <div style="text-align:center; padding: 56px 0; color: #9ca3af;">
        <div style="font-size: 52px; margin-bottom: 12px;">🗂️</div>
        <div style="font-size: 18px; font-weight: 700; color: #374151; margin-bottom: 8px;">Upload file CSV untuk mulai</div>
        <div style="font-size: 13px;">Bisa upload banyak file sekaligus dari platform berbeda</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown('<div style="text-align:center;font-size:12px;color:#9ca3af">Auto Report Generator · Dibuat oleh <b>Fasfast</b> · Hubungi via sidebar untuk custom fitur</div>', unsafe_allow_html=True)
