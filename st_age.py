import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title('연령별 인구 조사')
st.write('지역의 연령별 인구를 조사합니다')
loc = st.text_input('조사할 지역명을 입력하시오')

#loc = input('조사할 지역명: ')
#loc = '범계'

data = pd.read_csv('202507.csv', encoding = 'cp949', thousands = ',')
if loc:
    con = data['행정구역'].str.contains(loc)
    home = data[con].copy()
    st.write(home)
    home.columns = home.columns.str.replace('2025년07월_계_', '')
    home.columns = home.columns.str.replace('세', '')
    home.columns = home.columns.str.replace(' 이상', '')

    if not home.empty:
        home = home.iloc[:, 3:].T
        home.columns = ["population"]

        st.write('해당 지역 데이터')
        st.write(home)

        fig, ax = plt.subplots()
        ax.plot(range(0,101),home['population'], marker = 'o')
        ax.set_title('age')
        ax.set_xlabel('age')
        ax.set_ylabel('num')
        ax.tick_params(axis = 'x', rotation = 90, length = 10)

        st.pyplot(fig)

        fig, ax = plt.subplots(2, 1)
        ax[0].bar(range(0,101),home['population'])
        ax[0].set_title('bar')
        ax[1].barh(range(0,101),home['population'])
        ax[1].set_title('barh')

        st.pyplot(fig)
    else:
        st.warning('해당 이름을 포함한 행정구역이 없습니다')