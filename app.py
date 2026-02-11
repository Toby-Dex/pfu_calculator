import streamlit as st

# Page config
st.set_page_config(
    page_title="PFU Titer Calculator",
    page_icon="🦠",
    layout="centered"
)

# Title and description
st.title("PFU Titer Calculator")
st.markdown("Calculate viral titers from plaque assays with automatic countability checks")

# Input section
st.header("Input Data")

col1, col2, col3 = st.columns(3)

with col1:
    plaques = st.number_input(
        "Plaques Counted",
        min_value=0,
        value=50,
        step=1,
        help="Number of plaques counted on the plate"
    )

with col2:
    # Create dilution options from 10^-1 to 10^-9
    dilution_options = {
        "10⁻¹ (0.1)": 10,
        "10⁻² (0.01)": 100,
        "10⁻³ (0.001)": 1000,
        "10⁻⁴": 10000,
        "10⁻⁵": 100000,
        "10⁻⁶": 1000000,
        "10⁻⁷": 10000000,
        "10⁻⁸": 100000000,
        "10⁻⁹": 1000000000
    }
    
    dilution_label = st.selectbox(
        "Dilution Factor",
        options=list(dilution_options.keys()),
        index=5,  # Default to 10^-6
        help="Select the dilution used for plating"
    )
    
    dilution = dilution_options[dilution_label]

with col3:
    volume = st.number_input(
        "Volume Plated (µL)",
        min_value=1.0,
        value=100.0,
        step=10.0,
        help="Volume of inoculum plated"
    )

# Calculate button
if st.button("Calculate PFU/mL", type="primary"):
    # Convert µL to mL
    volume_ml = volume / 1000
    
    # Calculate PFU/mL
    pfu_ml = (plaques * dilution) / volume_ml
    
    # Countability check
    st.header("Results")
    
    if plaques < 30:
        st.warning(f"⚠️ Plaque count ({plaques}) is below 30 - results may lack statistical reliability")
    elif plaques > 300:
        st.warning(f"⚠️ Plaque count ({plaques}) is above 300 - plate may be too confluent for accurate counting, so flag as TOO MANY TOO COUNT")
    else:
        st.success("✅ Plaque count is within optimal range (30-300)")
    
    # Display result with proper scientific notation and dark green color
    # Convert to scientific notation format
    import math
    if pfu_ml > 0:
        exponent = int(math.floor(math.log10(pfu_ml)))
        mantissa = pfu_ml / (10 ** exponent)
        titer_display = f"{mantissa:.2f} × 10^{exponent} PFU/mL"
    else:
        titer_display = "0 PFU/mL"
    
    st.markdown(f"### Viral Titer")
    st.markdown(f"<h2 style='color: #006400; margin-top: -10px;'>{titer_display}</h2>", unsafe_allow_html=True)
    
    # Methods section
    st.header("Methods Section")
    
    # Calculate the exponent for better methods text
    import math
    if dilution > 1:
        exponent = int(math.log10(dilution))
    else:
        exponent = 0
    
    methods_text = f"""Viral titers were determined by plaque assay. Serial dilutions of virus stocks were prepared and {volume:.0f} µL of the 10^-{exponent} dilution was plated onto confluent cell monolayers. Plates were incubated until plaques were visible, fixed, and stained. Plaques were manually counted ({plaques} plaques) and titers were calculated as {pfu_ml:.2e} PFU/mL."""
    
    st.text_area("Copy for your methods:", methods_text, height=150)
    
# Footer
st.markdown("---")
st.markdown("*Developed for streamlining virology workflows*")
