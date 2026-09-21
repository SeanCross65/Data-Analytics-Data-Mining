Superconductor Critical Temperature Analysis
Overview
This project investigates what physicochemical properties drive high critical temperature (Tc) in superconductors, and whether a material can be classified as a "practical" superconductor (Tc above 77K, the boiling point of liquid nitrogen) from its composition alone.
Research Questions
What physicochemical properties actually drive high critical temperature?
Can a material be classified as a "practical" superconductor (Tc > 77K) from its composition alone?
Materials with Tc above 77K can be cooled with liquid nitrogen instead of liquid helium, making them far cheaper and more practical for real-world applications (MRI, power transmission, quantum computing).
Dataset
Name: Superconductor Dataset (Kaggle mirror of the UCI "Superconductivty Data" dataset)
Source: kaggle.com/datasets/munumbutt/superconductor-dataset (original: UCI ML Repository)
Size: 21,263 superconductors, 81 physicochemical features, with critical temperature as the target variable
Citation: Hamidieh, K. (2018). A data-driven statistical model for predicting the critical temperature of a superconductor. Computational Materials Science, 154, 346–354.
Full dataset reference, research question rationale, and ethics checklist are documented in notebooks/00_week2_RQ_data_ethics.ipynb.
Project Structure
.
├── data/                    # Local data files
├── notebooks/
│   └── 00_week2_RQ_data_ethics.ipynb   # Research question, dataset reference, ethics checklist
├── slides/                  # Presentation materials
├── SuperConductivity.py     # Downloads dataset via kagglehub, runs exploratory data analysis
└── requirements.txt         # Python dependencies
Setup
Clone this repository.
Install dependencies:
   pip install -r requirements.txt
Run the exploratory analysis script:
   python SuperConductivity.py
This downloads the dataset via kagglehub, then prints shape, summary statistics, missing values, duplicates, and a correlation matrix, and displays histograms of all features.
Notes on Ethics
This dataset contains no personal or human-subject data — it describes chemical compositions and physical properties of materials, not people. The main ethical consideration is publication bias in the underlying literature, which may over-represent already well-studied superconductor families and under-represent negative results or unpublished materials. See the ethics checklist notebook for full details.
