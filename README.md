# Branch Predictor Accuracy Analysis

## Overview
This project contains Python scripts that analyze the accuracy of one-bit and two-bit branch predictors. The scripts generate sequences of branch outcomes, compute the prediction accuracies, and identify sequences where one predictor outperforms the other.

## Files Description

### 1. [branchpredictor_accuracy.py](file:///Users/dino/Downloads/ScriptsCoding/PythonPlayground/BranchPredictor/branchpredictor_accuracy.py#1%2C1-1%2C1)
This script allows the user to input a sequence of branch outcomes and calculates the accuracy of both one-bit and two-bit predictors for that sequence.

- **Functionality**:
  - Input a sequence of branch outcomes.
  - Calculate and display the accuracy of one-bit and two-bit predictors.

### 2. [branchpredictor_accuracy_loop.py](file:///Users/dino/Downloads/ScriptsCoding/PythonPlayground/BranchPredictor/branchpredictor_accuracy_loop.py#1%2C1-1%2C1)
This script finds the best sequences where the one-bit predictor has the highest accuracy advantage over the two-bit predictor for a given sequence length.

- **Functionality**:
  - Input the length of the sequence.
  - Generate all possible sequences of the given length.
  - Calculate the accuracy difference between the one-bit and two-bit predictors.
  - Identify and display sequences where the one-bit predictor has the maximum accuracy advantage.

### 3. [branchpredictor_accuracy_bestsequences.py](file:///Users/dino/Downloads/ScriptsCoding/PythonPlayground/BranchPredictor/branchpredictor_accuracy_bestsequences.py#1%2C1-1%2C1)
This script includes functions to find sequences favorable to one-bit predictors over two-bit predictors and vice versa. It also includes a plotting function to visualize the best sequences for each length.

- **Functionality**:
  - Generate all possible sequences for a range of lengths.
  - Calculate and compare the accuracies of one-bit and two-bit predictors.
  - Plot the best sequences for each length where the one-bit predictor outperforms the two-bit predictor.

## Usage

To run any of the scripts, navigate to the directory containing the script and run:
```bash
python <script_name>.py
```
Follow the prompts in the terminal to input the required information (sequence or sequence length).

## Dependencies
- Python 3.x
- Matplotlib (for `branchpredictor_accuracy_bestsequences.py`)

## Installation
Ensure Python and pip are installed, then install Matplotlib using pip if you intend to use `branchpredictor_accuracy_bestsequences.py`:
```bash
pip install matplotlib
```

## Contributing
Contributions to improve the accuracy calculations or extend the functionality of the predictors are welcome. Please ensure to maintain the existing code structure and follow the commenting style.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
