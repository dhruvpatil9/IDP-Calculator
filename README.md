# Intradiscal Pressure Calculator

Welcome to the Intradiscal Pressure Calculator! This Streamlit application helps you calculate the intradiscal pressure (IDP) based on your weight and angle inputs. The application provides graphical representations for different vertebrae locations and displays the results along with detailed calculations.

## Features

- **Calculate Intradiscal Pressure (IDP):** Input your weight and angle to calculate IDP based on selected vertebrae locations.
- **Visual Representation:** View images corresponding to different vertebrae locations.
- **Interactive Interface:** Enter values to see results and view underlying formulas.

## Files

- **`README.md`**: This file.
- **`requirements.txt`**: Contains the list of Python packages required to run the application.
- **`streamlit.py`**: The main Streamlit application script.
- **`1.png`, `2.png`, `3.png`**: Images showing different vertebrae locations (C2/C3, C4/C5, C6/C7).

## Getting Started

### Prerequisites

Make sure you have Python installed. You can install the required packages by running:

```bash
pip install -r requirements.txt
```

### Running the Application

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/dhruvpatil9/IDP-Calculator.git
    cd IDP-Calculator
    ```

2. **Navigate to the Application Directory:**

    Ensure you are in the directory where `streamlit.py` is located.

3. **Run the Streamlit Application:**

    ```bash
    streamlit run streamlit.py
    ```

    This will start the Streamlit server and open the application in your default web browser.

### User Input

- **Weight (in kgs):** Enter your weight (within the range of 0-150 kg).
- **Angle β (in degrees):** Enter the flexion/extension angle (within the range of -60 to +70 degrees).

### Options

Select one of the following vertebrae locations to view the corresponding image and calculations:

- **C2/C3**
- **C4/C5**
- **C6/C7**

### Output

The application will display:

- **Weight of Head \(F(head)\):** The weight of the head in Newtons.
- **Net Force on Disc:** The net force acting on the disc in Newtons.
- **Intradiscal Pressure (IDP):** The calculated intradiscal pressure in MPa.

### Formulae

The following formulas are used in the calculations:

- **Weight of Head:**

  <p><i>F(head) = F<sub>w</sub> × g × constant</i></p>

- **Net Force on Disc:**

  <p><i>F<sub>n</sub> = √(N<sub>r</sub><sup>2</sup> + T<sub>r</sub><sup>2</sup>)</i></p>

- **Intradiscal Pressure:**

  <p><i>IDP = F<sub>n</sub> / (Area × CF)</i></p>

  where CF is the correction factor (0.66).

## Troubleshooting

- **Invalid Input:** Ensure that numerical values for weight and angle are valid.
- **Errors in Display:** Verify that image files (`1.png`, `2.png`, `3.png`) are correctly placed in the directory.
