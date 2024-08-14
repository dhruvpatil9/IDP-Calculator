Intradiscal Pressure Calculator

Welcome to the Intradiscal Pressure Calculator! This application, built with Streamlit, helps calculate the intradiscal pressure (IDP) based on user inputs such as weight and angle. It provides graphical representation for different vertebrae locations and displays the results of the calculations.

## Features

- **Calculate Intradiscal Pressure (IDP):** Enter your weight and angle to calculate IDP based on selected vertebrae location.
- **Visual Representation:** View images for different vertebrae locations to understand the context of the calculations.
- **Interactive Interface:** Input values and instantly see the results along with the underlying formulas.

## Getting Started

### Prerequisites

Ensure you have Python installed along with the necessary packages. You can install the required packages using `pip`:

```bash
pip install streamlit
```

### Running the Application

1. **Clone the Repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Navigate to the Application Directory:**

    Ensure you are in the directory where `app.py` is located.

3. **Run the Streamlit Application:**

    ```bash
    streamlit run app.py
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
  - \( F(head) = F_w \times g \times \text{constant} \)
  
- **Net Force on Disc:**
  - \( F_n = \sqrt{N_r^2 + T_r^2} \)

- **Intradiscal Pressure:**
  - \( IDP = \frac{F_n}{\text{Area} \times CF} \)

  where \( CF \) is the correction factor (0.66).

## Files

- **`app.py`:** The main application script.
- **`1.png`, `2.png`, `3.png`:** Images showing different vertebrae locations (C2/C3, C4/C5, C6/C7).

## Troubleshooting

- **Invalid Input:** Ensure that numerical values for weight and angle are valid.
- **Errors in Display:** Check the image file paths and ensure they are correctly placed in the directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify the README to better fit your needs or project specifics!
