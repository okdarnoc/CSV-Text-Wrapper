# CSV Text Formatter

A Python utility for processing CSV files by reformatting text in specified columns to meet width constraints. This tool is particularly useful when preparing data for fixed-width displays, reports, or other formatting-sensitive applications.

## Features

- Format text in CSV columns to meet specific width constraints
- Intelligent text splitting at comma positions
- Configurable font size support
- Preservation of data integrity and structure
- UTF-8 encoding support
- Clean line breaks without trailing spaces

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/csv-text-formatter.git
cd csv-text-formatter
```

2. No additional dependencies required - uses Python standard library only.

## Usage

### Command Line Interface

Run the script and follow the interactive prompts:

```bash
python csv_formatter.py
```

You will be asked to provide:
- Input CSV file path
- Output CSV file path
- Column index to process (0-based)
- Width limit in centimeters
- Font size in points

### As a Module

```python
from csv_formatter import process_csv

# Process a CSV file
process_csv(
    input_path='input.csv',
    output_path='output.csv',
    column_index=2,  # Process the third column (0-based index)
    limit_cm=10.0,   # 10 cm width limit
    font_size=12.0   # 12pt font size
)
```

## How It Works

1. **Character Width Calculation**: 
   - Estimates character width based on font size
   - Uses a base calculation of 0.21cm for 12pt font
   - Scales linearly with font size changes

2. **Text Splitting**:
   - Splits text only at comma positions
   - Ensures no line exceeds specified width
   - Maintains semantic grouping of text

3. **CSV Processing**:
   - Reads input CSV file
   - Applies formatting to specified column
   - Preserves all other data and structure
   - Writes to new CSV file

## Example

Input CSV:
```csv
ID,Name,Description
1,Product A,"Long description, with multiple, comma-separated, parts that need to be formatted"
```

Output CSV (with 10cm width limit):
```csv
ID,Name,Description
1,Product A,"Long description
with multiple, comma-separated
parts that need to be formatted"
```

## Limitations

- Character width calculation is a simplified approximation
- Only splits at comma positions
- Assumes monospace font characteristics
- May not account for all Unicode character widths
- No support for rich text formatting

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

- Your Name
- Contributors

## Acknowledgments

- Thanks to anyone whose code was used
- Inspiration
- etc

## Version History

- 1.0.0
    - Initial Release
    - Basic CSV processing functionality
    - Command line interface

## Future Improvements

- Add support for different fonts
- Implement more accurate character width calculations
- Add support for different text splitting strategies
- Include rich text formatting options
- Add batch processing capabilities
