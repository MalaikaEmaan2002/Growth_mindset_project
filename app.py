import streamlit as st

# Set page config
st.set_page_config(page_title="Growth Mindset Project")

# Apply custom CSS for background gradient and styles
st.markdown(
    """
    <style>
    .body {
        color: linear-gradient(135deg, #ff69b4, #98fb98);  
    }
    
    .hr {
        border: none;
        height: 8px;
        background: linear-gradient(to right, #ff69b4 50%, #32cd32 50%);
        margin-top: 10px;
        margin-bottom: 10px;
        font-weight: bold;
    }
    
    .title {
        font-size: 36px;
        font-weight: bold;
        background: linear-gradient(to right, #ff69b4 50%, #98fb98 50%);
        -webkit-background-clip: text;
        color: transparent;
        font-style: italic;
    }

    /* Center the footer text */
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 16px;
        color: #555;
        font-size: 20px
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add growth icon next to title and make the title italicized
st.markdown(
    """
    <div style="display: flex; align-items: center;">
        <div class="title"> ⚡ Growth Mindset Project With Streamlit</div>
    </div>
    """, unsafe_allow_html=True)

# Header
st.header("🚀 **_Welcome To Growth Journey!_**")

# Custom bold horizontal line with green and pink colors
st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

st.write("Providing interactive exercises, motivational content, and progress tracking tools to foster personal development and embrace challenges as opportunities for growth.")

# Quote section
st.header("✯ **_Growth Mindset Quote_**")
st.write('***_"Your ability to learn is not fixed, it grows with your effort." – Carol Dweck_***')

st.header(" 💪 What's your challenge today?")
user_input = st.text_input("***Describe a challenge you're facing:***")

# condition
if user_input:
    st.success(f"You're facing: **{user_input}**. Keep pushing forward toward your goal! 💗")
else:
    st.warning("Tell us about your challenge!")

# Reflexing
st.header("_🤞 Outcome On Your Learning!_")
reflection = st.text_area("**Write your outcome here:**") 

if reflection:
    st.success(f" ☆ Great ! Your outcome :{reflection}")
else:
    st.info("Reflection on your past experience helps you grow! Share your difficulties.")

# Achievement
st.header("_🏆 Celebrate Your Objective Met._")
achievement = st.text_input("**Share something you have recently accomplished**")

if achievement:
    st.success(f" ✯ Awesome! You achieved :{achievement}")
else:
    st.info(" ❤️️ Stay focused, keep pushing forward, and success will follow.")

# Footer - Centered
st.markdown(
    """
    <div class="footer">
        ⭐Keep believing in yourself. Growth is a journey, not a destination 🔥<br>
        ❦ Created by Malaika Emaan
    </div>
    """, unsafe_allow_html=True
)

