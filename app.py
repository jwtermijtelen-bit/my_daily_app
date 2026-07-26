import streamlit as st
from modules.news import get_news
from modules.weather import get_weather
from modules.investments import get_investments
from modules.commodities import get_commodities
from modules.productivity import get_productivity_tips
from modules.reminders import get_reminders

st.set_page_config(page_title="JW Daily Dashboard", layout="wide")

st.title("JW Daily Dashboard")
st.write("Your personalised daily overview.")

# --- NEWS ---
st.header("News")
news_items = get_news()
for item in news_items:
    st.subheader(item["title"])
    st.write(item["summary"])
    st.write(f"[Read more]({item['url']})")

# --- WEATHER ---
st.header("Weather")
weather = get_weather()
st.write(f"Location: {weather['location']}")
st.write(f"Temperature: {weather['temperature']}°C")
st.write(f"Condition: {weather['condition']}")

# --- INVESTMENTS ---
st.header("Investments")
investments = get_investments()
for inv in investments:
    st.write(f"{inv['name']}: {inv['value']}")

# --- COMMODITIES ---
st.header("Commodities")
commodities = get_commodities()
for com in commodities:
    st.write(f"{com['name']}: {com['price']}")

# --- PRODUCTIVITY ---
st.header("Productivity Tips")
tips = get_productivity_tips()
for tip in tips:
    st.write(f"- {tip}")

# --- REMINDERS ---
st.header("Reminders")
reminders = get_reminders()
for r in reminders:
    st.write(f"- {r}")
