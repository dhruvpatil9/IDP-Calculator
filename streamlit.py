import streamlit as st
import math

# Function to calculate variables based on inputs
def calculate_variables(mass, angle, option):
    # Convert inputs to float
    mass = float(mass)
    angle = float(angle)
    
    angle_rad = math.radians(16.3 + angle)
    alpha_rad = math.radians(16.3)
    
    
   
    
    # Symbolic representation of net force on disc
    net_force_symbolic = r"F_n^2 = \sqrt{N_r^2 + T_r^2}"
    weight_head = r"F (head) = F_w * 9.8 * 0.0826"
    if(option == "C2/C3"):
        idp = r"IDP = F_n / (Area (C2/C3) * CF )"

        var1 = mass * 9.8 * 0.0826
        Fm = var1 * math.sin(angle_rad) * (13/6)
        Nr = Fm + var1 * math.cos(alpha_rad)
        Tr = var1 * math.sin(alpha_rad)
        nrsquare = Nr ** 2
        trsquare = Tr ** 2
        var2 = math.sqrt(nrsquare + trsquare)
        var3 = var2 / (1000000*0.000190 * 0.66)
        
    elif (option == "C4/C5"):
        idp = r"IDP = F_n / (Area (C4/C5) * CF )"

        var1 = mass * 9.8 * 0.0826
        Fm = var1 * math.sin(angle_rad) * (15/6)
        Nr = Fm + var1 * math.cos(alpha_rad)
        Tr = var1 * math.sin(alpha_rad)
        nrsquare = Nr ** 2
        trsquare = Tr ** 2
        var2 = math.sqrt(nrsquare + trsquare)
        var3 = var2 / (1000000*0.000240 * 0.66)
        
    else:
        idp = r"IDP = F_n / (Area (C6/C7) * CF )"

        var1 = mass * 9.8 * 0.0826
        Fm = var1 * math.sin(angle_rad) * (17/6)
        Nr = Fm + var1 * math.cos(alpha_rad)
        Tr = var1 * math.sin(alpha_rad)
        nrsquare = Nr ** 2
        trsquare = Tr ** 2
        var2 = math.sqrt(nrsquare + trsquare)
        var3 = var2 / (1000000*0.000460 * 0.66)
    
    var1 = round(var1, 3)
    var2 = round(var2, 3)
    var3 = round(var3, 3)

    return var1, var2, var3, net_force_symbolic,weight_head,idp

# Main function for Streamlit app
def main():
    # Set layout to fixed width
    st.set_page_config(layout="wide")
    
    st.title("Intradiscal Pressure Calculator")
    
    # Increase sidebar width
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            width: 300px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Sidebar for image display
    st.sidebar.title("Analytical Model")
    option = st.sidebar.radio("Select an option:", ["C2/C3", "C4/C5", "C6/C7"])
    
    # Display image based on user selection
    if option == "C2/C3":
        image_path = "1.png"
    elif option == "C4/C5":
        image_path = "2.png"
    else:
        image_path = "3.png"
    
    # Display image in half of the window
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image(image_path, width=700)
    
    # User inputs in the other half of the window
    with col2:
        # User inputs as text
        mass = st.text_input("Enter your Weight (in kgs) (0-150)", "75")
        angle = st.text_input("Enter flexion/extension angle β (in degrees) (-70 to +90)", "0")
        
        # Calculate variables
        try:
            var1, var2, var3, net_force_symbolic,weight_head,idp = calculate_variables(mass, angle,option)
            
            # Display calculated variables
            st.write(f"Weight of Head F(head): **{var1}** Newton")
            st.latex(f"{weight_head}")
            st.write(f"Net Force on disc: **{var2}** Newton")
            st.latex(f"{net_force_symbolic}")
            st.write(f"Intradiscal pressure: **{var3}** MPa")
            st.latex(f"{idp}")
            st.latex("CF = 0.66 (correction factor)")
        except ValueError:
            st.error("Please enter valid numerical values for mass and angle.")
main()
