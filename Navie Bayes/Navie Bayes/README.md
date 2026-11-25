# Restaurant Review Sentiment Analysis using Naïve Bayes

## Project Overview
This project applies **Naïve Bayes classification** and Natural Language Processing (NLP) techniques to classify restaurant reviews as **Positive** or **Negative**. It also includes an interactive Streamlit application that lets users submit reviews and view predictions with probability scores.

## Problem Statement
Analyze customer-written restaurant reviews and predict their sentiment label (positive or negative) using text preprocessing, feature extraction, and probabilistic machine learning classifiers.

## Dataset
- **Dataset:** Restaurant reviews
- **Records before cleaning:** 1,000
- **Columns:** Review text and sentiment label (`Liked`)
- **Target labels:** 0 = Negative, 1 = Positive
- **Class balance:** 500 positive and 500 negative reviews in the initial data
- **Data cleaning:** 4 duplicate records were removed; the cleaned dataset contained 996 rows.

## Workflow
1. Load the review dataset and inspect its structure.
2. Clean column names and examine missing values and duplicates.
3. Perform exploratory data analysis (EDA), including sentiment counts and review-length analysis.
4. Preprocess text: lowercase, expand selected contractions, remove digits and punctuation, remove stopwords while preserving negation terms, and apply stemming.
5. Split data into stratified training and testing sets (80/20).
6. Extract text features using CountVectorizer and TF-IDF.
7. Train and evaluate Multinomial Naïve Bayes and Bernoulli Naïve Bayes models.
8. Compare performance using accuracy, precision, recall, F1-score, and confusion matrices.
9. Select the best-performing model and test sample reviews with prediction probabilities.
10. Save the trained model and vectorizer.
11. Build a Streamlit app for interactive sentiment predictions.

## NLP Preprocessing
- Lowercasing
- Expanding selected contractions
- Removing numeric and non-alphabetic characters
- Removing stopwords while retaining negation terms such as `not`, `no`, `nor`, and `never`
- Porter stemming

Preserving negation matters because it can reverse sentiment (e.g., “not good” versus “good”).

## Models and Feature Extraction
- Multinomial Naïve Bayes + CountVectorizer
- Multinomial Naïve Bayes + TF-IDF
- Bernoulli Naïve Bayes with binary features

## Model Results
| Model / Feature Representation | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Multinomial NB + CountVectorizer | 81.0% | 79.81% | 83.0% | 81.37% |
| Multinomial NB + TF-IDF | 79.0% | 76.36% | 84.0% | 80.0% |
| Bernoulli NB | 79.5% | 77.57% | 83.0% | 80.19% |

**Selected model:** Multinomial Naïve Bayes with CountVectorizer (81% accuracy in this experiment).

## Interactive Application
The Streamlit app supports:
- Review text input
- Positive/negative prediction
- Probability scores for both sentiment classes
- Confidence-style progress bars
- Clear-review control

Run from the project folder:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Saved Artifacts
- `sentiment_model.pkl`
- `count_vectorizer.pkl`

## Technologies Used
Python, Jupyter Notebook, Pandas, NumPy, Matplotlib, Seaborn, NLTK, Scikit-learn, Joblib, Streamlit.

## How to Run the Notebook
1. Download or clone the project.
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn nltk scikit-learn joblib streamlit jupyter
   ```
3. Open the notebook in Jupyter Notebook or VS Code.
4. Run cells in order.

## Project Structure
```text
Restaurant-Review-Sentiment-Analysis/
├── Navie Bayes.ipynb
├── Reviews_data.csv
├── app.py
├── sentiment_model.pkl
├── count_vectorizer.pkl
├── requirements.txt
└── README.md
```
*Adjust filenames and included files to match your actual project folder.*

## Key Learnings
- NLP preprocessing for text data
- Text feature extraction using CountVectorizer and TF-IDF
- Naïve Bayes text classification
- Comparing model metrics
- Preserving negation during preprocessing
- Saving model artifacts and integrating them into a Streamlit app

## Limitations
The model may struggle with sarcasm, mixed sentiment, complex context, or vocabulary not represented in its training data. Probability scores are estimates, not guarantees.

## Author
**Bhuvaneshwari Rebba**

Machine Learning practice project completed as part of the Innomatics Research Labs ML module.
