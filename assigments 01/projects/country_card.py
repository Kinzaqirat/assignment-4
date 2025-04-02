import streamlit as st
import requests

# Function to fetch country data
def get_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()[0]  # Extract the first match
    else:
        return None

# Streamlit UI
st.title("🌍 Country Information Card")

# User input
country_name = st.text_input("Enter a country name (e.g., Pakistan, France, Japan):")

if country_name:
    country_data = get_country_data(country_name)

    if country_data:
        # Extract details
        flag_url = country_data["flags"]["png"]
        name = country_data["name"]["common"]
        capital = country_data.get("capital", ["N/A"])[0]
        population = f"{country_data['population']:,}"  # Format with commas
        region = country_data["region"]
        currency = list(country_data["currencies"].keys())[0]
        currency_name = country_data["currencies"][currency]["name"]
        languages = ", ".join(country_data["languages"].values())

        # Display information
        st.image(flag_url, width=200)
        st.subheader(name)
        st.write(f"**Capital:** {capital}")
        st.write(f"**Population:** {population}")
        st.write(f"**Region:** {region}")
        st.write(f"**Currency:** {currency} ({currency_name})")
        st.write(f"**Languages:** {languages}")

    else:
        st.error("⚠️ Country not found! Please check the name and try again.")
