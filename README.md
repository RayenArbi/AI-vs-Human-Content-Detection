# 🧠 AI vs Human Content Detection (EDA + Modeling)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--learn%20%7C%20XGBoost%20%7C%20LightGBM-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

Detect whether a text is **AI-generated** or **human-written** using machine learning.  
Includes **EDA**, **feature engineering**, and **model comparison**.

---

## 📂 Dataset Summary

- **Records:** 1,367  
- **Features:** 17  
- **Target:** `label` (1 = AI, 0 = Human)  
- **Year:** 2025  

| Feature | Description |
|---------|-------------|
| `text_content` | Raw text |
| `content_type` | Content category |
| `word_count` | Number of words |
| `character_count` | Character count |
| `sentence_count` | Number of sentences |
| `lexical_diversity` | Unique words / total words |
| `avg_sentence_length` | Words per sentence |
| `avg_word_length` | Characters per word |
| `punctuation_ratio` | Punctuation / total chars |
| `flesch_reading_ease` | Readability score |
| `gunning_fog_index` | Readability complexity |

---

## 🔍 Exploratory Data Analysis (EDA)

**Key insights:**
- AI texts tend to have **higher lexical diversity** with **shorter sentences**.
- Human texts show **wider punctuation variation**.
- Readability metrics separate the classes well.

<p align="center">
  <img src="images/class_distribution.png" width="45%" alt="Class Distribution">
  <img src="images/readability_scores.png" width="45%" alt="Readability Scores">
</p>

---

## ⚙️ Modeling

Tested models:
- Logistic Regression
- Random Forest
- XGBoost ✅ *(Best Performer)*
- LightGBM
- SVM
- KNN

**Best Model:** **XGBoost Classifier**  
**Accuracy:** ~**93%** on test data with **balanced precision & recall**.

<p align="center">
  <img src="images/confusion_matrix.png" width="50%" alt="Confusion Matrix">
</p>

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/AI-vs-Human-Content-Detection.git
cd AI-vs-Human-Content-Detection
pip install -r requirements.txt
