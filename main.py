import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

'Start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)


left_column, right_column = st.columns(2)
left_column.button('右カラムに文字表示')
if st.button:
    right_column.write('ここは右カラム')
    


option = st.sidebar.text_input('あなたの趣味')
'趣味は', option, 'です'

condition = st.sidebar.slider('slider', 0, 100, 50)
'condition = ', condition

option = st.selectbox(
    'あなたが好きな数字',
    list(range(1,11))
)

'あなたの選んだ数字は、', option, 'です'

# st.write("Display Image")
# if st.checkbox('Show Image'):

#     img = Image.open('image.png')
#     st.image(img, caption='Icon', use_column_width=False)


df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

df_map = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df_map)

st.write(df)

st.dataframe(df.style.highlight_max(axis=0), width=400, height=400)
# width, hieght が指定できる

