# Steel Beam Analysis for ISO 834 Standard Fire

## Purpose
The following Python script generates a three-dimensional steel beam model in the Abaqus finite element (FE) environment, subjected to the ISO 834 standard fire conditions. The script facilitates the creation and submission of a job for analysis, providing temperature readings at predefined thermocouple locations. Additionally, it allows users to specify mesh size and steel beam section dimensions for parametric study purposes.

## Code Overview
The Python script utilizes Abaqus modules to perform the following tasks:
- Define input data such as beam dimensions, fire duration, and mesh size.
- Create a three-dimensional steel beam model based on the specified dimensions.
- Set up datum planes for partitioning the model.
- Assign material properties to the steel beam.
- Create a heat transfer step for simulating the ISO 834 fire conditions.
- Define the temperature-time relationship for the fire simulation.
- Generate mesh for the model with user-specified mesh size.
- Locate thermocouple points for temperature monitoring during analysis.
- Request history output for thermocouple points to track temperature variations.

## Usage
1. Open the Python script in an Abaqus/CAE environment or execute it using the Abaqus command line interface.
2. Specify input data such as beam dimensions, fire duration, and mesh size.
3. Run the script to create the steel beam model and submit it for analysis.
4. After analysis completion, retrieve temperature readings at thermocouple locations for further analysis or visualization.

## Dependencies
- Abaqus/CAE software environment
- Python with Abaqus libraries installed

## Example
```python
# Python code snippet demonstrating script usage
from part import *
from material import *
# Import other required Abaqus modules

# Define input data
h = 300
b = 300
w = 11
f = 19
L = 4400
T = 2100
m = 10

# Execute the script to generate steel beam model and simulate ISO 834 fire
# (Remaining code not shown for brevity)

Feel free to customize this `README.md` template according to your preferences and additional information about your script.

