# PCA on Breast Cancer Gene Expression Data

## Project Overview

This project performs **Principal Component Analysis (PCA)** on breast cancer gene expression data to classify samples into:

- **ER+ (Estrogen Receptor Positive)**
- **ER− (Estrogen Receptor Negative)**

The objective is to reproduce patterns similar to Figure 1 from the original breast cancer study using computational analysis.

This project was completed as part of the **Bioinformatics coursework** at :contentReference[oaicite:0]{index=0}.

---

## Dataset

Dataset Source: **:contentReference[oaicite:1]{index=1}**

Files used:

- `class.tsv` → Sample class labels
- `filtered.tsv.gz` → Gene expression matrix
- `columns.tsv.gz` → Gene ID to gene symbol mapping

---

## Objectives

### 1. Gene Expression Scatter Plot

Extract expression levels for:

- **:contentReference[oaicite:2]{index=2}**
- **:contentReference[oaicite:3]{index=3}**

Generate a scatter plot to visualize separation between ER+ and ER− samples.

---

### 2. Principal Component Analysis

Apply **:contentReference[oaicite:4]{index=4}** to reduce dimensionality of gene expression data.

Plot:

- PC1
- PC2

to visualize clustering of breast cancer samples.

---

## Technologies Used

- **:contentReference[oaicite:5]{index=5}**
- **:contentReference[oaicite:6]{index=6}**
- **:contentReference[oaicite:7]{index=7}**
- **:contentReference[oaicite:8]{index=8}**
- **:contentReference[oaicite:9]{index=9}**

---

## Project Structure

```text
bioinformatics-pca/
│
├── data/
│   ├── class.tsv
│   ├── filtered.tsv.gz
│   └── columns.tsv.gz
│
├── pca_analysis.py
├── README.md
```

---

## Installation

Install required libraries:

```bash
pip install pandas numpy matplotlib scikit-learn
```

---

## Run the Project

```bash
python3 pca_analysis.py
```

---

## Output

The program generates:

### Figure 1a
Scatter plot of:

- GATA3 expression
- XBP1 expression

---

### Figure 1c
PCA projection of breast cancer samples.

---

## Biological Interpretation

The genes **XBP1** and **GATA3** are important biomarkers associated with estrogen receptor activity in breast cancer.

PCA helps reveal dominant variation patterns in gene expression data and assists in distinguishing ER+ and ER− tumor samples.

---

## Learning Outcomes

This project demonstrates:

- Biological data preprocessing
- Gene annotation mapping
- Dimensionality reduction
- Data visualization
- Computational analysis using Python

---

## Author

**Tanishq**  
1st Year Biotechnology  
:contentReference[oaicite:10]{index=10}
