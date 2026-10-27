import gzip
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from Bio import SeqIO

INPUT = "data/reads.fastq.gz"
OUT = Path("results")
MAX_READS = 10000
OUT.mkdir(exist_ok=True)


def main():
    rows = []

    with gzip.open(INPUT, "rt") as handle:
        for record in SeqIO.parse(handle, "fastq"):
            seq = str(record.seq).upper()
            q = record.letter_annotations["phred_quality"]

            if not seq or not q:
                continue

            bases = sum(seq.count(b) for b in "ACGT")
            gc = 100 * (seq.count("G") + seq.count("C")) / bases if bases else 0

            rows.append({
                "read_id": record.id,
                "length": len(seq),
                "gc_percent": round(gc, 2),
                "mean_quality": round(sum(q) / len(q), 2)
            })

            if len(rows) >= MAX_READS:
                break

    if not rows:
        raise ValueError("No valid reads found.")

    df = pd.DataFrame(rows)
    df["low_quality"] = df["mean_quality"] < 20
    df.to_csv(OUT / "read_metrics.csv", index=False)

    summary = {
        "reads_analyzed": len(df),
        "mean_read_length": round(float(df["length"].mean()), 2),
        "mean_gc_percent": round(float(df["gc_percent"].mean()), 2),
        "mean_read_quality": round(float(df["mean_quality"].mean()), 2),
        "low_quality_reads": int(df["low_quality"].sum())
    }

    (OUT / "summary.json").write_text(json.dumps(summary, indent=2))

    for column, filename, label in [
        ("length", "read_length.png", "Read length (bases)"),
        ("gc_percent", "gc_content.png", "GC content (%)"),
        ("mean_quality", "read_quality.png", "Mean Phred quality")
    ]:
        plt.figure(figsize=(7, 4))
        plt.hist(df[column], bins=30, edgecolor="black")
        plt.xlabel(label)
        plt.ylabel("Number of reads")
        plt.title(label + " distribution")
        plt.tight_layout()
        plt.savefig(OUT / filename, dpi=150)
        plt.close()

    print(json.dumps(summary, indent=2))
    print("QC completed. Results saved in:", OUT.resolve())


if __name__ == "__main__":
    main()
