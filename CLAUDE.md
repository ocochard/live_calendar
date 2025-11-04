# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Life Calendar Generator: A Python CLI tool that generates a printable PDF showing a person's life in weeks (0-90 years). Past weeks are filled in black, future weeks remain empty. Inspired by Wait But Why Life Calendars.

## Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running the Application

```bash
# Interactive mode (prompts for birthdate)
python life_calendar.py

# With command-line arguments
python life_calendar.py --birthdate 1990-05-15
python life_calendar.py --birthdate 1990-05-15 --title "My Personal Life Journey"

# Help
python life_calendar.py --help
```

## Code Architecture

Single-file application (`life_calendar.py`) with these key components:

1. **Input Handling**
   - `get_birthdate()`: Interactive prompt with validation
   - `main()`: Argument parsing using argparse, supports `--birthdate` and `--title` flags

2. **Calculation**
   - `calculate_weeks_lived()`: Converts birthdate to weeks lived (days // 7)

3. **PDF Generation**
   - `create_life_calendar_pdf()`: Uses ReportLab to generate A4 portrait PDF
   - Grid: 52 weeks × 90 years = 4,680 total squares
   - Spacing: Gaps between boxes equal to half the box size for readability
   - Layout: Past weeks filled black, future weeks empty with grey border

## PDF Layout Details

- Page: A4 portrait (210mm × 297mm)
- Margins: 15mm + space for labels (20mm left, 20mm top)
- Grid positioning: Dynamically calculated to center the 52×90 grid with spacing
- Square size: Auto-calculated to fit available space
- Labels: Age (0-85 left, 90 right), weeks (top axis, every 5 weeks)
- Directional arrows show time progression (age down, weeks right)

## Design Principles

Follows KISS principle: minimal dependencies (only ReportLab), single file, straightforward logic, no external configuration.
