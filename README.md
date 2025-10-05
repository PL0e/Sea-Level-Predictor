# Sea Level Predictor

This project analyzes global average sea level change since 1880 and predicts sea level through 2050.

## Requirements

- Python 3.x
- pandas
- matplotlib
- scipy
- numpy

## Setup

1. Make sure you have the `epa-sea-level.csv` data file in the same directory as the scripts
2. Install required packages:
   \`\`\`bash
   pip install pandas matplotlib scipy numpy
   \`\`\`

## Usage

Run the main script:
\`\`\`bash
python scripts/main.py
\`\`\`

Or run just the sea level predictor:
\`\`\`bash
python scripts/sea_level_predictor.py
\`\`\`

## What it does

1. Imports sea level data from `epa-sea-level.csv`
2. Creates a scatter plot of Year vs CSIRO Adjusted Sea Level
3. Calculates and plots a line of best fit using all data (1880-present) extending to 2050
4. Calculates and plots a second line of best fit using only data from 2000-present, also extending to 2050
5. Saves the plot as `sea_level_plot.png`

## Files

- `sea_level_predictor.py` - Main analysis code
- `main.py` - Entry point for development and testing
- `test_module.py` - Unit tests
- `epa-sea-level.csv` - Data file (you need to provide this)
