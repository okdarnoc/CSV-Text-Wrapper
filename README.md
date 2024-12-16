# CSV Text Formatter

A robust Python utility for reformatting text in CSV columns to meet specific width constraints. Perfect for preparing data for fixed-width displays, reports, or any situation requiring controlled text formatting.

## Features

- Format CSV columns to precise width specifications
- Smart text splitting at comma positions
- Configurable font size support
- Robust error handling for file and data issues
- UTF-8 encoding support with fallback options
- Type hints for better code maintainability

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/csv-text-formatter.git
cd csv-text-formatter

# Run the formatter
python csv_formatter.py
```

## Usage

### Command Line

Run the script and follow the prompts:

```bash
$ python csv_formatter.py
Enter the path to the input CSV file: input.csv
Enter the path to the output CSV file: output.csv
Enter the index (starting from 0) of the column to be processed: 2
Enter the width limit in cm: 10
Enter the font size: 12
```

### As a Module

```python
from csv_formatter import process_csv

# Basic usage
process_csv(
    input_path='input.csv',
    output_path='output.csv',
    column_index=2,
    limit_cm=10.0,
    font_size=12.0
)

# Advanced usage with error handling
try:
    process_csv('input.csv', 'output.csv', 2, 10.0, 12.0)
except FileNotFoundError:
    print("Input file not found")
except IndexError:
    print("Invalid column index")
except ValueError:
    print("Invalid width or font size")
```

## Input/Output Example

Input CSV:
```csv
ID,Product,Description
1,Laptop,"High-performance laptop, with 16GB RAM, 512GB SSD, dedicated graphics"
```

Output CSV (10cm width limit):
```csv
ID,Product,Description
1,Laptop,"High-performance laptop
with 16GB RAM
512GB SSD
dedicated graphics"
```

## Error Handling

The script handles common errors:
- Missing input files
- Invalid column indices
- Malformed CSV data
- Invalid width/font parameters
- Encoding issues (with fallback)

## Technical Details

### Character Width Calculation

The formatter uses a simplified model for character width:
- Base width: 0.21cm at 12pt font
- Linear scaling with font size
- Assumes monospace-like characteristics

### Text Splitting Strategy

- Splits only at comma positions to maintain data integrity
- Ensures no line exceeds specified width
- Preserves original commas except at line breaks
- Removes extra spaces after splits

## Requirements

- Python 3.6+
- No external dependencies

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Future Improvements

- [ ] Add support for custom delimiter characters
- [ ] Implement more sophisticated character width calculations
- [ ] Add support for different text splitting strategies
- [ ] Include configuration file support
- [ ] Add command line arguments parser
- [ ] Create automated tests

## Acknowledgments

- Inspired by the need for precise text formatting in data processing
- Thanks to all contributors and users for their feedback and suggestions
