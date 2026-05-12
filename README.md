# Cherry Me - Rush Assignments

This project contains 5 rush assignments that display squares on the terminal using character-based graphics.

## Project Structure

```
cherry_me/
├── rush.py              # Universal redirector for all assignments
├── rush1-1.py           # Redirector for assignment 1
├── rush1-2.py           # Redirector for assignment 2
├── rush1-3.py           # Redirector for assignment 3
├── rush1-4.py           # Redirector for assignment 4
├── rush1-5.py           # Redirector for assignment 5
├── README.md            # This file
└── pyTechTest.pdf       # Assignment specifications
```

## How to Run

### Option 1: Using the Universal Redirector (Recommended)
```bash
python3 rush.py <assignment> <width> <height>
```

**Examples:**
```bash
python3 rush.py 1 5 3    # Assignment 1, width=5, height=3
python3 rush.py 2 5 3    # Assignment 2, width=5, height=3
python3 rush.py 3 5 3    # Assignment 3, width=5, height=3
python3 rush.py 4 5 3    # Assignment 4, width=5, height=3
python3 rush.py 5 5 3    # Assignment 5, width=5, height=3
```

### Option 2: Using Direct Redirectors
```bash
python3 rush1-1.py <width> <height>
python3 rush1-2.py <width> <height>
python3 rush1-3.py <width> <height>
python3 rush1-4.py <width> <height>
python3 rush1-5.py <width> <height>
```

**Examples:**
```bash
python3 rush1-1.py 5 3    # Assignment 1, width=5, height=3
python3 rush1-5.py 4 4    # Assignment 5, width=4, height=4
```

## Assignment Examples

### Assignment 1 - Basic Square
```bash
python3 rush.py 1 5 3
```
Output:
```
o---o
|   |
o---o
```

### Assignment 2 - Diamond Square
```bash
python3 rush.py 2 5 3
```
Output:
```
/***\
*   *
\***/
```

### Assignment 3 - Letter Square (A/B/C)
```bash
python3 rush.py 3 5 3
```
Output:
```
ABBBA
B   B
CBBBC
```

### Assignment 4 - Letter Square (Different Pattern)
```bash
python3 rush.py 4 5 3
```
Output:
```
ABBBC
B   B
ABBBC
```

### Assignment 5 - Letter Square (Rotated)
```bash
python3 rush.py 5 5 3
```
Output:
```
ABBBC
B   B
CBBBA
```

## Error Handling

If you provide invalid parameters (size ≤ 0 or non-integer values), the program will print:
```
Invalid size
```

To stderr and exit with code 1.

## Requirements

- Python 3.x
- No external dependencies
