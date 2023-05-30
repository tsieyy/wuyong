
import streamlit as st
import tools

st.title('寝室选择')

# st.write("请输入你想要选择的寝室：")

num_ = st.number_input("请输入你想要选择的寝室：", format="%f")

if num_ and not 99 < num_ < 1000:
    st.warning('只能选择三位数的寝室号', icon="⚠️")


num = tools.get_3_random()

if num_ and 99 < num_ < 1000:
    st.success('你的寝室已经分配到：' + str(num), icon="✅")