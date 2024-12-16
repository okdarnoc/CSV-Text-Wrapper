#!/usr/bin/env python3

import csv
import sys
from typing import TextIO

def calculate_char_width(font_size: float) -> float:
    """Estimate character width in cm based on font size.
    
    Args:
        font_size: Font size in points
    
    Returns:
        Estimated character width in centimeters
    """
    base_font_size = 12  # Base font size for width estimation
    base_char_width = 0.21  # Base average character width in cm
    return (font_size / base_font_size) * base_char_width

def split_text(text: str, limit: float, font_size: float) -> str:
    """Split text at commas to fit within specified width limit.
    
    Args:
        text: Input text to be split
        limit: Maximum width in centimeters
        font_size: Font size in points
    
    Returns:
        Formatted text with appropriate line breaks
    """
    char_width = calculate_char_width(font_size)
    max_chars = int(limit / char_width)
    
    parts = text.split(',')
    new_text = ""
    current_line = ""
    
    for i, part in enumerate(parts):
        if i > 0:
            part = ',' + part  # Add comma back for all but first part
        
        # Check if adding this part exceeds max_chars
        if len(current_line + part) > max_chars:
            if new_text:
                new_text += '\n'
            new_text += current_line
            current_line = part.strip(',')  # Start new line without leading comma
        else:
            current_line += part
    
    # Add any remaining text
    if current_line:
        if new_text:
            new_text += '\n'
        new_text += current_line
    
    return new_text

def process_csv(input_path: str, output_path: str, column_index: int, 
                limit_cm: float, font_size: float) -> None:
    """Process a CSV file, reformatting specified column to meet width constraints.
    
    Args:
        input_path: Path to input CSV file
        output_path: Path for output CSV file
        column_index: Index of column to process (0-based)
        limit_cm: Maximum width in centimeters
        font_size: Font size in points
    
    Raises:
        FileNotFoundError: If input file doesn't exist
        IndexError: If column_index is out of range
        ValueError: If limit_cm or font_size is negative
    """
    if limit_cm <= 0 or font_size <= 0:
        raise ValueError("Width limit and font size must be positive")

    try:
        with open(input_path, 'r', newline='', encoding='utf-8', errors='ignore') as infile, \
             open(output_path, 'w', newline='', encoding='utf-8') as outfile:
            process_csv_files(infile, outfile, column_index, limit_cm, font_size)
    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found.", file=sys.stderr)
        sys.exit(1)

def process_csv_files(infile: TextIO, outfile: TextIO, column_index: int,
                     limit_cm: float, font_size: float) -> None:
    """Process CSV files using provided file handles.
    
    This function separates file I/O from the core processing logic.
    """
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    try:
        # Process header row first to validate column_index
        header = next(reader)
        if column_index >= len(header):
            raise IndexError(f"Column index {column_index} is out of range")
        writer.writerow(header)
        
        # Process remaining rows
        for row in reader:
            if column_index < len(row):  # Handle rows with fewer columns
                row[column_index] = split_text(row[column_index], limit_cm, font_size)
            writer.writerow(row)
    except IndexError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

def main():
    """Main function to handle user input and process the CSV file."""
    try:
        input_path = input("Enter the path to the input CSV file: ").strip()
        output_path = input("Enter the path to the output CSV file: ").strip()
        column_index = int(input("Enter the index (starting from 0) of the column to be processed: "))
        limit_cm = float(input("Enter the width limit in cm: "))
        font_size = float(input("Enter the font size: "))
        
        process_csv(input_path, output_path, column_index, limit_cm, font_size)
        print(f"Success: CSV file has been processed and saved to: {output_path}")
    
    except ValueError as e:
        print(f"Error: Invalid input - {str(e)}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
