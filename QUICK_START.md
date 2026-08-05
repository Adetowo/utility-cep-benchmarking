# Quick Start Guide

Get up and running with the EBMUD benchmarking analysis in 5 minutes.

---

## Option 1: View Without Installing (Fastest)

**Just want to see the results?**
- Open `README.md` in this repo for an overview
- Read `data/utility_dimension_scores.csv` (open in Excel) to see the scores
- Read `data/recommendations_by_priority.csv` to see prioritized recommendations
- View the images in `visuals/` folder for charts

**No coding required. Takes ~5 minutes to understand the analysis.**

---

## Option 2: Run the Python Analysis (10 minutes)

**Want to reproduce the analysis or modify the data?**

### Step 1: Install Python (if you don't have it)
```bash
# Download from https://python.org
# Install version 3.9+
python --version  # Verify installation
```

### Step 2: Clone or Download This Repository
```bash
# Via Git
git clone <this-repo-url>
cd ebmud-cep-benchmarking

# OR: Download as ZIP and unzip
```

### Step 3: Install Dependencies
```bash
pip install pandas matplotlib
```

### Step 4: Run the Analysis
```bash
cd scripts
python analyze_benchmarking.py
```

**What happens:**
- Reads data from `data/utility_dimension_scores.csv`
- Calculates normalized scores and gaps
- Generates charts in `visuals/` folder
- Prints summary to console

**Output:**
```
================================================================================
EBMUD CONTRACT EQUITY PROGRAM BENCHMARKING ANALYSIS
================================================================================

OVERALL PERFORMANCE
  EBMUD Score:        3.57/5.0
  Peer Average:       4.31/5.0
  Gap:                -0.74 points (below average)
  Rank:               #9 of 10 utilities

[More analysis...]

✓ Saved: dimension_comparison.png
✓ Saved: utility_rankings.png
✓ Saved: gap_analysis.png
```

---

## Option 3: Interactive Dashboard (Streamlit) — Best for Exploration

**Want to explore the data interactively?**

### Step 1: Install Streamlit
```bash
pip install streamlit
```

### Step 2: Launch the Dashboard
```bash
cd scripts
streamlit run dashboard.py
```

**What happens:**
- A web browser opens automatically
- You see an interactive dashboard with:
  - Overview metrics
  - Peer comparison charts (filterable by dimension)
  - Utility rankings
  - Recommendations (expandable by priority)
  - Methodology documentation

**Features:**
- ✓ Filter utilities and dimensions
- ✓ See EBMUD vs. peer average
- ✓ Explore each recommendation with peer examples
- ✓ Download data as CSV

---

## Option 4: For Data Analysts / Engineers (Advanced)

**Want to modify the analysis or use this as a template?**

### Open in Python/Jupyter
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
scores = pd.read_csv("data/utility_dimension_scores.csv")
recs = pd.read_csv("data/recommendations_by_priority.csv")

# Analyze
print(scores)
print(recs)

# Modify and re-run
# See scripts/analyze_benchmarking.py for full pipeline
```

### Extend the Framework
```python
# Example: Add a new utility
new_utility = {
    "Utility": "New Utility Name",
    "Overall_Score": 3.8,
    "Design_Structure": 4.0,
    # ... etc
}

# Add to scores dataframe and re-run analysis
```

---

## File Structure Overview

```
ebmud-cep-benchmarking/
├── README.md                          Main overview (start here)
├── QUICK_START.md                     This file
├── data/
│   ├── utility_dimension_scores.csv   All utility scores (real data)
│   ├── recommendations_by_priority.csv Prioritized recommendations
│   └── analysis_summary.txt           Generated summary
├── scripts/
│   ├── analyze_benchmarking.py        Main analysis script
│   └── dashboard.py                   Interactive Streamlit dashboard
├── docs/
│   ├── METHODOLOGY.md                 Detailed technical documentation
│   ├── CONSULTING_BRIEF.md            Full engagement narrative
│   └── README.md                      Documentation index
└── visuals/
    ├── dimension_comparison.png       EBMUD vs peer average
    ├── utility_rankings.png           Peer rankings
    └── gap_analysis.png               Gap analysis by dimension
```

---

## Common Questions

### Q: Can I modify the data and re-run?
**A:** Yes. Edit `data/utility_dimension_scores.csv` (or `data/recommendations_by_priority.csv`), then re-run `python scripts/analyze_benchmarking.py`. Charts regenerate automatically.

### Q: What if I want to add a new utility?
**A:** Add a new row to `data/utility_dimension_scores.csv` with scores for all 5 dimensions. Re-run the script to see the new utility in rankings and comparisons.

### Q: Can I use this framework for a different program?
**A:** Absolutely. Adapt the 5 dimensions and 33 indicators to fit your program (e.g., clean energy programs, apprenticeships, small business development). The normalization logic and comparative framework remain the same.

### Q: How do I understand the methodology?
**A:** Read `docs/METHODOLOGY.md` for detailed explanation of:
- Why these 5 dimensions
- How the scoring works (0–3 scale)
- How normalization works (0–5 scale)
- Why each recommendation was prioritized

### Q: Where do the utility names and scores come from?
**A:** All data is sourced from public documents (CPUC filings, annual reports, websites). See `data/` folder for CSVs and `docs/METHODOLOGY.md` for source citations.

---

## For Interviews (Google / Artefact)

**Google Data Analytics Roles:** Emphasize the Python reproducibility
- "I built this entire analysis using pandas and matplotlib"
- "Here's how the data was transformed and normalized"
- "Run the Python script to regenerate everything"

**Artefact Consulting Roles:** Emphasize the engagement structure
- "I took an ambiguous problem and built a measurable framework"
- "Identified gaps and translated them into peer-sourced recommendations"
- "See `docs/CONSULTING_BRIEF.md` for the full engagement narrative"

---

## Next Steps

1. **Understand the Results** → Read `README.md` (5 min)
2. **Explore the Data** → Open `data/*.csv` in Excel (5 min)
3. **See the Charts** → View `visuals/` folder (2 min)
4. **Understand the Methodology** → Read `docs/METHODOLOGY.md` (10 min)
5. **Run the Analysis** → Execute `python scripts/analyze_benchmarking.py` (2 min)
6. **Interact with Dashboard** → Launch `streamlit run scripts/dashboard.py` (5 min)
7. **Review Recommendations** → Read `docs/CONSULTING_BRIEF.md` (15 min)

---

## Troubleshooting

### "Command not found: python"
```bash
# Try python3 instead
python3 scripts/analyze_benchmarking.py
```

### "ModuleNotFoundError: No module named 'pandas'"
```bash
# Install dependencies
pip install pandas matplotlib streamlit
```

### "No such file or directory: data/utility_dimension_scores.csv"
```bash
# Make sure you're in the project root directory
cd /path/to/ebmud-cep-benchmarking
python scripts/analyze_benchmarking.py
```

### Charts not showing in Streamlit
```bash
# Make sure you're in the scripts directory
cd scripts
streamlit run dashboard.py
```

---

## Need Help?

- **Understanding the analysis?** → Read `README.md` or `docs/METHODOLOGY.md`
- **Want to modify the code?** → Start with `scripts/analyze_benchmarking.py` (heavily commented)
- **Want to understand the consulting angle?** → Read `docs/CONSULTING_BRIEF.md`
- **Have questions?** → Check the FAQ above or review the code comments

---

**Happy exploring! This analysis should take you from 0 to 60 on EBMUD's supplier diversity program in under 30 minutes.**
