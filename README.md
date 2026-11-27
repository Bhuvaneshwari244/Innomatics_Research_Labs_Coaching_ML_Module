# Innomatics Research Labs — Machine Learning Module  

A collection of hands-on Machine Learning assignments completed as part of the **Innomatics Research Labs ML Module**. The repository demonstrates end-to-end ML workflows—from understanding and preparing data to training, evaluating, comparing, and applying models.

## 📌 Repository Overview

This repository contains three projects covering classification, regression, and text sentiment analysis.

| Task | Project | ML Type | Algorithm | Dataset / Domain |
|---|---|---|---|---|
| 01 | Banknote Authentication | Classification | K-Nearest Neighbors (KNN) | Banknote authenticity |
| 02 | Concrete Compressive Strength Prediction | Regression | K-Nearest Neighbors (KNN) Regression | Concrete strength |
| 03 | Restaurant Review Sentiment Analysis | Text Classification | Naïve Bayes | Restaurant customer reviews |

---

## 🧠 Projects

### 1. Banknote Authentication — KNN Classification

**Objective:** Predict whether a banknote is authentic or counterfeit based on numerical features.

**Workflow:**
- Load and inspect the dataset
- Check data quality and explore feature distributions
- Prepare features and target labels
- Split data into training and testing sets
- Train a KNN classification model
- Evaluate predictions using accuracy, confusion matrix, and classification metrics

**Evaluation:** The notebook achieved **100% accuracy** on its test split. This result should be interpreted carefully because duplicate records were identified during review; duplicate handling and a fresh evaluation can help assess how well the model generalizes.

**Key learning:** Classification workflow, distance-based learning, train/test evaluation, and classification metrics.

### 2. Concrete Compressive Strength Prediction — KNN Regression

**Objective:** Estimate concrete compressive strength from its ingredient and age-related input features.

**Workflow:**
- Load and inspect the dataset
- Perform exploratory data analysis and check data quality
- Prepare the input features and continuous target
- Split into training and testing data
- Train and evaluate KNN regression models
- Compare distance metrics and regression evaluation scores

**Reported evaluation:**

| Metric | Score |
|---|---:|
| MAE | 7.1005 |
| MSE | 83.9194 |
| RMSE | 9.1608 |
| R² | 0.7187 |

**Key learning:** Regression, distance-based prediction, model comparison, and interpreting error metrics.

### 3. Restaurant Review Sentiment Analysis — Naïve Bayes

**Objective:** Classify restaurant reviews as **Positive** or **Negative** using text-processing and Naïve Bayes models. The project also includes a Streamlit interface for interactive predictions.

**Workflow:**
- Inspect the review dataset and sentiment labels
- Clean column names and check missing/duplicate data
- Explore sentiment balance and review lengths
- Preprocess text (lowercase, contraction handling, remove unwanted characters, stopword filtering while preserving negation, and stemming)
- Split into training and testing data
- Build text features using CountVectorizer and TF-IDF
- Train and compare Naïve Bayes variants
- Evaluate models using accuracy, precision, recall, F1-score, and confusion matrices
- Save the selected model and vectorizer
- Use the saved artifacts in a Streamlit prediction app

**Model comparison (reported):**

| Model / Features | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Multinomial NB + CountVectorizer | 81.0% | 79.81% | 83.0% | 81.37% |
| Multinomial NB + TF-IDF | 79.0% | 76.36% | 84.0% | 80.0% |
| Bernoulli NB + Binary Count Features | 79.5% | 77.57% | 83.0% | 80.19% |

**Selected model:** Multinomial Naïve Bayes with CountVectorizer.

**App features:**
- Enter a review and predict its sentiment
- View Positive and Negative probability estimates
- Clear the review field
- Simple interactive Streamlit interface

**Key learning:** NLP preprocessing, vectorization, Naïve Bayes comparison, model serialization, probability output, and building a simple ML app.

---

## 🛠️ Tools & Technologies

- Python
- Jupyter Notebook
- Pandas and NumPy
- Matplotlib / Seaborn (data visualization)
- Scikit-learn
- NLTK (text preprocessing)
- Joblib (saving/loading trained model artifacts)
- Streamlit (interactive application)
- Git and GitHub (version control and project hosting)

---

## 📂 Suggested Repository Structure

```text
Innomatics_Research_Labs_Coaching_ML_Module/
├── Task_01_KNN_Classification/
│   ├── notebook.ipynb
│   └── dataset/                 # if included
├── Task_02_KNN_Regression/
│   ├── notebook.ipynb
│   └── dataset/                 # if included
├── Task_03_Naive_Bayes_Sentiment/
│   ├── Navie Bayes.ipynb
│   ├── app.py
│   ├── sentiment_model.pkl
│   ├── count_vectorizer.pkl
│   ├── requirements.txt
│   └── dataset/                 # if included
└── README.md
```

*Adjust the folder/file names in this example to match the actual names in the repository.*

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Bhuvaneshwari244/Innomatics_Research_Labs_Coaching_ML_Module.git
cd Innomatics_Research_Labs_Coaching_ML_Module
```

### 2. Create and activate a virtual environment (recommended)

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

Install the libraries needed for the notebooks:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter nltk joblib streamlit
```

If a project has its own `requirements.txt`, install it from that project folder:

```bash
pip install -r requirements.txt
```

### 4. Run notebooks

Launch Jupyter:

```bash
jupyter notebook
```

Open the relevant notebook and run the cells in order.

### 5. Run the sentiment analysis app (Task 03)

From the Task 03 project directory, make sure the model and vectorizer files are present, then run:

```bash
python -m streamlit run app.py
```

Streamlit will open the application in your browser. Enter a restaurant review and click **Analyze Sentiment** to view the predicted sentiment and probability estimates.

---

## 📊 Skills Demonstrated

- Data loading, inspection, and cleaning
- Exploratory Data Analysis (EDA)
- Feature and target preparation
- Train/test splitting
- Classification and regression
- KNN and Naïve Bayes algorithms
- Text preprocessing and feature extraction
- Model evaluation and comparison
- Saving and loading ML artifacts
- Building an interactive ML application
- Organizing and documenting projects with GitHub

---

## ⚠️ Notes

- Results are specific to the datasets and train/test splits used in the notebooks; they are not guarantees of performance on new data.
- The Banknote Authentication notebook's reported perfect test accuracy warrants checking for duplicates or possible data leakage before treating it as generalizable.
- For the sentiment app, the preprocessing logic used at inference time should remain consistent with the preprocessing used when training the model and vectorizer.
- Dataset files may be omitted from GitHub if they are large, restricted, or not intended for redistribution. If omitted, provide a note explaining how to obtain them.

---

## 👩‍💻 Author

**Bhuvaneshwari Rebba**

Machine Learning assignments and projects completed as part of the Innomatics Research Labs coaching/module.

---

## 🔗 Repository

[Innomatics Research Labs — Coaching ML Module](https://github.com/Bhuvaneshwari244/Innomatics_Research_Labs_Coaching_ML_Module)

---

⭐ If you find this repository useful, feel free to explore the notebooks and project implementations.
