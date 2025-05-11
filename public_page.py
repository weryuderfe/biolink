import streamlit as st
import json
import os

st.set_page_config(page_title="Link Bio Page", layout="centered")

# Ambil username dari URL (query string)
query_params = st.experimental_get_query_params()
username = query_params.get("user", [None])[0]

if username is None:
    st.error("Username tidak ditemukan di URL. Contoh: ?user=johndoe")
else:
    file_path = f"saved_pages/{username}.json"
    if not os.path.exists(file_path):
        st.error("Halaman tidak ditemukan.")
    else:
        with open(file_path, "r") as f:
            data = json.load(f)
        
        st.title(data["title"])
        st.markdown(f"**@{data['username']}**")

        st.markdown("---")
        for link in data["links"]:
            st.markdown(f"🔗 [{link['label']}]({link['url']})")

