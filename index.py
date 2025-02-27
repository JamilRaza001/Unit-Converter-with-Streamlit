import streamlit as st
from utils.conversion import ConvertArea, ConvertDigitalStorage, ConvertEnergy, ConvertFrequency, ConvertLength, ConvertSpeed, ConvertTemperature, ConvertTime, ConvertVolume, ConvertMass

# Custom CSS styling
st.markdown("""
<style>
    /* Main page styling */
    .stApp {
        background: rgb(177,125,249);
        background: -moz-linear-gradient(33deg, rgba(177,125,249,1) 0%, rgba(92,227,255,1) 100%);
        background: -webkit-linear-gradient(33deg, rgba(177,125,249,1) 0%, rgba(92,227,255,1) 100%);
        background: linear-gradient(33deg, rgba(177,125,249,1) 0%, rgba(92,227,255,1) 100%);
        filter: progid:DXImageTransform.Microsoft.gradient(startColorstr="#b17df9",endColorstr="#5ce3ff",GradientType=1);
    }
    
    /* Title styling with gradient text */
    .title-text {
       background: rgb(247,181,255);
       background: -moz-linear-gradient(33deg, rgba(247,181,255,1) 0%, rgba(255,189,128,1) 100%);
       background: -webkit-linear-gradient(33deg, rgba(247,181,255,1) 0%, rgba(255,189,128,1) 100%);
       background: linear-gradient(33deg, rgba(247,181,255,1) 0%, rgba(255,189,128,1) 100%);
       filter: progid:DXImageTransform.Microsoft.gradient(startColorstr="#f7b5ff",endColorstr="#ffbd80",GradientType=1);
        font-weight: 800 !important;
        text-align: center;
        font-size: 2.5em !important;
        margin-bottom: 30px !important;
    }
    
    /* Section headers with emoji and animation */
    .section-header {
        background: linear-gradient(45deg, #ffffff, #f8f9fa);
        padding: 15px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #4ECDC4;
        animation: slideIn 0.5s ease-in-out;
        color:rgb(3, 19, 18);
        font-weight: 600;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(45deg, #4ECDC4, #45B7AF) !important;
        color: white !important;
        border-radius: 25px !important;
        padding: 10px 25px !important;
        transition: all 0.3s ease !important;
        border: none !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Result display styling */
    .result-box {
        background: linear-gradient(45deg, #ffffff, #f8f9fa);
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #FF6B6B;
        animation: fadeIn 0.5s ease-in-out;
    }
    
    /* Animations */
    @keyframes slideIn {
        from { transform: translateX(-50px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: rgb(223,218,218);
        background: -moz-linear-gradient(33deg, rgba(223,218,218,1) 0%, rgba(255,125,151,1) 100%);
        background: -webkit-linear-gradient(33deg, rgba(223,218,218,1) 0%, rgba(255,125,151,1) 100%);
        background: linear-gradient(33deg, rgba(223,218,218,1) 0%, rgba(255,125,151,1) 100%);
        filter: progid:DXImageTransform.Microsoft.gradient(startColorstr="#dfdada",endColorstr="#ff7d97",GradientType=1); !important;
        box-shadow: 5px 0 15px rgba(0, 0, 0, 0.1) !important;
    }
    
    .sidebar-header {
        color: white  !important;
        font-size: 1.5em !important;
        padding-bottom: 10px !important;
        border-bottom: 2px solid white !important;
        font-weight: 800 !important;    
    }
</style>
""", unsafe_allow_html=True)

# Main title with emoji
st.markdown('<p class="title-text">🌍 Universal Unit Converter</p>', unsafe_allow_html=True)

# Sidebar with enhanced styling
with st.sidebar:
    st.markdown('<div class="sidebar-header">⚙️ Conversion Settings</div>', unsafe_allow_html=True)
    conversion_type = st.selectbox("Select Conversion Type", [
        "Length", "Weight", "Temperature", "Frequency", 
        "Speed", "Area", "Volume", "Digital Storage", 
        "Energy", "Time"
    ])

# Input value with improved styling
value = st.number_input("Enter the value to convert:", 
                       value=1.0, 
                       help="Enter the numerical value you want to convert")

# Conversion sections with emojis and animations


# Conversion sections with emojis and animations
result = None
conversion_emojis = {
    "Length": "📏",
    "Weight": "⚖️",
    "Temperature": "🌡️",
    "Frequency": "📡",
    "Speed": "🚀",
    "Area": "📐",
    "Volume": "🧪",
    "Digital Storage": "💾",
    "Energy": "⚡",
    "Time": "⏳"
}

if conversion_type == "Length":
    st.markdown(f'<div class="section-header">{conversion_emojis["Length"]} Length Conversion</div>', unsafe_allow_html=True)
    units = ["meters", "kilometers", "centimeters", "millimeters",
             "micrometers", "nanometers", "miles", "yards", "feet", "inches", "nauticalmiles"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit", units, key="LengthFrom")
    with col2:
        to_unit = st.selectbox("To Unit", units, key="LengthTo")
    if st.button("Convert Length", key="LengthConvert"):
        result = ConvertLength(value, from_unit, to_unit)

elif conversion_type == "Weight":
    st.markdown(f'<div class="section-header">{conversion_emojis["Weight"]} Weight Conversion</div>', unsafe_allow_html=True)
    units = ["tonne", "kilogram", "gram", "milligram", "microgram",
             "imperial ton", "US ton", "stone", "pound", "ounce"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit", units, key="mass_from")
    with col2:
        to_unit = st.selectbox("To Unit", units, key="mass_to")
    if st.button("Convert Weight", key="mass_convert"):
        result = ConvertMass(value, from_unit, to_unit)

elif conversion_type == "Temperature":
    st.markdown(f'<div class="section-header">{conversion_emojis["Temperature"]} Temperature Conversion</div>', unsafe_allow_html=True)
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit", units, key="temp_from")
    with col2:
        to_unit = st.selectbox("To Unit", units, key="temp_to")
    if st.button("Convert Temperature", key="temp_convert"):
        result = ConvertTemperature(value, from_unit, to_unit)

elif conversion_type == "Area":
    st.markdown(f'<div class="section-header">{conversion_emojis["Area"]} Area Conversion</div>', unsafe_allow_html=True)
    units = ["square meter", "square kilometer", "square mile", "square yard",
             "square foot", "square inch", "hectare", "acre"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit", units, key="area_from")
    with col2:
        to_unit = st.selectbox("To Unit", units, key="area_to")
    if st.button("Convert Area", key="area_convert"):
        result = ConvertArea(value, from_unit, to_unit)

elif conversion_type == "Volume":
    st.markdown(f'<div class="section-header">{conversion_emojis["Volume"]} Volume Conversion</div>', unsafe_allow_html=True)
    units = ["cubic meter", "liter", "milliliter", "cubic centimeter",
             "cubic inch", "cubic foot", "gallon"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit", units, key="volume_from")
    with col2:
        to_unit = st.selectbox("To Unit", units, key="volume_to")
    if st.button("Convert Volume", key="volume_convert"):
        result = ConvertVolume(value, from_unit, to_unit)

elif conversion_type == "Digital Storage":
    st.markdown(f'<div class="section-header">{conversion_emojis["Digital Storage"]} Digital Storage Conversion</div>', unsafe_allow_html=True)
    units = ["bit", "kilobit", "megabit", "gigabit", "terabit", "petabit",
             "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit", units, key="storage_from")
    with col2:
        to_unit = st.selectbox("To Unit", units, key="storage_to")
    if st.button("Convert Digital Storage", key="storage_convert"):
        result = ConvertDigitalStorage(value, from_unit, to_unit)

elif conversion_type == "Energy":
    st.markdown(f'<div class="section-header">{conversion_emojis["Energy"]} Energy Conversion</div>', unsafe_allow_html=True)
    units = ["joule", "kilojoule", "gram calorie", "kilocalorie", 
             "watt-hour", "kilowatt-hour", "electronvolt"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit", units, key="energy_from")
    with col2:
        to_unit = st.selectbox("To Unit", units, key="energy_to")
    if st.button("Convert Energy", key="energy_convert"):
        result = ConvertEnergy(value, from_unit, to_unit)

elif conversion_type == "Frequency":
    st.markdown(f'<div class="section-header">{conversion_emojis["Frequency"]} Frequency Conversion</div>', unsafe_allow_html=True)
    units = ["hertz", "kilohertz", "megahertz", "gigahertz"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit", units, key="freq_from")
    with col2:
        to_unit = st.selectbox("To Unit", units, key="freq_to")
    if st.button("Convert Frequency", key="freq_convert"):
        result = ConvertFrequency(value, from_unit, to_unit)

elif conversion_type == "Speed":
    st.markdown(f'<div class="section-header">{conversion_emojis["Speed"]} Speed Conversion</div>', unsafe_allow_html=True)
    units = ["meter per second", "kilometer per hour", "mile per hour", 
             "foot per second", "knot"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit", units, key="speed_from")
    with col2:
        to_unit = st.selectbox("To Unit", units, key="speed_to")
    if st.button("Convert Speed", key="speed_convert"):
        result = ConvertSpeed(value, from_unit, to_unit)

elif conversion_type == "Time":
    st.markdown(f'<div class="section-header">{conversion_emojis["Time"]} Time Conversion</div>', unsafe_allow_html=True)
    units = ["second", "minute", "hour", "day", "week"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit", units, key="time_from")
    with col2:
        to_unit = st.selectbox("To Unit", units, key="time_to")
    if st.button("Convert Time", key="time_convert"):
        result = ConvertTime(value, from_unit, to_unit)

# Display result with animation and styling
if result is not None:
    st.markdown(f"""
    <div class="result-box">
        <h3 style='color: #4ECDC4; margin:0;'>🎉 Conversion Result</h3>
        <p style='font-size: 1.2em; margin: 10px 0;'>
            {value} <strong>{from_unit}</strong> = 
            <span style='color: #FF6B6B; font-weight: 800;'>{result}</span> <strong>{to_unit}</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)