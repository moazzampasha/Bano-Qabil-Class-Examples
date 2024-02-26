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

# Streamlit UI
st.title("Currency Converter")

amount = st.number_input("Enter Your Amount ():", value=0.0, step=1.0)
currency = st.selectbox("Select Currency To Convert From ______To PKR:", options=["USD", "EUR", "GBP", "SAR", "INR", "AUD"])

if st.button("Convert"):
    result = convert_currency(amount, currency.lower())
    st.write(result)

# Adding a column on the right
st.write("")
st.write("Conversion Rates:")
st.write("1 USD = 279 PKR")
st.write("1 EUR = 301 PKR")
st.write("1 GBP = 348 PKR")
st.write("1 SAR = 73 PKR")
st.write("1 INR = 3.33 PKR")
st.write("1 AUD = 180 PKR")