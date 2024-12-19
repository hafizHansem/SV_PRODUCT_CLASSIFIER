Product Engagement Classifier for Shopee Video

Deskripsi Proyek

Proyek ini bertujuan untuk membangun sebuah aplikasi berbasis web yang dapat memprediksi engagement produk di platform Shopee Video khusus untuk seorang affiliator Shopee. Dengan menggunakan model klasifikasi yang telah dilatih, aplikasi ini dapat membantu affiliator menentukan apakah suatu produk memiliki potensi untuk dipromosikan.

Aplikasi ini memungkinkan pengguna untuk:

Memasukkan data produk secara manual untuk mendapatkan prediksi kualitas produk.

Mengunggah file CSV berisi data produk untuk prediksi secara batch.

Fitur Utama

Input Manual: Pengguna dapat memasukkan jumlah like, komentar, dan view dari produk secara manual.


Hasil Prediksi: Aplikasi akan memberikan hasil berupa apakah produk tersebut berkualitas untuk afiliasi atau tidak, beserta probabilitas prediksi.

Teknologi yang Digunakan

Bahasa Pemrograman: Python

Framework: Streamlit untuk aplikasi web

Library:

Pandas untuk manipulasi data

Joblib untuk menyimpan dan memuat model

Scikit-learn untuk preprocessing dan model machine learning

Numpy untuk operasi numerik

Cara Menjalankan Aplikasi

Pastikan Anda sudah menginstal Python (versi 3.7 atau lebih baru).

Clone repository ini ke komputer Anda:

git clone [<repository-url>](https://github.com/hafizHansem/SV_PRODUCT_CLASSIFIER.git)

Masuk ke direktori proyek:

cd [<nama-direktori>](SV_PRODUCT_CLASSIFIER)

Install dependensi dengan menjalankan perintah berikut:

pip install -r requirements.txt

Jalankan aplikasi dengan Streamlit:

streamlit run main.py

Akses aplikasi melalui browser di: http://localhost:8501

Anggota Kelompok

Nama Kelompok: Kelompok 15

Anggota:

Hafiz Ilham Ardana

Rafi Purwa


Struktur Dataset

Dataset yang digunakan untuk melatih model memiliki kolom-kolom berikut:

Jumlah Like - Jumlah likes pada produk

Jumlah Komentar - Jumlah komentar pada produk

Jumlah View - Jumlah views pada produk

Fitur tambahan yang dihitung:

log_like - Log transformasi dari jumlah likes

log_view - Log transformasi dari jumlah views

Output Model

Model akan memberikan:

Prediksi kelas: Good Product atau Not Good Product

Probabilitas prediksi

Lisensi

Proyek ini hanya untuk keperluan pembelajaran dan tidak memiliki lisensi resmi.