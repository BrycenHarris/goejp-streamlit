import streamlit as st
import geojp.foliumap as geojp

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://geojp-map.streamlit.app/Folium>
"""
 
st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Geojp Map")

with st.expander("See source code"):
    with st.echo():
        m = geojp.Map()
        m.add_basemap("OpenTopoMap")
        m.add_basemap("Esri.WorldImagery")
        m.add_layer_control()

m.to_streamlit(width=1000, height=700)
