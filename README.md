# Product Engagement Classifier for Shopee Video

## Deskripsi Proyek
Proyek ini bertujuan untuk membangun sebuah aplikasi berbasis web yang dapat memprediksi engagement produk di platform Shopee Video khusus untuk seorang affiliator Shopee. Dengan menggunakan model klasifikasi yang telah dilatih, aplikasi ini dapat membantu affiliator menentukan apakah suatu produk memiliki potensi untuk dipromosikan.

Aplikasi ini memungkinkan pengguna untuk:
- Memasukkan data produk secara manual untuk mendapatkan prediksi engagement produk.


## Fitur Utama
1. **Input Manual:** Pengguna dapat memasukkan jumlah like, komentar, dan view dari produk secara manual.
2. **Hasil Prediksi:** Aplikasi akan memberikan hasil berupa apakah produk tersebut ber-engagement untuk afiliasi atau tidak, beserta probabilitas prediksi.

## Teknologi yang Digunakan
- **Bahasa Pemrograman:** Python
- **Framework:** Streamlit untuk aplikasi web
- **Library:**
  - Pandas untuk manipulasi data
  - Joblib untuk menyimpan dan memuat model
  - Scikit-learn untuk preprocessing dan model machine learning
  - Numpy untuk operasi numerik

## Cara Menjalankan Aplikasi
1. Pastikan Anda sudah menginstal Python (versi 3.7 atau lebih baru).
2. Clone repository ini ke komputer Anda:
   ```bash
   git clone https://github.com/hafizHansem/SV_PRODUCT_CLASSIFIER.git
   ```
3. Masuk ke direktori proyek:
   ```bash
   cd SV_PRODUCT_CLASSIFIER
   ```
4. Install dependensi dengan menjalankan perintah berikut:
   ```bash
   pip install -r requirements.txt
   ```
5. Jalankan aplikasi dengan Streamlit:
   ```bash
   streamlit run main.py
   ```
6. Akses aplikasi melalui browser di: `http://localhost:8501`

## Anggota Kelompok
- **Nama Kelompok:** Kelompok 7
- **Anggota:**
  1. Hafiz Ilham Ardana
  2. Rafi Purwa

## Struktur Dataset
Dataset yang digunakan untuk melatih model memiliki kolom-kolom berikut:
- `Jumlah Like` - Jumlah likes pada produk
- `Jumlah Komentar` - Jumlah komentar pada produk
- `Jumlah View` - Jumlah views pada produk

Fitur tambahan yang dihitung:
- `log_like` - Log transformasi dari jumlah likes
- `log_view` - Log transformasi dari jumlah views

## Output Model
Model akan memberikan:
- Prediksi kelas: **Good Product** atau **Not Good Product**
- Probabilitas prediksi

## Lisensi
Proyek ini hanya untuk keperluan pembelajaran dan tidak memiliki lisensi resmi.

---

Terima kasih telah menggunakan aplikasi ini! Jika Anda memiliki pertanyaan, silakan hubungi anggota kelompok.

