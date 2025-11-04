#!/usr/bin/env python3
"""
Life Calendar Generator
Creates a printable PDF showing a person's life in weeks (0-90 years old).
Past weeks are filled in black, future weeks remain empty.
"""

from datetime import datetime, date
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, lightgrey
import sys
import argparse


def get_birthdate():
    """Prompt user for birthdate and validate input."""
    while True:
        try:
            date_str = input("Enter your birthdate (YYYY-MM-DD): ").strip()
            birthdate = datetime.strptime(date_str, "%Y-%m-%d").date()

            # Validate date is not in the future
            if birthdate > date.today():
                print("Error: Birthdate cannot be in the future. Please try again.")
                continue

            # Validate date is reasonable (not before 1900)
            if birthdate.year < 1900:
                print("Error: Please enter a birthdate after 1900.")
                continue

            return birthdate

        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD (e.g., 1990-05-15)")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            sys.exit(0)


def calculate_weeks_lived(birthdate):
    """Calculate the number of weeks lived from birthdate to today."""
    today = date.today()
    days_lived = (today - birthdate).days
    weeks_lived = days_lived // 7
    return weeks_lived


def create_life_calendar_pdf(birthdate, weeks_lived, filename, title="A 90-Year Human Life in Weeks"):
    """Generate PDF with life calendar grid."""

    # Page setup - A4 landscape
    page_width, page_height = landscape(A4)

    # Grid dimensions
    weeks_per_year = 52
    max_age = 90
    total_weeks = weeks_per_year * max_age  # 4,680 weeks

    # Calculate margins and square size
    margin = 15 * mm
    label_space_left = 20 * mm  # Space for age labels
    label_space_top = 15 * mm   # Space for week labels

    usable_width = page_width - (2 * margin) - label_space_left
    usable_height = page_height - (2 * margin) - label_space_top

    # Calculate square size to fit grid
    square_width = usable_width / weeks_per_year
    square_height = usable_height / max_age
    square_size = min(square_width, square_height)

    # Adjust grid starting position to center it
    grid_width = square_size * weeks_per_year
    grid_height = square_size * max_age

    start_x = margin + label_space_left + (usable_width - grid_width) / 2
    start_y = page_height - margin - label_space_top - (usable_height - grid_height) / 2

    # Create PDF
    c = canvas.Canvas(filename, pagesize=landscape(A4))

    # Add title
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(page_width / 2, page_height - margin, title)

    # Draw grid
    c.setLineWidth(0.5)
    c.setStrokeColor(lightgrey)

    for age in range(max_age):
        for week in range(weeks_per_year):
            x = start_x + (week * square_size)
            y = start_y - (age * square_size) - square_size

            # Calculate which box number this is (0-indexed)
            box_number = age * weeks_per_year + week

            # Fill with black if this week has been lived
            if box_number < weeks_lived:
                c.setFillColor(black)
                c.rect(x, y, square_size, square_size, fill=1, stroke=1)
            else:
                c.setFillColor(black)
                c.rect(x, y, square_size, square_size, fill=0, stroke=1)

    # Add age labels on the left (every 5 years, except 90)
    c.setFont("Helvetica", 7)
    c.setFillColor(black)
    for age in range(0, max_age, 5):  # Changed max_age + 1 to max_age to exclude 90
        y = start_y - (age * square_size) - (square_size / 2)
        label_x = start_x - 5 * mm
        c.drawRightString(label_x, y - 1 * mm, str(age))

    # Add age 90 on the right side only
    y_90 = start_y - (max_age * square_size) - (square_size / 2)
    label_x_right = start_x + grid_width + 5 * mm
    c.drawString(label_x_right, y_90 - 1 * mm, "90")

    # Add week labels on top (every 5 weeks)
    for week in range(0, weeks_per_year + 1, 5):
        if week == 0:
            week = 1
        x = start_x + (week - 1) * square_size + (square_size / 2)
        label_y = start_y + 2 * mm
        c.drawCentredString(x, label_y, str(week))

    # Add axis labels
    c.setFont("Helvetica-Bold", 9)
    c.drawString(margin + label_space_left / 4, start_y - (grid_height / 2), "Age")
    c.drawCentredString(start_x + grid_width / 2, start_y + 10 * mm, "Week of Year")

    # Add footer
    c.setFont("Helvetica", 8)
    footer_text = "Each box represents one week of your life. Black boxes are weeks you've lived."
    c.drawCentredString(page_width / 2, margin - 5 * mm, footer_text)

    # Save PDF
    c.save()


def main():
    """Main function to run the life calendar generator."""
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description='Generate a life calendar PDF showing your life in weeks.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Example: python life_calendar.py --birthdate 1990-05-15 --title "My Life Journey"'
    )
    parser.add_argument(
        '--birthdate',
        type=str,
        help='Your birthdate in YYYY-MM-DD format (e.g., 1990-05-15). If not provided, you will be prompted.'
    )
    parser.add_argument(
        '--title',
        type=str,
        default='A 90-Year Human Life in Weeks',
        help='Custom title for the calendar (default: "A 90-Year Human Life in Weeks")'
    )
    args = parser.parse_args()

    print("=" * 50)
    print("Life Calendar Generator")
    print("=" * 50)
    print()

    # Get birthdate from argument or prompt user
    if args.birthdate:
        try:
            birthdate = datetime.strptime(args.birthdate, "%Y-%m-%d").date()

            # Validate date is not in the future
            if birthdate > date.today():
                print("Error: Birthdate cannot be in the future.")
                sys.exit(1)

            # Validate date is reasonable (not before 1900)
            if birthdate.year < 1900:
                print("Error: Please enter a birthdate after 1900.")
                sys.exit(1)

        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD (e.g., 1990-05-15)")
            sys.exit(1)
    else:
        birthdate = get_birthdate()

    # Calculate weeks lived
    weeks_lived = calculate_weeks_lived(birthdate)
    total_weeks = 52 * 90
    percentage = (weeks_lived / total_weeks) * 100

    # Generate filename
    filename = f"life_calendar_{birthdate.strftime('%Y-%m-%d')}.pdf"

    # Create PDF
    print(f"\nGenerating your life calendar...")
    create_life_calendar_pdf(birthdate, weeks_lived, filename, title=args.title)

    # Success message
    print(f"✓ PDF saved as: {filename}")
    print(f"  You have lived {weeks_lived:,} weeks out of {total_weeks:,} possible weeks.")
    print(f"  That's {percentage:.1f}% of a 90-year life.")
    print()


if __name__ == "__main__":
    main()
