import streamlit as st
import pandas as pd
import numpy as np
import joblib
from category_encoders import TargetEncoder
from sklearn.preprocessing import StandardScaler
from catboost import CatBoostRegressor
import shap 
from streamlit_shap import st_shap
import streamlit.components.v1 as components


st.title('Previsão de valores de imóveis')

st.write("""
Esse APP visa predizer o valor de imóveis na cidade de Belo Horizonte,
tendo como ponto de partida informações de um imóvel. Preencha o campo
ao lado e veja abaixo o resultado e avaliação do mesmo a partir de gráficos.
""")

neighborhoods = joblib.load('fase3_deploy/neighborhoods.sav')
pipeline = joblib.load('fase3_deploy/pipeline.sav')
model = joblib.load('fase3_deploy/model.sav')

st.sidebar.subheader('Dados do imóvel em m2')
area_m2 = st.sidebar.number_input('Àrea do imóvel', min_value=0, value=100, step=10)
bedrooms = st.sidebar.number_input('Quantidade de quartos', min_value=0, value=3)
suites =  st.sidebar.number_input('Quantidade de suítes', min_value=0, value=0)
vacancies = st.sidebar.number_input('Quantidade de vagas na garagem', min_value=0, value=1)
bathrooms = st.sidebar.number_input('Quantidade de banheiros', min_value=0, value=2)
neighborhoods = st.sidebar.selectbox('Selecione o bairro do imóvel', neighborhoods)
target = st.sidebar.selectbox('Qual o objetivo', ['Compra', 'Venda'])

if st.sidebar.button('Previsão'):

    x_df = pd.DataFrame([[area_m2, bedrooms, suites, vacancies, bathrooms, neighborhoods]],
                       columns=['area_m2', 'bedrooms', 'suites', 'vacancies', 'bathrooms', 'neighborhoods'])
    x = pipeline.transform(x_df)
    predict = model.predict(x)

    st.write(f'O preço previsto do imóvel é R${predict[0]:.2f}')

    if target == 'Compra':
        st.success(f'O preço ideal para compra é R${(predict[0]*0.88):.2f}')
    else:
        st.success(f'O preço ideal para venda é R${(predict[0]*1.07):.2f}')
    
    x = pd.DataFrame(x, columns=['area_m2', 'quartos', 'suites', 'vagas', 'banheiro', 'bairro'])
    st.subheader('interpretação de resultado - Influência no preço')

    #shap.initjs()
    explainer = shap.TreeExplainer(model) 
    shap_values = explainer.shap_values(x)

    st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], x.iloc[0,:]), height=200, width=1000)
    st.write('Observação: Se não for possível ver todo o gráfico recolha a barra lateral')
    st.write("""
    O gráfico acima busca demonstrar como cada informação influencia no preço do imóvel,
    tanto para mais (cor vermelha) quanto para menos (cor azul). Outra informação que pode ser observada
    é a intensidade dessa influência a partir do tamanho da barra, quanto maior a barra mais forte
    foi o impacto no valor.
    """)
    
    st.subheader('interpretação de resultado - Influência geral')
    st_shap(shap.summary_plot(shap_values, x, plot_type='bar'))
    st.write("""
    Esse gráfico traz o impacto geral que cada informação teve sobre o preço previsto,
    desconsiderando se esse impacto foi para mais ou para menos.
    """)
