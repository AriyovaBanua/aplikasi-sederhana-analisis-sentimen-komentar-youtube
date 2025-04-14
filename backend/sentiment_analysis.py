import re
import json
import string
from transformers import pipeline

# Load kamus kata alay
with open("resources/_json_colloquial-indonesian-lexicon.txt") as f:
    data = f.read()
lookup_dict = json.loads(data)

# Inisialisasi model sentiment classifier IndoBERT
pretrained_name = "w11wo/indonesian-roberta-base-sentiment-classifier"
nlp = pipeline("sentiment-analysis", model=pretrained_name, tokenizer=pretrained_name)

# Ganti kata sesuai kamus alay
def ganti_kata(kalimat, lookup_dict):
    kata_kata = kalimat.split()
    kalimat_baru = []
    for kata in kata_kata:
        if kata in lookup_dict:
            kalimat_baru.append(lookup_dict[kata])
        else:
            kalimat_baru.append(kata)
    return " ".join(kalimat_baru)

# Pembersihan teks
def clean_text(text):
    text = text.lower()
    text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    text = re.sub(r'@[A-Za-z0-9_]+','', text)  # hapus mention
    text = re.sub(r'#\w+','', text)            # hapus hashtag
    text = re.sub(r'https?://\S+', '', text)   # hapus URL

    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)

    # Ensure the output is a string, not a list or other data type
    text = re.sub(r'[^A-Za-z0-9 ]','', text)
    text = re.sub(r'\s+', ' ', text).strip()
  
    return text

# Analisis sentimen menggunakan RoBERTa
def analyze_sentiment(comments):
    results = {
        "positif": {"jumlah": 0, "komentar": []},
        "netral": {"jumlah": 0, "komentar": []},
        "negatif": {"jumlah": 0, "komentar": []}
    }

    # Preprocessing
    normalized_comments = [ganti_kata(c, lookup_dict) for c in comments]
    cleaned_comments = [clean_text(c) if clean_text(c) else "/n" for c in normalized_comments]

    # Batch prediction
    predictions = nlp(cleaned_comments)

    label_map = {
        "positive": "positif",
        "neutral": "netral",
        "negative": "negatif"
    }

    for original_comment, pred in zip(comments, predictions):
        label = pred['label'].lower()  # e.g., "positive", "neutral", "negative"
        mapped_label = label_map.get(label, "netral")  # fallback ke netral jika tidak ditemukan
        results[mapped_label]["jumlah"] += 1
        if len(results[mapped_label]["komentar"]) < 10:
            results[mapped_label]["komentar"].append(original_comment)

    return results
