import streamlit as st
from PIL import Image

VERSION = "1.0.0"

# 页面配置
st.set_page_config(
    page_title="Yami-API",
    page_icon=Image.open("static/icon.png"),
    # default：centered,居中展示。 wide: 全屏展示
    layout="wide",
    # 侧边栏默认展示还是收缩
    initial_sidebar_state="expanded"
)

st.title(f":moneybag:**Yami**:red[API] {VERSION}")
sidebar = st.sidebar
with sidebar:
    st.image("static/theme_icon.png")
    st.divider()
    