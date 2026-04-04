# MLOps-Potential-Stress-Levels
This study develops a machine learning model to predict potential stress levels based on smartphone usage, sleep patterns, productivity, and caffeine consumption, not as a definitive clinical measurement.
## Simulasi Periodik

Sistem data ingestion dirancang untuk dapat dijalankan secara berulang tanpa menimpa data sebelumnya.

Setiap kali script dijalankan, data akan dibagi ke dalam beberapa batch dengan ukuran tertentu (1000 data per batch), kemudian disimpan dengan penamaan berurutan seperti:

- batch_001_raw.csv
- dan seterusnya

Dengan pendekatan ini, data lama tetap tersimpan dan data baru akan ditambahkan sebagai batch berikutnya. Hal ini mensimulasikan proses pengambilan data secara berkala (periodik) seperti pada sistem real-time.

Pendekatan ini mendukung konsep **Continual Learning**, di mana model dapat terus diperbarui menggunakan data terbaru tanpa kehilangan data historis.
## Data Ingestion

Script: `src/data2/ingestion.py`

Fungsi:
- Membaca dataset utama
- Membagi data menjadi batch (1000 data)
- Menyimpan data ke folder `data/raw`
- Menghindari overwrite dengan sistem penomoran batch

Cara menjalankan:

```bash
python src/data2/ingestion.py

---

# 3. DATA PREPROCESSING

``markdown
## Data Preprocessing

Script: `src/data2/process.py`

Fungsi:
- Membersihkan data (menghapus duplikat, menangani missing value)
- Melakukan feature engineering
- Encoding fitur kategorikal
- Menyimpan data hasil ke folder `data/processed`

Cara menjalankan:

```bash
python src/data2/process.py

---
