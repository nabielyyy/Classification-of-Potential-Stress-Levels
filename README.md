# MLOps - Stress Level Classification

## Deskripsi Proyek
Proyek ini bertujuan untuk melakukan klasifikasi tingkat stres pengguna berdasarkan data penggunaan smartphone. Dataset yang digunakan berasal dari Kaggle dan berisi berbagai fitur seperti durasi penggunaan ponsel, aktivitas media sosial, dan tingkat produktivitas.

## Tujuan
- Melakukan eksplorasi data (EDA)
- Melakukan preprocessing data
- Membangun model klasifikasi untuk memprediksi tingkat stres
- Mengimplementasikan pipeline MLOps sederhana

## Struktur Direktori
.
├── LICENSE                 # Lisensi proyek
├── README.md               # Dokumentasi proyek
├── config                  # File konfigurasi (parameter model, pipeline, dll)
├── data
│   ├── processed           # Dataset yang sudah melalui tahap preprocessing
│   └── raw                 # Dataset mentah
│       └── Smartphone_Usage_Productivity_Dataset_50000.csv
├── models                  # Penyimpanan model yang sudah dilatih
├── notebooks               # Notebook untuk eksplorasi dan eksperimen
│   └── data_preprocessing.ipynb
├── requirements.txt        # Daftar dependensi Python
└── src
    ├── data                # Script untuk load dan transformasi data
    ├── features            # Script untuk feature engineering
    └── models              # Script untuk training dan evaluasi model

## Cara Menjalankan Proyek (GitHub Codespaces)

1. Buka repositori di GitHub.
2. Klik tombol **Code**.
3. Pilih tab **Codespaces**.
4. Klik **Create Codespace on main**.
5. Setelah environment terbuka, install dependensi:
pip install -r requirements.txt
6. Jalankan notebook pada folder `notebooks/` untuk melakukan eksplorasi data dan preprocessing.

## Dataset
Dataset yang digunakan berasal dari Kaggle:
- Smartphone Usage and Productivity Dataset (50.000 data)

Dataset ini berisi informasi mengenai:
- Durasi penggunaan smartphone
- Aktivitas media sosial
- Tingkat produktivitas
- Indikasi tingkat stres pengguna


