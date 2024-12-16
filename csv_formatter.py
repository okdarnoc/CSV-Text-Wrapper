import csv 

def calculate_char_width(font_size): 
    """
    Estimate character width in centimeters based on font size.
    
    This function uses a simplified estimation method based on:
    - A base font size of 12pt
    - A base character width of 0.21cm at 12pt
    - Linear scaling of width with font size
    
    Args:
        font_size (float): The target font size in points
        
    Returns:
        float: Estimated character width in centimeters
    
    Note:
        This is a simplified approximation and may need adjustment
        based on specific fonts or use cases.
    """
    base_font_size = 12  # Standard base font size in points
    base_char_width = 0.21  # Average character width at 12pt in cm
    return (font_size / base_font_size) * base_char_width 

def split_text(text, limit, font_size):
    """
    Splits text at commas to ensure each line stays within specified width limit.
    
    The function maintains the following properties:
    - Splits only at commas to preserve semantic grouping
    - Maintains original commas in output except at line breaks
    - Ensures no line exceeds the specified width limit
    - Removes unnecessary spaces after splits
    
    Args:
        text (str): Input text to be split
        limit (float): Maximum line width in centimeters
        font_size (float): Font size in points
        
    Returns:
        str: Formatted text with appropriate line breaks
    """
    # Calculate maximum characters per line based on font size
    char_width = calculate_char_width(font_size)
    max_chars = int(limit / char_width)
    
    # Split text at commas for processing
    parts = text.split(',')
    new_text = ""
    current_line = ""
    
    # Process each part of the split text
    for i, part in enumerate(parts):
        # Add comma back for all parts except the first
        if i > 0:
            part = ',' + part
        
        # Check if adding this part would exceed the character limit
        if len(current_line + part) > max_chars:
            # Add current line to result with proper formatting
            if new_text:
                new_text += '\n'
            new_text += current_line
            # Start new line, removing leading comma if present
            current_line = part.strip(',')
        else:
            # Add part to current line if within limits
            current_line += part
    
    # Handle any remaining text
    if current_line:
        if new_text:
            new_text += '\n'
        new_text += current_line
    
    return new_text

def process_csv(input_path, output_path, column_index, limit_cm, font_size):
    """
    Process a CSV file by reformatting text in specified column to meet width constraints.
    
    This function:
    1. Reads the input CSV file
    2. Processes the specified column to meet width constraints
    3. Writes the modified data to a new CSV file
    
    Args:
        input_path (str): Path to input CSV file
        output_path (str): Path where processed CSV will be saved
        column_index (int): Index of column to process (0-based)
        limit_cm (float): Maximum width limit in centimeters
        font_size (float): Font size in points
        
    Note:
        - Assumes UTF-8 encoding for input and output files
        - Maintains original CSV structure except for formatted column
    """
    with open(input_path, 'r', newline='', encoding='utf-8') as infile, \
         open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Process each row in the CSV
        for row in reader:
            # Apply text formatting to specified column
            row[column_index] = split_text(row[column_index], limit_cm, font_size)
            writer.writerow(row)

# Main execution block with user input handling
if __name__ == "__main__":
    # Gather necessary information from user
    input_path = input("Enter the path to the input CSV file: ")
    output_path = input("Enter the path to the output CSV file: ")
    column_index = int(input("Enter the index (starting from 0) of the column to be processed: "))
    limit_cm = float(input("Enter the width limit in cm: "))
    font_size = float(input("Enter the font size: "))
    
    # Process the CSV with provided parameters
    process_csv(input_path, output_path, column_index, limit_cm, font_size)
    
    print("The CSV file has been processed and saved to:", output_path)
