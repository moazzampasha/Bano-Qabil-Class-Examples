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

    return f"{amount} PKR = {converted_amount:.2f} {currency.upper()}"

# Streamlit UI
st.title("Currency Converter")

amount = st.number_input("Enter Your Amount (PKR):", value=0.0, step=1.0)
currency = st.selectbox("Select Currency To Convert To:", options=["USD", "EUR", "GBP", "SAR", "INR", "AUD"])

if st.button("Convert"):
    result = convert_currency(amount,currency.lower())
    st.write(result)



