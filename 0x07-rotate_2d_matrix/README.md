# 0x07-rotate_2d_matrix

## Description
This project is focused on rotating a 2D matrix in-place. The goal is to implement a function that rotates the matrix 90 degrees clockwise.

## Problem Statement
Given an n x n 2D matrix, rotate it 90 degrees clockwise. The function prototype is `def rotate_2d_matrix(matrix):`. The matrix must be edited in-place. You can assume the matrix will have 2 dimensions and will not be empty.

## Requirements
* Python 3.6 (or higher)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/addymwenda12/0x07-rotate_2d_matrix.git
    ```

2. Navigate to the project directory:
    ```bash
    cd 0x07-rotate_2d_matrix
    ```

## Usage
To use the rotate_2d_matrix function, import it from the rotate_2d_matrix module and pass in your 2D matrix as an argument. Here's an example:

```python
from rotate_2d_matrix import rotate_2d_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

## Testing
To run the tests for the rotate_2d_matrix function, use the following command:

```bash
python -m unittest test_rotate_2d_matrix.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)