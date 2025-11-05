# geo2r-top250-filter
Minimal reproducible pipeline to filter top 250 genes from GEO2R

## Overview

GEO2R provides differential expression results for GEO datasets. This repository shows a simple workflow to:

1. Load GEO2R output.
2. Filter genes by significance (adjusted p-value) and magnitude of change (log2 fold change).
3. Select the top 250 genes with the strongest expression changes.

---

## Requirements

- Python 3.10+  
- pandas 1.5+  

Install pandas:

```bash
pip install pandas

Input Data

- Excel .xlsx file from GEO2R (or TSV/CSV if converted)

- Required columns:

    Gene – Gene name or ID
    logFC – log2 fold change
    adjPVal – adjusted p-value (FDR corrected)

Usage

The code was developed and tested in Spyder (Python IDE).
1. Open filter_top_genes.py in Spyder
2. Make sure your GEO2R file (e.g., GSE15852.xlsx) is in the same folder or update the path
3. Run the script
4. The top 250 gene names will be saved to top_250_genes_names_only.csv
The top 250 genes can be used for downstream analysis such as pathway enrichment or visualization.

Filtering Criteria
  Adjusted p-value < 0.05 → ensures statistical significance
  Absolute log2 fold change |logFC| ≥ 1 → selects genes with ≥2-fold change
  Top 250 genes are selected based on the largest absolute logFC

Notes
  Minimal working example for educational purposes
  Assumes GEO2R output is normalized and contains required columns
  Contributions and suggestions welcome via GitHub Pull Requests

References

GEO2R
 – NCBI GEO differential expression tool (https://www.ncbi.nlm.nih.gov/geo/geo2r/)

pandas
 – Python data analysis library (https://pandas.pydata.org/)
