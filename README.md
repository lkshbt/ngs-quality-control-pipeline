NGS Read Quality Control Pipeline

A Python-based bioinformatics project for analyzing FASTQ sequencing reads, calculating read-level quality metrics, and generating quality-control reports and visualizations.

Author: Lakshay Saini

Project Overview

Next-generation sequencing (NGS) produces large amounts of sequencing data that must be evaluated before downstream analysis. This project implements a lightweight Python workflow to summarize read length, GC content, and Phred quality scores from compressed FASTQ files.

The project also includes a FastQC report for examining additional sequencing quality indicators.

Features

- Parse FASTQ and gzipped FASTQ files
- Calculate read length and GC content
- Calculate mean Phred quality per read
- Flag reads with mean Phred quality below Q20
- Export read-level metrics to CSV
- Generate summary statistics in JSON format
- Create three quality-control plots
- Examine FastQC reports and quality warnings

Technologies

- Python 3
- Biopython
- pandas
- Matplotlib
- FastQC
- Git and GitHub

Dataset

- Accession: SRR1553426
- Source: European Nucleotide Archive (ENA)
- Input format: Compressed FASTQ (".fastq.gz")

Raw sequencing data is not included in this repository. Download the dataset separately and place the input file at "data/reads.fastq.gz".

Installation

git clone https://github.com/lkshbt/ngs-quality-control-pipeline.git
cd ngs-quality-control-pipeline

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

Usage

1. Download the sequencing dataset.
2. Save the compressed FASTQ file as "data/reads.fastq.gz".
3. Activate the virtual environment.
4. Run the analysis:

python src/qc_pipeline.py

The Python pipeline analyzes up to 10,000 reads and saves the output files in "results/".

Example Results

The Python pipeline produced the following results for the analyzed subset:

Metric| Result
Reads analyzed| 10,000
Mean read length| 101 bases
Mean GC content| 42.16%
Mean Phred quality| 37.52
Reads with mean quality below Q20| 82

These values describe the analyzed subset, not necessarily the entire sequencing dataset.

Quality-Control Visualizations

Read Length Distribution

"Read length distribution" (examples/read_length.png)

GC Content Distribution

"GC content distribution" (examples/gc_content.png)

Mean Phred Quality Distribution

"Mean Phred quality distribution" (examples/read_quality.png)

FastQC Results

A separate FastQC report was generated for "reads.fastq.gz". Its summary reported:

- PASS: Basic statistics, per-base sequence quality, per-sequence quality scores, per-sequence GC content, per-base N content, and sequence length distribution.
- WARN: Per-base sequence content, overrepresented sequences, and adapter content.
- FAIL: Sequence duplication levels.

These results identify areas for further investigation. Duplication and adapter signals must be interpreted in the context of the sequencing library and experiment; a FastQC warning or failure alone does not establish that the data is unusable.

View the "FastQC summary" (results/fastqc/summary.txt).

Output Files

File| Description
"results/read_metrics.csv"| Read-level metrics
"results/summary.json"| Summary statistics
"results/read_length.png"| Read length distribution
"results/gc_content.png"| GC content distribution
"results/read_quality.png"| Mean Phred quality distribution
"results/reads_fastqc.html"| FastQC HTML report, if generated
"results/fastqc/summary.txt"| FastQC module status summary

Generated files are not all committed to Git. The repository retains selected reports and example plots; raw sequencing data is excluded.

Limitations

- The Python pipeline analyzes at most 10,000 reads per run.
- The Q20 threshold is a screening criterion based on mean read quality.
- FastQC module statuses require biological interpretation.
- The project does not currently perform adapter trimming, read alignment, variant calling, or differential gene-expression analysis.

Future Improvements

- Add automated tests and input validation.
- Integrate adapter trimming with Cutadapt.
- Add configurable input paths and read limits.
- Generate a combined quality-control report.
- Extend the workflow to support larger datasets and reproducible pipeline execution.

License

A license has not yet been specified. Add an appropriate open-source license before encouraging reuse or redistribution.
