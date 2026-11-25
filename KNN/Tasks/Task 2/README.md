# Concrete Compressive Strength Prediction using KNN Regression

## Project Overview
This project uses **K-Nearest Neighbors (KNN) Regression** to estimate the compressive strength of concrete based on its composition and age-related input features.

## Problem Statement
Predict concrete compressive strength from the concrete mixture's input variables using a regression model.

## Dataset
The dataset includes concrete mixture variables and a target column representing compressive strength.

- **Task type:** Regression
- **Target:** Concrete compressive strength
- **Inputs:** Concrete composition and age-related numerical features

## Workflow
1. Load the dataset and inspect the data.
2. Perform exploratory data analysis (EDA).
3. Examine feature distributions and relationships with the target.
4. Prepare input features and target values.
5. Split the dataset into training and testing sets.
6. Apply feature scaling where appropriate for a distance-based model.
7. Train the KNN regression model.
8. Compare distance metrics.
9. Evaluate the model using MAE, MSE, RMSE, and R².

## Algorithm: K-Nearest Neighbors Regression
KNN Regression predicts a numeric value by finding the nearest training samples and combining their target values (commonly by averaging). Because KNN relies on distances, feature scaling is important when inputs have different ranges.

## Model Evaluation
Reported test results:

| Metric | Score |
|---|---:|
| MAE | 7.1005 |
| MSE | 83.9194 |
| RMSE | 9.1608 |
| R² Score | 0.7187 |

The model's R² score indicates that it captured a meaningful portion of the variation in the target on the test split. The error metrics describe the typical size of prediction errors in the target's units (MAE and RMSE).

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
- Difference between classification and regression tasks.
- Exploring and preparing numerical data.
- Scaling features for distance-based algorithms.
- Applying KNN to predict continuous values.
- Comparing distance metrics.
- Evaluating regression models with MAE, MSE, RMSE, and R².

## Project Structure
```text
Concrete-Strength-KNN-Regression/
├── notebook.ipynb
├── dataset.csv
└── README.md
```
*Update the example filenames above to match the files in your project folder.*

## Author
**Bhuvaneshwari Rebba**

Machine Learning practice project completed as part of the Innomatics Research Labs ML module.
