# MLOps-Potential-Stress-Levels

## 📌 Overview

This project develops a machine learning model to predict potential stress levels based on:

* Smartphone usage
* Sleep patterns
* Productivity
* Caffeine consumption

This model is **not intended as a clinical diagnostic tool**, but as a predictive system.

---

# ⚙️ 1. SIMULASI PERIODIK (DATA INGESTION)

Sistem data ingestion dirancang untuk berjalan secara berulang tanpa menimpa data sebelumnya.

## 🔍 Konsep

* Data dibagi menjadi batch (±1000 data per batch)
* Disimpan dengan penamaan berurutan:

  * `batch_001_raw.csv`
  * `batch_002_raw.csv`
  * dan seterusnya
* Data lama tetap tersimpan
* Data baru ditambahkan sebagai batch berikutnya

👉 Pendekatan ini mensimulasikan sistem real-time dan mendukung **Continual Learning**

---

## 📂 Script

```
src/data2/ingestion.py
```

## ⚙️ Fungsi

* Membaca dataset utama
* Membagi data menjadi batch
* Menyimpan ke folder `data/raw_batch`
* Menghindari overwrite dengan penomoran otomatis

## ▶️ Cara Menjalankan

```bash
python src/data2/ingestion.py
```

---

# 🧹 2. DATA PREPROCESSING

## 📂 Script

```
src/data2/process.py
```

## ⚙️ Fungsi

* Menghapus duplikat
* Menangani missing values
* Feature engineering
* Encoding fitur kategorikal
* Menyimpan hasil ke `data/processed`

## ▶️ Cara Menjalankan

```bash
python src/data2/process.py
```

---

# 🗂️ 3. DATA VERSIONING (DVC)

## 🔍 Overview

DVC (Data Version Control) digunakan untuk mengelola dataset besar tanpa menyimpannya langsung di Git.

👉 Git menyimpan **metadata**
👉 DVC mengelola **file data besar**

---

## 3.1 Inisialisasi DVC

```bash
dvc init
git add .
git commit -m "init DVC"
```

---

## 3.2 Tracking Dataset Awal

```bash
dvc add data/raw/Smartphone_Usage_Productivity_Dataset_50000.csv
git add data/raw/*.dvc .gitignore
git commit -m "track dataset v1"
```

### Hasil:

* File `.dvc` dibuat sebagai metadata
* Dataset tidak masuk ke Git
* `.gitignore` diperbarui otomatis

---

## 3.3 Simulasi Penambahan Data

```bash
python src/data2/ingestion.py
```

👉 Data baru disimpan di:

```
data/raw_batch/
```

---

## 3.4 Update Dataset (Continual Learning)

Gabungkan data baru ke dataset utama:

```bash
cat data/raw_batch/batch_001_raw.csv >> data/raw/Smartphone_Usage_Productivity_Dataset_50000.csv
```

---

## 3.5 Versioning Dataset Baru

```bash
dvc add data/raw/Smartphone_Usage_Productivity_Dataset_50000.csv
git add data/raw/*.dvc
git commit -m "update dataset v2"
```

👉 Hash pada file `.dvc` akan berubah → menandakan versi baru

---

## 3.6 Perbandingan Versi Data

```bash
dvc diff
```

👉 Digunakan untuk:

* Melihat perubahan data
* Melacak histori dataset
* Mendukung reproducibility

---

# 📦 4. STRUKTUR FOLDER

```
data/
│
├── raw/
│   └── Smartphone_Usage_Productivity_Dataset_50000.csv
│
├── raw_batch/
│   ├── batch_001_raw.csv
│   ├── batch_002_raw.csv
│
├── processed/
│
src/
├── data2/
│   ├── ingestion.py
│   ├── process.py
│
notebooks/
```

---

# 🧠 5. KONSEP MLOPS YANG DIGUNAKAN

* Data Ingestion (Batch Simulation)
* Data Preprocessing
* Data Versioning (DVC)
* Continual Learning
* Data Lineage

---

# 🚀 6. CARA MENJALANKAN PROJECT

## Install dependencies

```bash
pip install -r requirements.txt
```

## Jalankan ingestion

```bash
python src/data2/ingestion.py
```

## Jalankan preprocessing

```bash
python src/data2/process.py
```

## Jalankan DVC tracking

```bash
dvc add data/raw/Smartphone_Usage_Productivity_Dataset_50000.csv
```

---

# 🎯 7. KESIMPULAN

Proyek ini menunjukkan bahwa:

* Data dapat diperbarui secara berkala (continual learning)
* Dataset besar dapat dikelola tanpa membebani Git
* DVC memungkinkan versioning dan tracking data secara efisien

👉 Dengan pendekatan ini, sistem menjadi:

* Scalable
* Reproducible
* Terstruktur

---

# 💡 CATATAN

* Dataset besar tidak disimpan di Git
* DVC menyimpan metadata melalui file `.dvc`
* Sistem mendukung pengembangan model berbasis data terbaru
