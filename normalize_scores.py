"""
normalize_scores.py

Reusable scoring engine for the Supplier Diversity / Contract Equity
Benchmarking Framework.

WHAT IT DOES
------------
1. Reads indicator-level evidence scores (0-3 scale) for one or more
   organizations across five program dimensions.
2. Sums indicator scores within each dimension and normalizes to a
   0-5 scale using: (raw_score / max_possible_score) * 5
3. Computes an overall score per organization (mean of the five
   normalized dimension scores).
4. Outputs a tidy summary table (CSV) and a grouped bar chart (PNG)
   comparing every organization across all five dimensions.

WHY THIS APPROACH
------------------
Raw indicator counts differ by dimension (e.g. Outreach & Accessibility
has 9 indicators, Economic & Community Impact has only 4). Normalizing
to a common 0-5 scale makes dimensions comparable to each other and
across organizations of different sizes -- the same logic used in
benchmarking, scorecarding, and rubric-based evaluation work broadly
(including LLM/AI evaluation rubrics, which use an analogous
weighted-criteria-to-common-scale approach).

USAGE
-----
    python normalize_scores.py --input ../data/sample_scores.csv

Swap in your own CSV with the same three columns
(organization, dimension, score_0_to_3) to reuse this on any
comparative benchmarking project.
"""

import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt


def load_scores(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    required_cols = {"organization", "dimension", "score_0_to_3"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Input CSV is missing required columns: {missing}")
    return df


def normalize(df: pd.DataFrame) -> pd.DataFrame:
    """Sum raw scores per org/dimension, then normalize to a 0-5 scale."""
    grouped = (
        df.groupby(["organization", "dimension"])["score_0_to_3"]
        .agg(raw_score="sum", n_indicators="count")
        .reset_index()
    )
    grouped["max_possible"] = grouped["n_indicators"] * 3
    grouped["normalized_score_0_5"] = (
        grouped["raw_score"] / grouped["max_possible"] * 5
    ).round(2)
    return grouped


def pivot_summary(normalized: pd.DataFrame) -> pd.DataFrame:
    pivot = normalized.pivot(
        index="organization", columns="dimension", values="normalized_score_0_5"
    )
    pivot["Overall Score"] = pivot.mean(axis=1).round(2)
    return pivot.sort_values("Overall Score", ascending=False)


def plot_comparison(pivot: pd.DataFrame, output_path: str) -> None:
    dims = [c for c in pivot.columns if c != "Overall Score"]
    ax = pivot[dims].plot(
        kind="bar",
        figsize=(12, 6),
        width=0.8,
    )
    ax.set_ylabel("Normalized Score (0-5)")
    ax.set_title("Program Benchmarking: Dimension Scores by Organization")
    ax.set_ylim(0, 5)
    ax.legend(loc="upper left", bbox_to_anchor=(1.0, 1.0), fontsize=8)
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    print(f"Saved chart to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Benchmark scoring engine")
    parser.add_argument(
        "--input", default="../data/sample_scores.csv", help="Path to input CSV"
    )
    parser.add_argument(
        "--summary-out",
        default="../data/summary_scores.csv",
        help="Path to write the summary CSV",
    )
    parser.add_argument(
        "--chart-out",
        default="../visuals/dimension_comparison.png",
        help="Path to write the comparison chart",
    )
    args = parser.parse_args()

    df = load_scores(args.input)
    normalized = normalize(df)
    pivot = pivot_summary(normalized)

    os.makedirs(os.path.dirname(args.summary_out), exist_ok=True)
    os.makedirs(os.path.dirname(args.chart_out), exist_ok=True)

    pivot.to_csv(args.summary_out)
    print("\n=== Normalized Dimension Scores (0-5 scale) ===")
    print(pivot.to_string())

    plot_comparison(pivot, args.chart_out)


if __name__ == "__main__":
    main()
