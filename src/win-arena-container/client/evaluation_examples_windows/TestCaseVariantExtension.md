# Test Case Variant Extension

## Overview
This comprehensive guide outlines 4 methodologies for extending and customizing test case variants in Windows Arena testing scenarios. 

- Instruction-only modifications
- JSON-based result variations
- File-based result variations
- Python evaluator function customizations

The base test cases referenced in this documentation are derived from the [example test suite](./examples), which serves as the foundation for variant implementations.

For a more comprehensive summary of the test cases, please refer to this file: [extended_example_summary](./extended_example_summary.json)


## 1. Change Instruction Only

This method keeps test steps and expected results unchanged, only generating new instructions through AI inference.

### Example 1 (ID: 28b91a24-5d97-4c2a-891c-dccbd3820c62-WOS-3)

**Original Instruction:**

- *Use the calculator app, how many days are there between 13/01/2023 and 20/08/2024? Can you save the answer in 'numdays.txt' on the Desktop (e.g. X days)*

**Expected Result:**
Check if file "numdays.txt" with the content matches "585 days"

**Variant Instruction Examples:**
These variants use different dates but have the same expected result - outputting a text file with the calculation result "585 days".

- *Calculate the number of days between March 15, 2023 and October 31, 2023 using the calculator app, and save the result as 'numdays.txt' on the Desktop (e.g. X days)*
- *Using the calculator app, determine how many days are there from April 1, 2023 to November 17, 2023? Save your answer in a file named 'numdays.txt' on the Desktop in the format 'X days'*
- *Open the calculator and find out the number of days between May 20, 2023 and January 5, 2024. Save the result in a text file called 'numdays.txt' on the Desktop with the format 'X days'*
- *Use the calculator to count the days from June 10, 2023 to January 26, 2024, then save the answer as 'numdays.txt' on the Desktop in the format 'X days'*
- *With the calculator app, compute the number of days from February 1, 2023 to September 19, 2023, and save the result on the Desktop as 'numdays.txt' containing 'X days'*

### Example 2 (ID: 2ae9ba84-3a0d-4d4c-8338-3a1478dc5fe3-wos)

In most test cases, due to limitations in test steps and expected results, most variant cases only change the natural language description of the original instruction without changing the parameters within the instruction.

**Original Instruction:**

- *Lately I have changed my English name to Thomas. I want to update my username. Could you help me change the username in chrome profiles to Thomas?*

**Variant Instruction Examples:**

- *I need to update my Chrome profile name to Thomas - can you show me how?*
- *Hey, I want to change my name in Chrome to Thomas, could you help me do that?*
- *Can you guide me through updating my Chrome username to Thomas?*
- *I'd like to set my Chrome profile name as Thomas - how do I do that?*
- *Would you help me modify my Chrome browser profile name to Thomas?*

**Coverage:** This method can be used to extend all feasible test cases (142/151), [currently extended to 142*5=710 test cases](./examples_extendedByInstruction).

## 2. Change Instruction and Evaluator Result (JSON)

This method keeps test steps unchanged while generating new instructions and expected results in the evaluator JSON.

### Example (ID: 2ae9ba84-3a0d-4d4c-8338-3a1478dc5fe3-wos)

**Original Instruction:**

- *Lately I have changed my English name to Thomas. I want to update my username. Could you help me change the username in chrome profiles to Thomas?*

**Key Parameter for Expected Result:** ```Thomas```

**New Parameter Variants and Corresponding Instructions:**

Parameter ```William```:
- *I'd like to change my Chrome profile name to William since that's my preferred name now. Can you help me update it?*

Parameter ```Emma```:
- *I got married and want to update my Chrome profile name to Emma. Could you show me how to change it?*

Parameter ```Work Profile```:
- *I need to set up a separate Chrome profile for work. Can you help me change the profile name to 'Work Profile'?*

**Coverage:** 32/151 test cases are suitable for this method, [extended to 32*3=96 test cases](./examples_extendedByEvaluatorResult).

## 3. Change Instruction and Evaluator Result (File)

This method is suitable for test cases where the expected result is a specific file (xlsx, png, txt, etc.).

### Example (ID: 01b269ae-2111-4a07-81fd-3fcd711993b0-WOS)

**Original Instruction:**

- *Fill all the blank cells with the value in the cell above it*

**Expected Result:**
Check if file "Student_Level_Fill_Blank.xlsx" is the same as the file downloaded from cloud.

**Features:**
- Expected results involve file comparison
- Requires more manual operation and modification
- Currently lacks automated implementation solutions

**Coverage:** 69/151 test cases are suitable for this method.

## 4. Change Instruction and Evaluator Function (Python)

This method creates new variants by modifying parameters and logic in the evaluator function's Python code.

### Example (ID: 7c70e16b-e14f-4baa-b046-3e022b2d0305-WOS)

**Original Instruction:**
- *Sort files by date modified in the Documents folder.*

Its evaluator function is ```are_files_sorted_by_modified_time```. Here, we can modify the original evaluator function to expose the sort method as a parameter to the evaluator expected rule, enabling new variant test case extensions.

**Features:**
- Allows for more detailed and in-depth evaluator function modifications
- Supports customized extensions
- Requires higher development effort

**Coverage:** Theoretically, all test cases can be extended using this method, but it requires significant development investment. 