# Life Calendar Generator - Project Plan

## Project Overview

**Life Calendar Generator** - A CLI tool that creates a printable PDF showing a person's life in weeks (0-90 years old), with past weeks filled in black.

### Inspiration
Based on the Wait But Why life calendars: https://store.waitbutwhy.com/collections/life-calendars

### Purpose
To help humans understand how precious time is by visualizing their entire life as weeks, showing what has passed and what potentially remains.

---

## Technical Approach

### Technology Stack
- **Language**: Python 3 (simple, readable, great for this task)
- **PDF Generation**: ReportLab (most straightforward Python PDF library)
- **Date Handling**: Built-in `datetime` module (no external dependency)
- **Dependencies**: Minimal - just ReportLab for PDF generation

### Design Principles
- **KISS (Keep It Simple, Stupid)**: Minimal dependencies, straightforward code
- **Single purpose**: Does one thing well - generates life calendar PDFs
- **Easy to use**: Simple CLI interface with one input (birthdate)
- **Printable output**: High-quality PDF suitable for printing

---

## Core Components

### 1. Input Handler
- Prompt user for birthdate (format: YYYY-MM-DD)
- Validate the input (proper date format, not future date, reasonable year)
- Calculate current age in weeks

### 2. Calendar Calculator
- Calculate which week of which year the person was born
- Calculate total weeks lived from birth to today
- Determine which boxes to fill (coordinates in the 52×90 grid)
- Account for the starting week offset (birthday might not be week 1)

### 3. PDF Generator
- Create A4 or Letter-sized page (landscape orientation)
- Draw 52×90 grid of small squares
- Fill appropriate squares black (weeks lived)
- Leave future weeks empty/white
- Add minimal labels (week numbers on top, ages on left side)
- Use thin transparent/gray borders for grid lines

---

## Implementation Plan

### Phase 1: Core Logic (30-45 min)
1. Set up project structure (single Python file for KISS)
2. Implement birthdate input and validation
3. Calculate weeks lived since birth
4. Create grid coordinate mapping logic
5. Test calculation accuracy with sample dates

### Phase 2: PDF Generation (45-60 min)
1. Set up ReportLab PDF canvas
2. Calculate optimal square size for page (fit 52×90 grid)
3. Draw grid with thin borders
4. Fill lived weeks with black color
5. Add axis labels (weeks 1-52 on X-axis, ages 0-90 on Y-axis)
6. Test PDF output and print quality

### Phase 3: Testing & Polish (15-30 min)
1. Test with various birthdates (edge cases)
2. Ensure PDF prints correctly on standard paper
3. Add basic error handling (invalid dates, future dates)
4. Create simple README with usage instructions
5. Add informative output messages

**Total Estimated Time**: 1.5 - 2.5 hours

---

## File Structure

```
life-calendar/
├── life_calendar.py    # Single main script (all logic)
├── requirements.txt    # Just: reportlab
└── README.md          # Usage instructions
```

### Alternative (if complexity grows)
```
life-calendar/
├── life_calendar.py    # Main CLI entry point
├── calculator.py       # Date/week calculations
├── pdf_generator.py    # PDF creation logic
├── requirements.txt
└── README.md
```

---

## User Flow

```bash
$ python life_calendar.py
Enter your birthdate (YYYY-MM-DD): 1990-05-15
Generating your life calendar...
PDF saved as: life_calendar_1990-05-15.pdf
You have lived 1,752 weeks out of 4,680 possible weeks.
```

---

## Key Design Decisions

### Grid Layout
- **Dimensions**: 52 columns (weeks) × 90 rows (years)
- **Orientation**: Week 1 at top-left, progressing left-to-right, then down by age
- **Total boxes**: 4,680 squares representing potential weeks of life

### Page Configuration
- **Size**: A4 landscape (297mm × 210mm) - fits 52 columns nicely
- **Alternative**: Letter landscape if A4 doesn't fit well
- **Square size**: ~4-5mm per square (makes 52×90 fit on one page)
- **Margins**: 10-15mm on all sides for printer safety

### Visual Style
- **Border style**: Thin gray lines (0.5pt) - visible but not dominant
- **Lived weeks**: Solid black fill
- **Future weeks**: White/empty with gray border
- **Labels**: Small, minimal font for week numbers and ages

### Output
- **Filename pattern**: `life_calendar_YYYY-MM-DD.pdf`
- **Location**: Current directory
- **Quality**: High resolution for printing

---

## Technical Specifications

### Date Calculations
- Birth week is week 0 of age 0
- Each row represents 52 weeks (1 year)
- Account for partial first week (birthday might be mid-week)
- Use ISO week calculation or simple division (7 days = 1 week)

### Grid Coordinates
```
(0,0) = Week 1, Age 0    (51,0) = Week 52, Age 0
(0,1) = Week 1, Age 1    (51,1) = Week 52, Age 1
...
(0,89) = Week 1, Age 89  (51,89) = Week 52, Age 89
```

### PDF Generation Details
```python
# Example calculations for A4 landscape
page_width = 297mm
page_height = 210mm
usable_width = page_width - (2 * margin)
usable_height = page_height - (2 * margin)
square_size = min(usable_width/52, usable_height/90)
```

---

## Potential Enhancements (Future)

### Nice to Have
- Add title/header with name and birthdate
- Include current age and weeks lived statistics
- Add quote or motivational text
- Support different life expectancies (not just 90)
- Command-line arguments for customization

### Advanced Features
- Color-code different life phases (childhood: blue, adult: green, retirement: gold)
- Add major life events as markers (graduations, marriage, children)
- Support for multiple people on one page (family calendars)
- Interactive mode to add life events
- Different themes/color schemes

### Technical Improvements
- Configuration file for customization
- Multiple output formats (PNG, SVG)
- Web interface option
- GUI wrapper for non-technical users

---

## Dependencies

### Required
```txt
reportlab==4.0.7  # Or latest stable version
```

### Built-in Python Modules
- `datetime` - date calculations
- `argparse` - CLI arguments (optional)
- `sys` - system operations
- `os` - file operations

---

## Testing Plan

### Test Cases
1. **Valid inputs**
   - Recent birthdate (2020s)
   - Middle-aged person (1980s-1990s)
   - Elderly person (1930s-1940s)

2. **Edge cases**
   - Born on January 1st (week 1 alignment)
   - Born on December 31st (year boundary)
   - Born exactly today
   - Leap year birthdays

3. **Invalid inputs**
   - Future date
   - Invalid format
   - Non-existent date (Feb 30)
   - Very old dates (before 1900)

4. **Output quality**
   - PDF opens correctly
   - Grid is properly aligned
   - Squares are correct size
   - Prints clearly on paper

---

## Success Criteria

- ✓ User can input birthdate easily
- ✓ PDF generates in under 5 seconds
- ✓ Grid is accurately filled based on birthdate
- ✓ PDF prints clearly on standard printer
- ✓ Code is simple and maintainable (<200 lines)
- ✓ Only one external dependency (ReportLab)
- ✓ Works on Windows, Mac, Linux

---

## Getting Started (Future Implementation)

### Installation
```bash
pip install reportlab
```

### Usage
```bash
python life_calendar.py
```

### Example Output
```
Enter your birthdate (YYYY-MM-DD): 1985-03-15
Generating your life calendar...
✓ PDF saved as: life_calendar_1985-03-15.pdf
  You have lived 2,077 weeks out of 4,680 possible weeks.
  That's 44.4% of a 90-year life.
```

---

## Notes

- Keep the code simple and readable (KISS principle)
- Comment key calculations for clarity
- Handle errors gracefully with helpful messages
- Make it satisfying to use (good feedback messages)
- Remember: this is a personal, meaningful tool - keep it human

---

**Project Status**: Planning Complete ✓
**Next Step**: Ready for implementation
