# NGS Read Quality Control Pipeline

A Python bioinformatics project for analyzing FASTQ sequencing reads and generating quality-control summaries.

## Features
- FASTQ and gzipped FASTQ parsing
- Read length and GC content calculation
- Mean Phred quality calculation
- Low-quality read flagging using a mean Q20 threshold
- CSV and JSON summary reports
- Three QC plots

## Technologies
- Python 3
- Biopython
- pandas
- Matplotlib
- Git

## Dataset
Public sequencing dataset: SRR1553426
Source: European Nucleotide Archive (ENA)

Raw sequencing data is not included in this repository.

## Installation
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
Download the dataset and save it as `data/reads.fastq.gz`.

Run:
```bash
python src/qc_pipeline.py
```

The current script analyzes up to 10,000 reads.

## Example Results
Results from the first 10,000 reads:
- Mean read length: 101 bases
- Mean GC content: 42.16%
- Mean Phred quality: 37.52
- Reads flagged below mean Q20: 82

These are preliminary subset results.

## Limitations
This project performs basic read-level QC. It does not perform adapter trimming, alignment, variant calling, or differential gene-expression analysis. A Q20 flag is a screening threshold, not a universal definition of a poor-quality read.

## Author
Lakshay Saini
