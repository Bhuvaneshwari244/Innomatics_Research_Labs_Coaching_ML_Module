# Banknote Authentication using K-Nearest Neighbors (KNN) Classification

## Project Overview
This project applies the **K-Nearest Neighbors (KNN) Classification** algorithm to the Banknote Authentication dataset. The objective is to classify banknotes as **authentic or counterfeit** using numerical features derived from banknote images.

## Problem Statement
Build a classification model that uses the banknote's numerical measurements to predict its authentication class.

## Dataset
The dataset contains numerical features derived from images of banknotes and a target label indicating the class.

- **Task type:** Binary classification
- **Target:** Authentication class (authentic / counterfeit)
- **Features:** Numerical measurements extracted from banknote images

## Workflow
1. Load the dataset and inspect its structure.
2. Perform exploratory data analysis (EDA).
3. Check data quality and duplicate records.
4. Prepare features and target labels.
5. Split data into training and testing sets.
6. Train the KNN classification model.
7. Evaluate predictions using classification metrics.
8. Review the confusion matrix and classification report.

## Algorithm: K-Nearest Neighbors
KNN is a distance-based algorithm. For a new data point, it finds the nearest training observations and predicts the class based on the majority class among those neighbors. The choice of `k` and feature scaling can influence performance.

## Results
The model achieved **100% test accuracy** in the reported experiment.

| Metric | Result |
|---|---:|
| Test accuracy | 100% |
| Test samples | 275 |

The result is specific to this train/test split. Duplicate records were identified during project review, so duplicate handling and the split strategy should be considered when interpreting the score.

## Technologies Used
- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib / Seaborn
- Scikit-learn

## How to Run
1. Clone or download this project folder.
2. Install the required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter
   ```
3. Open the notebook in Jupyter Notebook or VS Code.
4. Run the notebook cells from top to bottom.

## Key Learnings
- Understanding a classification problem and its target labels.
- Exploring numerical datasets and checking data quality.
- Training and evaluating a distance-based classifier.
- Interpreting accuracy, confusion matrices, precision, recall, and F1-score.
- Recognizing the importance of data preparation and avoiding data leakage.

## Project Structure
```text
Banknote-Authentication-KNN/
├── notebook.ipynb
├── dataset.csv
└── README.md
```
*Update the example filenames above to match the files in your project folder.*

## Author
**Bhuvaneshwari Rebba**

Machine Learning practice project completed as part of the Innomatics Research Labs ML module.
