import streamlit as st


def convert_currency(amount, currency):
    converted_amount = 0

    if currency == "usd":
        converted_amount = amount * 279
    elif currency == "eur":
        converted_amount = amount * 301
    elif currency == "gbp":
        converted_amount = amount * 348
    elif currency == "sar":
        converted_amount = amount * 73
    elif currency == "inr":
        converted_amount = amount * 3.33
    elif currency == "aud":
        converted_amount = amount * 180
    else:
        return "Currency not supported"

    return f"{amount} {currency.upper()} = {converted_amount:.2f} PKR"
st.write("# BANO QABIL CURRENCY CALCULATOR")
st.write("## Sir Ghuffran Kamal Python CIT Project")

# Streamlit UI
st.title("Currency Converter")

amount = st.number_input("Enter Your Amount ():", value=0.0, step=1.0)
currency = st.selectbox("Select Currency To Convert From ______To PKR:", options=["USD", "EUR", "GBP", "SAR", "INR", "AUD"])

if st.button("Convert"):
    result = convert_currency(amount, currency.lower())
    st.write(result)

# Adding a column on the right
st.text("")
st.text("Conversion Rates:")
st.text("1 USD = 279 PKR")
st.text("1 EUR = 301 PKR")
st.text("1 GBP = 348 PKR")
st.text("1 SAR = 73 PKR")
st.text("1 INR = 3.33 PKR")
st.text("1 AUD = 180 PKR")

def about_us_page():
    st.title("About Us Page")
    st.write("This is the About Us Page.")

def contact_us_page():
    st.title("Contact Us Page")
    st.write("You can contact us at contact@example.com.")

def main():
    st.sidebar.title("Menu")
    selection = st.sidebar.radio("Go to", ["Home", "About Us", "Contact Us"])
    if selection == "Home":
        home_page()
    elif selection == "About Us":
        about_us_page()
    elif selection == "Contact Us":
        contact_us_page()

    st.title("Display Image from GitHub")
    
    # URL of the image hosted on GitHub
    image_url = "https://github.com/moazzampasha/Bano-Qabil-Class-Examples/blob/main/logo.png"  # Update with your image URL
    
    st.image(image_url, caption='Image from GitHub', use_column_width=True)




if __name__ == "__main__":
    main()


