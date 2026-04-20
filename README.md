# IT5006 Group 8 - Chicago Crime Risk Prediction

This repository contains the dataset, notebooks, trained models, evaluation outputs, and Streamlit application for the IT5006 Group 8 project on Chicago crime risk prediction.

## Project Structure

```text
IT5006-Group8/
├── data/
├── deployment/
├── docs/
├── notebooks/
├── src/
└── README.md
```

## Folder Overview

- `data/` - project dataset files
- `deployment/` - environment and dependency files
- `docs/` - reports, submission package, figures, and evaluation outputs
- `notebooks/` - exploratory analysis, model development, and comparison notebooks
- `src/` - Streamlit app and trained model files

## Main Files

### Dataset
- `data/chicago_crime_2015_2024_enriched.parquet`

### Notebooks
- `notebooks/Chicago_Crime_EDA_2015_2024_v2.ipynb` - exploratory data analysis and data understanding
- `notebooks/IT5006_Crime_Prediction_Baselines_Training_Validation.ipynb` - baseline model training and validation
- `notebooks/models_for_proposed_problem.ipynb` - proposed model development and tuning
- `notebooks/Model evaluation&Comparison.ipynb` - model evaluation and comparison

### Source / Models
- `src/app.py` - Streamlit web application
- `src/best_logistic_regression.joblib` - saved Logistic Regression model
- `src/best_random_forest.joblib` - saved Random Forest model
- `src/chicago_crime_model_lightgbm_tuned.joblib` - tuned LightGBM model
- `src/chicago_crime_model_xgboost_tuned.joblib` - tuned XGBoost model used by the app

## Setup

Install the required packages:

```bash
pip install -r deployment/requirements.txt
```

## Run the Streamlit App

```bash
streamlit run src/app.py
```

## Reproducing the Workflow

If you want to review or reproduce the project workflow, a simple order is:

1. Open the EDA notebook for data exploration.
2. Run the baseline training and validation notebook.
3. Run the proposed model notebook.
4. Review the evaluation and comparison notebook.
5. Launch the Streamlit app for interactive prediction.

## Notes

- The deployed prediction app currently uses the tuned XGBoost model.
- Evaluation outputs, figures, and submission documents are stored in `docs/`.
