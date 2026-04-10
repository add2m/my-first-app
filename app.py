import streamlit as st

st.set_page_config(page_title="Customer Portal", layout="centered")

st.title("Welcome to Our Service")

if 'confirmed' not in st.session_state:
    st.session_state.confirmed = False

if not st.session_state.confirmed:
    st.header("Please enter your information")
    
    with st.form("user_form"):
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=1, max_value=100)
        address = st.text_input("Address")
        phone = st.text_input("Phone Number")
        email = st.text_input("Email Address")
        
        submit = st.form_submit_button("Submit")
        
        if submit:
            if name and address and phone and email:
                st.session_state.user_data = {
                    "Name": name, "Age": age, "Address": address, 
                    "Phone": phone, "Email": email
                }
                st.session_state.review = True
            else:
                st.error("Please fill in all fields.")

    if 'review' in st.session_state and st.session_state.review:
        st.write("---")
        st.subheader("Review Your Details")
        for key, value in st.session_state.user_data.items():
            st.write(f"**{key}:** {value}")
        
        col1, col2 = st.columns(2)
        if col1.button("Yes, I'm sure"):
            st.session_state.confirmed = True
            st.rerun()
        if col2.button("No, let me edit"):
            st.session_state.review = False
            st.rerun()

else:
    st.success("Information saved successfully!")
    st.subheader("How can we help you today?")
    
    choice = st.radio("Select an option:", ["Buy", "Contact Customer Service"])
    
    if st.button("Confirm Selection"):
        if choice == "Buy":
            st.info("Thank you! We will contact you within moments.")
            st.balloons() 
        else:
            st.info("Our team will contact you within 24 hours.")

    if st.button("Start Over"):
        st.session_state.confirmed = False
        st.rerun()

st.write("\n" * 3) 
st.markdown("<h3 style='text-align: center;'>❤️Thank you for your business❤️</h3>", unsafe_allow_html=True)


 