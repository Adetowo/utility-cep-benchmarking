"""
EBMUD Contract Equity Program Benchmarking Dashboard

Interactive Streamlit dashboard for exploring utility benchmarking results.

Run:
    streamlit run dashboard.py

Visit http://localhost:8501 in your browser.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Page config
st.set_page_config(
    page_title="EBMUD CEP Benchmarking",
    page_icon="📊",
    layout="wide"
)

# Load data
DATA_DIR = Path(__file__).parent.parent / "data"
scores_df = pd.read_csv(DATA_DIR / "utility_dimension_scores.csv")
recommendations_df = pd.read_csv(DATA_DIR / "recommendations_by_priority.csv")

# Separate data
ebmud = scores_df[scores_df["Utility"] == "East Bay Municipal Utility District (EBMUD)"].iloc[0]
peer_avg = scores_df[scores_df["Utility"] == "Peer Average (Excl. EBMUD)"].iloc[0]
peers = scores_df[
    ~scores_df["Utility"].isin([
        "East Bay Municipal Utility District (EBMUD)",
        "Peer Average (Excl. EBMUD)"
    ])
].drop_duplicates(subset=["Utility"])

dimensions = {
    "Design_Structure": "Design & Structure",
    "Implementation_Operations": "Implementation & Operations",
    "Outreach_Accessibility": "Outreach & Accessibility",
    "Program_Outcomes": "Program Outcomes",
    "Economic_Community_Impact": "Economic & Community Impact"
}

# ============================================================================
# HEADER
# ============================================================================

st.title("📊 EBMUD Contract Equity Program Benchmarking")
st.markdown("**Interactive exploration of 9 utility supplier diversity programs**")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("EBMUD Score", f"{ebmud['Overall_Score']:.2f}/5.0", f"{ebmud['Overall_Score'] - peer_avg['Overall_Score']:+.2f} vs peer avg")
with col2:
    st.metric("Rank Among Peers", "9th of 10", "Below average")
with col3:
    st.metric("Largest Gap", "Economic Impact", "-2.45 points")

st.markdown("---")

# ============================================================================
# TAB 1: OVERVIEW
# ============================================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Overview",
    "🔍 Peer Comparison",
    "💡 Recommendations",
    "📋 Methodology"
])

with tab1:
    st.subheader("EBMUD Performance Summary")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Dimension Scores")
        dim_data = []
        for col, name in dimensions.items():
            ebmud_score = ebmud[col]
            peer_score = peer_avg[col]
            gap = ebmud_score - peer_score
            dim_data.append({
                "Dimension": name,
                "EBMUD": f"{ebmud_score:.2f}",
                "Peer Avg": f"{peer_score:.2f}",
                "Gap": f"{gap:+.2f}"
            })
        
        dim_df = pd.DataFrame(dim_data)
        st.dataframe(dim_df, use_container_width=True, hide_index=True)
    
    with col2:
        st.write("### Strengths vs. Gaps")
        
        # Identify strengths and gaps
        strengths = []
        gaps = []
        for col, name in dimensions.items():
            gap = ebmud[col] - peer_avg[col]
            if gap >= 0:
                strengths.append((name, ebmud[col]))
            else:
                gaps.append((name, abs(gap)))
        
        if strengths:
            st.success(f"**✓ Strengths ({len(strengths)})**")
            for dim, score in strengths:
                st.write(f"  • {dim}: {score:.2f}/5.0")
        
        st.error(f"**✗ Gaps ({len(gaps)})**")
        for dim, gap_size in sorted(gaps, key=lambda x: x[1], reverse=True):
            st.write(f"  • {dim}: -{gap_size:.2f} points")

# ============================================================================
# TAB 2: PEER COMPARISON
# ============================================================================

with tab2:
    st.subheader("Peer Utility Comparison")
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        selected_dimension = st.selectbox(
            "Select Dimension to Explore",
            list(dimensions.values())
        )
        show_peer_avg = st.checkbox("Show Peer Average", value=True)
    
    with col1:
        # Create comparison chart
        dim_col = [k for k, v in dimensions.items() if v == selected_dimension][0]
        
        # Get data for all utilities
        all_utils = pd.concat([peers, pd.DataFrame([ebmud])])
        chart_data = all_utils[["Utility", dim_col]].copy()
        chart_data.columns = ["Utility", "Score"]
        chart_data = chart_data.sort_values("Score", ascending=True)
        
        # Create bar chart
        fig, ax = plt.subplots(figsize=(10, 6))
        
        colors = ["#d62728" if u == "East Bay Municipal Utility District (EBMUD)" else "#1f77b4" 
                  for u in chart_data["Utility"]]
        
        ax.barh(chart_data["Utility"], chart_data["Score"], color=colors, alpha=0.8)
        
        if show_peer_avg:
            ax.axvline(x=peer_avg[dim_col], color="orange", linestyle="--", linewidth=2, label=f"Peer Avg: {peer_avg[dim_col]:.2f}")
            ax.legend()
        
        ax.set_xlabel("Score (0-5)", fontsize=11, fontweight="bold")
        ax.set_title(f"{selected_dimension} by Utility", fontsize=12, fontweight="bold")
        ax.set_xlim(0, 5.5)
        ax.grid(axis="x", alpha=0.3)
        
        # Add value labels
        for i, v in enumerate(chart_data["Score"]):
            ax.text(v + 0.1, i, f'{v:.2f}', va='center', fontsize=9)
        
        st.pyplot(fig, use_container_width=True)
    
    st.markdown("---")
    
    st.write("### Utility Rankings (Overall Score)")
    rankings = all_utils[["Utility", "Overall_Score"]].sort_values("Overall_Score", ascending=False)
    rankings.reset_index(drop=True, inplace=True)
    rankings.index = rankings.index + 1
    rankings.columns = ["Utility", "Overall Score"]
    st.dataframe(rankings, use_container_width=True)

# ============================================================================
# TAB 3: RECOMMENDATIONS
# ============================================================================

with tab3:
    st.subheader("Recommendations by Priority")
    
    for idx, row in recommendations_df.iterrows():
        with st.expander(f"**Priority {row['Priority']}:** {row['Dimension']} (Gap: {row['Gap_Points']:+.2f})", expanded=(idx < 2)):
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.write("**Recommendation**")
                st.write(row['Recommendation'])
                st.write(f"\n**Implementation Complexity:** {row['Implementation_Complexity']}")
                st.write(f"**Timeline:** {row['Estimated_Timeline']}")
            
            with col2:
                st.write("**Learn From These Peers**")
                st.write(row['Peer_Examples'])
                st.metric("EBMUD Score", f"{row['EBMUD_Score']:.2f}/5.0", f"{row['Gap_Points']:+.2f} vs peer avg")

# ============================================================================
# TAB 4: METHODOLOGY
# ============================================================================

with tab4:
    st.subheader("Methodology & Data Sources")
    
    st.write("""
    ### Benchmarking Framework
    
    This analysis evaluates 9 utilities across **5 program dimensions** using **33 evidence-based indicators**:
    
    1. **Design & Structure** (8 indicators)
       - Program foundation, policy framework, goal-setting, enforcement mechanisms
    
    2. **Implementation & Operations** (7 indicators)
       - Staff capacity, reporting systems, supplier development programs, data tracking
    
    3. **Outreach & Accessibility** (9 indicators)
       - Supplier engagement, professional development, communication, partnerships
    
    4. **Program Outcomes** (5 indicators)
       - Results reporting, goal attainment, category disaggregation, trends
    
    5. **Economic & Community Impact** (4 indicators)
       - Economic impact documentation, supplier success stories, business growth metrics
    
    ### Scoring Methodology
    
    - **Indicator Scoring:** Each indicator scored 0–3 based on evidence quality
      - 0: Not present/reported
      - 1: Limited/ad hoc activity
      - 2: Clearly documented, consistently implemented
      - 3: Best-in-class, exemplary performance
    
    - **Normalization:** Raw scores normalized to 0–5 scale
      - Formula: `(raw_score / max_possible) × 5`
      - Enables comparison across dimensions with different indicator counts
    
    - **Overall Score:** Mean of 5 dimension scores
    
    ### Data Sources (All Public)
    
    - Annual supplier diversity reports and performance plans
    - CPUC General Order 156 filings (for California utilities)
    - Corporate websites and supplier diversity portals
    - Economic impact studies and community benefit reports
    - Strategic plans, Board resolutions, DEI/ESG reports
    - Utility procurement guides and compliance documentation
    
    ### Utilities Benchmarked
    
    **CPUC-Regulated (CA):**
    - Pacific Gas & Electric (PG&E)
    - Southern California Edison (SCE)
    - San Diego Gas & Electric (SDG&E)
    
    **Public Water Utilities:**
    - DC Water (DC)
    - WSSC Water (MD)
    - American Water (National)
    - EBMUD (CA)
    
    **Other:**
    - Southwest Gas (Multi-state)
    - Dominion Energy (Multi-state)
    
    ### Limitations
    
    - Analysis evaluates publicly documented elements only
    - Some utilities may have undocumented effective practices
    - Economic impact studies reflect self-reported or commissioned findings
    - Utility size, regulatory environment, and geographic factors affect achievable scores
    """)

st.markdown("---")
st.markdown("**Data Last Updated:** November 2025 | **Analysis Period:** October 2024 – November 2025")
