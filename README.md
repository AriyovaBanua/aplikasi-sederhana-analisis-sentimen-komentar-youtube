# 🇮🇩 Analisis Sentimen Komentar Bahasa Indonesia

Aplikasi ini digunakan untuk menganalisis sentimen komentar dalam Bahasa Indonesia, khususnya dari media sosial atau teks online. Dengan bantuan model **RoBERTa Bahasa Indonesia**, aplikasi ini dapat mengklasifikasikan komentar ke dalam tiga kategori: **positif**, **netral**, atau **negatif**.

---

## Penjelasan Aplikasi

Aplikasi ini terdiri dari dua bagian utama:

1. **Frontend (React + Vite)**
   - Antarmuka pengguna untuk menginput URL video YouTube dan melihat hasil analisis sentimen komentar.

2. **Backend (Flask)**
   - API yang melakukan pengambilan komentar, praproses teks, dan klasifikasi sentimen menggunakan model RoBERTa.

### Alur Proses

1. Pengguna memasukkan URL video YouTube dari frontend.
2. Komentar diambil melalui backend dengan bantuan API YouTube.
3. Backend melakukan:
   - Cleansing komentar
   - Normalisasi kata alay dengan kamus dari [Kamus Alay by nasalsabila](https://github.com/nasalsabila/kamus-alay)
   - Klasifikasi sentimen dengan model RoBERTa
4. Hasil analisis dikirim kembali ke frontend.
5. Frontend menampilkan hasil dalam bentuk grafik pie dan daftar komentar.

---

## 📦 Library yang Dibutuhkan

### Backend (Python)
- `Flask`
- `requests`
- `python-dotenv`
- `transformers`
- `torch`

### Frontend (React + Vite)
- `recharts`
- `axios`

---

## ⚙️ Instalasi & Menjalankan Aplikasi

### 1. **Clone Project**
```bash
https://github.com/AriyovaBanua/aplikasi-sederhana-analisis-sentimen-komentar-youtube.git
```

### 2. **Masuk ke Folder Backend dan Buat Environment**
Ganti nama file env menjadi .env.
Ubah isinya dengan Youtube data API Key milikmu
```
YOUTUBE_API_KEY= API_KEY_KAMU
```

### 3. **Instalasi Library Backend**
```bash
pip install -r requirements.txt
```

### 4. **Jalankan Backend**
```bash
python app.py
```

### 5. **Masuk ke Folder Frontend dan Instalasi**
```bash
cd ../frontend
npm install
```

### 6. **Jalankan Frontend**
```bash
npm install axios
npm install recharts
npm run dev
```

Pastikan backend berjalan di `localhost:5000` dan frontend di `localhost:5173`.

---

## 📃 Struktur Folder

```
project/
│
├── backend/
│   ├── env/                            # Virtual environment
│   ├── app.py                          # Flask backend utama
│   ├── sentiment_analysis.py           # Modul analisis sentimen
│   ├── youtube_api.py                  # Pengambilan komentar dari YouTube
│   ├── requirements.txt                # Daftar pustaka Python
│   ├── .env.template                   # Template konfigurasi API key
│   └── resources/
│       └── _json_colloquial-indonesian-lexicon.txt  # Kamus alay
│
└── frontend/                           # Vite + React app
    ├── src/
    │   ├── App.jsx
    │   └── ...
    ├── package.json
    ├── requirements.txt                # Kebutuhan frontend
    └── ...
```

---

## 🔧 Cara Menggunakan (Frontend)

1. Jalankan `npm run dev` di folder frontend.
2. Masukkan URL YouTube pada input.
3. Klik "Analisis".
4. Hasil analisis akan muncul dalam grafik dan daftar komentar.

---

## 📓 Contoh Output Backend

```json
{
  "positif": {
    "jumlah": 5,
    "komentar": ["Keren banget!", "Suka videonya"]
  },
  "netral": {
    "jumlah": 2,
    "komentar": ["Biasa aja"]
  },
  "negatif": {
    "jumlah": 3,
    "komentar": ["Nggak bagus", "Kurang seru"]
  }
}
```

---

## 📚 Sumber Model & Lexicon

- Model: [w11wo/indonesian-roberta-base-sentiment-classifier](https://huggingface.co/w11wo/indonesian-roberta-base-sentiment-classifier)
- Kamus Alay: [nasalsabila/kamus-alay](https://github.com/nasalsabila/kamus-alay)

---

## 🧑‍💻 Author

Ariyova Banua – Informatika, Universitas Sanata Dharma  

