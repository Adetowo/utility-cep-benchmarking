"""
EBMUD Contract Equity Program Benchmarking Analysis

This script reproduces the core benchmarking analysis:
1. Loads utility dimension scores
2. Compares EBMUD to peer average
3. Identifies performance gaps
4. Generates visualizations
5. Summarizes peer-sourced recommendations

Data Sources:
- All utility data sourced from public CPUC filings, annual reports, and corporate websites
- Scoring based on 33 evidence-based indicators across 5 program dimensions
- Methodology ensures auditability and replicability

Run:
    python analyze_benchmarking.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Set up paths
DATA_DIR = Path(__file__).parent.parent / "data"
VISUALS_DIR = Path(__file__).parent.parent / "visuals"
VISUALS_DIR.mkdir(exist_ok=True)

# ============================================================================
# LOAD DATA
# ============================================================================

scores_df = pd.read_csv(DATA_DIR / "utility_dimension_scores.csv")
recommendations_df = pd.read_csv(DATA_DIR / "recommendations_by_priority.csv")

# Separate EBMUD from peers
ebmud = scores_df[scores_df["Utility"] == "East Bay Municipal Utility District (EBMUD)"].iloc[0]
peer_avg = scores_df[scores_df["Utility"] == "Peer Average (Excl. EBMUD)"].iloc[0]
peers = scores_df[
    ~scores_df["Utility"].isin([
        "East Bay Municipal Utility District (EBMUD)",
        "Peer Average (Excl. EBMUD)"
    ])
].drop_duplicates(subset=["Utility"])

# ============================================================================
# ANALYSIS 1: OVERALL PERFORMANCE
# ============================================================================

print("\n" + "=" * 80)
print("EBMUD CONTRACT EQUITY PROGRAM BENCHMARKING ANALYSIS")
print("=" * 80)

print(f"\nOVERALL PERFORMANCE")
print(f"  EBMUD Score:        {ebmud['Overall_Score']:.2f}/5.0")
print(f"  Peer Average:       {peer_avg['Overall_Score']:.2f}/5.0")
print(f"  Gap:                {ebmud['Overall_Score'] - peer_avg['Overall_Score']:.2f} points (below average)")

# Rank EBMUD among peers
all_utils = pd.concat([peers, pd.DataFrame([ebmud])])
all_utils_sorted = all_utils.sort_values("Overall_Score", ascending=False).reset_index(drop=True)
ebmud_rank = all_utils_sorted[all_utils_sorted["Utility"] == "East Bay Municipal Utility District (EBMUD)"].index[0] + 1
print(f"  Rank:               #{ebmud_rank} of {len(all_utils)} utilities")

# ============================================================================
# ANALYSIS 2: DIMENSION-BY-DIMENSION BREAKDOWN
# ============================================================================

dimensions = [
    "Design_Structure",
    "Implementation_Operations",
    "Outreach_Accessibility",
    "Program_Outcomes",
    "Economic_Community_Impact"
]

dim_names = {
    "Design_Structure": "Design & Structure",
    "Implementation_Operations": "Implementation & Operations",
    "Outreach_Accessibility": "Outreach & Accessibility",
    "Program_Outcomes": "Program Outcomes",
    "Economic_Community_Impact": "Economic & Community Impact"
}

print(f"\nDIMENSION-BY-DIMENSION PERFORMANCE")
print(f"\n{'Dimension':<40} {'EBMUD':<8} {'Peer Avg':<8} {'Gap':<8} {'Status':<15}")
print("-" * 80)

gaps = {}
for dim in dimensions:
    ebmud_score = ebmud[dim]
    avg_score = peer_avg[dim]
    gap = ebmud_score - avg_score
    gaps[dim_names[dim]] = gap
    
    status = "✓ Strength" if gap >= 0 else "✗ Gap"
    print(f"{dim_names[dim]:<40} {ebmud_score:<8.2f} {avg_score:<8.2f} {gap:+.2f}    {status:<15}")

# ============================================================================
# ANALYSIS 3: IDENTIFY STRENGTHS & CRITICAL GAPS
# ============================================================================

print(f"\nKEY FINDINGS")

strengths = [dim for dim, gap in gaps.items() if gap >= 0]
print(f"\nEBMUD Strengths ({len(strengths)}):")
for s in strengths:
    print(f"  ✓ {s}: {ebmud[s.replace(' & ', '_').replace(' ', '_')]:.2f}/5.0 (peer avg: {peer_avg[s.replace(' & ', '_').replace(' ', '_')]:.2f})")

critical_gaps = recommendations_df.nsmallest(3, "Gap_Points")
print(f"\nCritical Performance Gaps (Top 3):")
for idx, row in critical_gaps.iterrows():
    print(f"  {idx+1}. {row['Dimension']}")
    print(f"     Gap: {row['Gap_Points']:+.2f} points | EBMUD: {row['EBMUD_Score']:.2f} vs Peer Avg: {row['Peer_Avg_Score']:.2f}")
    print(f"     Recommendation: {row['Recommendation']}")
    print(f"     Learn from: {row['Peer_Examples']}")
    print()

# ============================================================================
# VISUALIZATION 1: Dimension Comparison
# ============================================================================

fig, ax = plt.subplots(figsize=(14, 7))

x = np.arange(len(dimensions))
width = 0.35

ebmud_values = [ebmud[d] for d in dimensions]
peer_avg_values = [peer_avg[d] for d in dimensions]
dim_labels = [dim_names[d] for d in dimensions]

bars1 = ax.bar(x - width/2, ebmud_values, width, label="EBMUD", color="#1f77b4", alpha=0.8)
bars2 = ax.bar(x + width/2, peer_avg_values, width, label="Peer Average", color="#ff7f0e", alpha=0.8)

ax.set_xlabel("Program Dimension", fontsize=12, fontweight="bold")
ax.set_ylabel("Score (0-5 Scale)", fontsize=12, fontweight="bold")
ax.set_title("EBMUD vs. Peer Average: Dimension Scores", fontsize=14, fontweight="bold")
ax.set_xticks(x)
ax.set_xticklabels(dim_labels, rotation=15, ha="right")
ax.legend(fontsize=11)
ax.set_ylim(0, 5.5)
ax.grid(axis="y", alpha=0.3)

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}',
                ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig(VISUALS_DIR / "dimension_comparison.png", dpi=300, bbox_inches="tight")
print("✓ Saved: dimension_comparison.png")

# ============================================================================
# VISUALIZATION 2: Utility Rankings
# ============================================================================

fig, ax = plt.subplots(figsize=(12, 8))

rankings = all_utils_sorted[["Utility", "Overall_Score"]].reset_index(drop=True)
colors = ["#d62728" if u == "East Bay Municipal Utility District (EBMUD)" else "#1f77b4" 
          for u in rankings["Utility"]]

# Shorten utility names for display
display_names = [
    u.replace("East Bay Municipal Utility District (", "")
     .replace("Pacific Gas & Electric (PG&E)", "PG&E")
     .replace("Southern California Edison (SCE)", "SCE")
     .replace("San Diego Gas & Electric (SDG&E)", "SDG&E")
     .replace("Washington Suburban Sanitary Commission", "WSSC Water")
     .replace(")", "")
    for u in rankings["Utility"]
]

ax.barh(display_names, rankings["Overall_Score"], color=colors, alpha=0.8)
ax.set_xlabel("Overall Score (0-5 Scale)", fontsize=12, fontweight="bold")
ax.set_title("Utility Benchmarking Rankings", fontsize=14, fontweight="bold")
ax.set_xlim(0, 5.5)
ax.grid(axis="x", alpha=0.3)

# Add value labels
for i, v in enumerate(rankings["Overall_Score"]):
    ax.text(v + 0.1, i, f'{v:.2f}', va='center', fontsize=10, fontweight="bold")

# Add legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#d62728', alpha=0.8, label='EBMUD'),
    Patch(facecolor='#1f77b4', alpha=0.8, label='Peer Utilities')
]
ax.legend(handles=legend_elements, fontsize=11)

plt.tight_layout()
plt.savefig(VISUALS_DIR / "utility_rankings.png", dpi=300, bbox_inches="tight")
print("✓ Saved: utility_rankings.png")

# ============================================================================
# VISUALIZATION 3: Gap Analysis (Heatmap style)
# ============================================================================

fig, ax = plt.subplots(figsize=(10, 6))

gap_data = pd.DataFrame({
    "Dimension": [dim_names[d] for d in dimensions],
    "Gap_Points": [gaps[dim_names[d]] for d in dimensions]
})
gap_data = gap_data.sort_values("Gap_Points")

colors_gaps = ["#d62728" if x < 0 else "#2ca02c" for x in gap_data["Gap_Points"]]
ax.barh(gap_data["Dimension"], gap_data["Gap_Points"], color=colors_gaps, alpha=0.8)
ax.set_xlabel("Gap (EBMUD Score - Peer Avg)", fontsize=12, fontweight="bold")
ax.set_title("EBMUD Performance Gaps by Dimension\n(Negative = Below Peer Average)", 
             fontsize=14, fontweight="bold")
ax.axvline(x=0, color="black", linestyle="--", linewidth=1)
ax.grid(axis="x", alpha=0.3)

# Add value labels
for i, v in enumerate(gap_data["Gap_Points"]):
    offset = 0.05 if v > 0 else -0.05
    ha = "left" if v > 0 else "right"
    ax.text(v + offset, i, f'{v:+.2f}', va='center', ha=ha, fontsize=11, fontweight="bold")

plt.tight_layout()
plt.savefig(VISUALS_DIR / "gap_analysis.png", dpi=300, bbox_inches="tight")
print("✓ Saved: gap_analysis.png")

# ============================================================================
# EXPORT SUMMARY REPORT
# ============================================================================

summary_report = f"""
EXECUTIVE SUMMARY: EBMUD CONTRACT EQUITY PROGRAM BENCHMARKING

Overall Performance:
  - EBMUD Score: {ebmud['Overall_Score']:.2f}/5.0
  - Peer Average: {peer_avg['Overall_Score']:.2f}/5.0
  - Gap: {ebmud['Overall_Score'] - peer_avg['Overall_Score']:.2f} points
  - Rank: #{ebmud_rank} of {len(all_utils)} utilities

Strengths:
{chr(10).join([f"  ✓ {dim}: {ebmud[dim.replace(' & ', '_').replace(' ', '_')]:.2f}/5.0" for dim in strengths])}

Critical Gaps:
{chr(10).join([f"  {idx+1}. {row['Dimension']}: {row['Gap_Points']:+.2f} points" for idx, row in critical_gaps.iterrows()])}

Key Insight:
EBMUD has sound program design (4.38/5.0) but faces capacity constraints in execution 
(3.57/5.0 Implementation) and supplier engagement (3.70/5.0 Outreach). The most critical gap 
is Economic & Community Impact measurement (1.25/5.0), where EBMUD lacks peer-comparable 
economic impact documentation and supplier success tracking.

Recommendation Priority:
1. Commission Independent Economic Impact Study (peer examples: PG&E, SCE, SDG&E)
2. Establish Supplier Advisory Council + expand professional development (peer examples: SCE, SDG&E, PG&E)
3. Expand staffing capacity and implement real-time tracking dashboard (peer examples: WSSC Water, PG&E)
"""

with open(DATA_DIR / "analysis_summary.txt", "w") as f:
    f.write(summary_report)
print("✓ Saved: analysis_summary.txt")

print("\n" + "=" * 80)
print("Analysis complete. Check /visuals for charts and /data for summary report.")
print("=" * 80)
