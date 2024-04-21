import streamlit as st
import math

st.set_page_config(
  page_title="Σ IDP",
  page_icon = '☠',
  layout="wide"
)



# Function to calculate variables based on inputs
def calculate_variables(mass, angle, option):
    # Convert inputs to float
    mass = float(mass)
    angle = float(angle)
    
    angle_rad = math.radians(abs(13.9 + angle) )
    alpha_rad = math.radians(13.9)
    
    
   
    
    # Symbolic representation of net force on disc
    net_force_symbolic = r"F_n = \sqrt{N_r^2 + T_r^2}"
    if(option == "C2/C3"):
        idp = r"IDP = F_n / (Area (C2/C3) * CF )"
        weight_head = r"F (head) = F_w * 9.8 * 0.08"

        var1 = mass * 9.8 * 0.08
        Fm = var1 * ((math.sin(angle_rad) * 5) + 1.5)/6
        Nr = Fm + var1 * math.cos(alpha_rad)
        Tr = var1 * math.sin(alpha_rad)
        nrsquare = Nr ** 2
        trsquare = Tr ** 2
        var2 = math.sqrt(nrsquare + trsquare)
        var3 = var2 / (1000000*0.000190 * 0.66)
        
    elif (option == "C4/C5"):
        idp = r"IDP = F_n / (Area (C4/C5) * CF )"
        weight_head = r"F (head) = F_w * 9.8 * 0.082"

        var1 = mass * 9.8 * 0.082
        Fm = var1 * ((math.sin(angle_rad) * 7) + 1.5)/6
        Nr = Fm + var1 * math.cos(alpha_rad)
        Tr = var1 * math.sin(alpha_rad)
        nrsquare = Nr ** 2
        trsquare = Tr ** 2
        var2 = math.sqrt(nrsquare + trsquare)
        var3 = var2 / (1000000*0.000240 * 0.66)
        
    else:
        idp = r"IDP = F_n / (Area (C6/C7) * CF )"
        weight_head = r"F (head) = F_w * 9.8 * 0.084"

        var1 = mass * 9.8 * 0.084
        Fm = var1 * ((math.sin(angle_rad) * 9) + 1.5)/6
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

if 'evaluate_now' not in st.session_state:
    st.session_state['evaluate_now'] = False

# Main function for Streamlit app
def main(): 
    
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
        st.title("Intradiscal Pressure Calculator")
        st.image(image_path, width=600)
    
    # User inputs in the other half of the window
    with col2:
        # User inputs as text
        mass = st.text_input("Enter your Weight (in kgs) (0-150)", "75")
        angle = st.text_input("Enter flexion/extension angle β (in degrees) (-60 to +70)", "0")
        def evaluate_trigger():
            st.session_state['evaluate_now'] = True

        st.button("Evaluate",on_click = evaluate_trigger)
        
        # Calculate variables
        try:
            var1, var2, var3, net_force_symbolic,weight_head,idp = calculate_variables(mass, angle,option)
            
            # Display calculated variables
            st.divider()
            if st.session_state['evaluate_now']:
                # st.markdown(f" :gray[Weight of Head F(head):] :rainbow[{var1}] :gray[Newton]")
                st.markdown(f"""
<p><span style="color: gray;">Weight of Head F(head): </span><span style="color: orange; font-weight: bold; font-size: 2em;">{var1}</span> <span style="color: gray;">Newton</span></p>
""", unsafe_allow_html=True)
                
                st.markdown(f"""
<p><span style="color: gray;">Net Force on disc: </span><span style="color: orange; font-weight: bold; font-size: 2em;">{var2}</span> <span style="color: gray;">Newton</span></p>
""", unsafe_allow_html=True)
                st.markdown(f"""
<p><span style="color: gray;">Intradiscal pressure: </span><span style="color: orange; font-weight: bold; font-size: 2em;">{var3}</span> <span style="color: gray;">MPa</span></p>
""", unsafe_allow_html=True)
                # st.write(f" :gray[] :rainbow[{var2}] :gray[Newton]")
                # st.write(f" :gray[Intradiscal pressure (IDP):] :rainbow[{var3}] :gray[MPa]")
                st.session_state['evaluate_now'] = False
                st.toast("Success")
            else:
                st.caption("Click on Evaluate button 👆")

                

            st.divider()
            with st.popover("Show Formula"):
                st.latex(f"{weight_head}")
                st.latex(f"{net_force_symbolic}")
                st.latex(f"{idp}")
                st.latex("CF = 0.66 (correction factor)")
        except ValueError:
            st.error("Please enter valid numerical values for mass and angle.")
if __name__ == "__main__":
    main()
