# Setup Instructions for GitHub

This document walks you through pushing this portfolio project to GitHub **TODAY**.

---

## Step 1: Create a GitHub Account (If You Don't Have One)

- Go to github.com
- Sign up (free)
- Verify your email

---

## Step 2: Create a New Repository on GitHub

1. Log in to GitHub
2. Click the "+" icon (top right) → "New repository"
3. **Repository name:** `ebmud-cep-benchmarking`
4. **Description:** "Benchmarking analysis of utility supplier diversity programs. Analyzed 9 utilities across 5 dimensions using 33 indicators. Python + Streamlit + real public data."
5. **Visibility:** Public
6. **Initialize with:** None (we'll push existing files)
7. Click "Create repository"

**You'll see:**
```
Quick setup — if you've done this kind of thing before
or

HTTPS:
git clone https://github.com/<your-username>/ebmud-cep-benchmarking.git

SSH:
git clone git@github.com:<your-username>/ebmud-cep-benchmarking.git
```

Copy the HTTPS URL.

---

## Step 3: Install Git Locally (If You Don't Have It)

```bash
# Windows: Download from https://git-scm.com/download/win
# Mac: brew install git
# Linux: sudo apt-get install git

git --version  # Verify installation
```

---

## Step 4: Push This Repo to GitHub

Navigate to your local project folder and run:

```bash
cd /path/to/ebmud-cep-benchmarking

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: EBMUD benchmarking analysis with real data and recommendations"

# Add remote (use the HTTPS URL from Step 2)
git remote add origin https://github.com/<your-username>/ebmud-cep-benchmarking.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Done!** Your repo is now live at `https://github.com/<your-username>/ebmud-cep-benchmarking`

---

## Step 5: Add Key Metadata (Make It Discoverable)

Back on GitHub.com:

1. Go to your repo
2. Click "Settings" (right side)
3. Scroll down to "Repository topics"
4. Add these tags (comma-separated):
   ```
   data-analysis, benchmarking, python, pandas, matplotlib, streamlit, utilities, public-data, consulting
   ```
5. Save

This makes your repo show up in GitHub searches for those terms.

---

## Step 6: Pin It on Your Profile (Make It Visible)

1. Go to github.com/<your-username> (your profile)
2. Scroll to "Popular repositories"
3. Click "Customize your pinned repositories"
4. Check `ebmud-cep-benchmarking`
5. Save

Your most recent visitor sees this repo front-and-center.

---

## Step 7: Add to Your LinkedIn & Resume

**LinkedIn:**
- Update "Featured" section
- Add this repo as a featured project
- Write 1-sentence description: "Benchmarked 9 utilities' supplier diversity programs across 5 dimensions using public data, normalized scores, and delivered peer-sourced recommendations"
- Link directly to GitHub repo

**Resume:**
Under Projects section, add:

```
EBMUD Supplier Diversity Benchmarking Analysis | Python, Pandas, Streamlit | GitHub: [link]
• Analyzed 9 utility companies across 5 dimensions (Design, Implementation, Outreach, Outcomes, Impact) 
  using 33 evidence-based indicators sourced from public CPUC filings and annual reports
• Designed normalization framework (0-3 indicator scores normalized to 0-5 scale) enabling apples-to-apples 
  comparison across uneven category sizes
• Identified EBMUD performance gaps vs. peer average (-0.74 points overall) and prioritized 
  peer-sourced recommendations (economic impact study, supplier advisory council, staffing expansion)
• Delivered interactive Streamlit dashboard and reproducible Python analysis pipeline
```

---

## Step 8: Apply to Google & Artefact

**When applying to Google:**
- Link to GitHub repo
- In cover letter or "Why Google" section: "This benchmarking project demonstrates my ability to find public data, design a replicable framework, and deliver actionable insights using Python and dashboards."
- Show the Streamlit dashboard if interviewing

**When applying to Artefact:**
- Link to GitHub repo
- In cover letter: "This engagement demonstrates the consulting cycle: discovery (design framework) → analysis (score 9 utilities) → benchmarking (identify gaps) → recommendations (peer-sourced solutions). See docs/CONSULTING_BRIEF.md for the full engagement narrative."
- Emphasize the consulting angle, not just the code

---

## Optional: Make a "Fork-Friendly" Version

If you want others (or interviewers) to easily modify and run this:

Add a file called `requirements.txt` to your repo:

```bash
pandas==2.0.0
matplotlib==3.7.0
streamlit==1.30.0
```

Then users can do:
```bash
pip install -r requirements.txt
python scripts/analyze_benchmarking.py
```

---

## Checklist: Before You Hit "Send" to Recruiters

- [ ] Repo is public on GitHub
- [ ] README.md is clear and complete
- [ ] Code runs without errors (tested `python scripts/analyze_benchmarking.py`)
- [ ] All CSVs are readable (can open in Excel)
- [ ] Streamlit dashboard launches without errors (`streamlit run scripts/dashboard.py`)
- [ ] Repo has 3+ topics (for discoverability)
- [ ] Repo is pinned on your GitHub profile
- [ ] LinkedIn "Featured" section includes this repo
- [ ] Resume includes the project with strong bullet points
- [ ] All code is commented and understandable
- [ ] No confidential data in commits (only public sources)
- [ ] Pushed to GitHub (not just local)

---

## Repo Link Template (Copy-Paste for Applications)

```
GitHub Repository: https://github.com/<your-username>/ebmud-cep-benchmarking

Live Dashboard: streamlit run scripts/dashboard.py (after cloning and installing dependencies)

Key Files:
- README.md — Overview and quick summary
- docs/METHODOLOGY.md — Technical deep dive
- docs/CONSULTING_BRIEF.md — Engagement narrative (for Artefact-style roles)
- scripts/analyze_benchmarking.py — Reproducible analysis pipeline
- data/ — Real utility scores and recommendations
```

---

## After You Push: Next Steps

This repo is ready to ship. **But you should start thinking about Project 2 now** (while you're applying):

**Project 2: AI Transformation Lifecycle Framework**
- Phases: Feasibility → Benchmarking (reuse this framework) → Pilot → Governance → Change Management → Measurement
- Timeline: 4-8 weeks to build Phase 1
- Goal: Show full consulting lifecycle + AI angle

---

**Go live with this TODAY. You've got a real, ship-ready portfolio project.**

---

Last updated: August 4, 2026
