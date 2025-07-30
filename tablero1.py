import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Nombre en la pestaña
st.set_page_config(layout='centered',
                   page_title='Talento Teach',
                   page_icon=':smile:')
# Título de la página
t1, t2 =st.columns([0.3,0.7])
t1.image('descarga.jfif',width=200)
t2.title('Mi Primer Tablero')
t2.markdown('**tel:** 123 **| email:** andresvillabon2000@gmail.com')
#Secciones
steps= st.tabs(['Pestaña', 'Pestaña 2', 'Pestaña  $\sqrt{9}$'])
with steps[0]:
    camp_df=pd.read_csv('Campanhas.csv', encoding='latin-1', sep=';')
    camp=st.selectbox('Escoge un ID de camaña',
                      camp_df['ID_Campana'] ,
                        help='Muestra las campañas existente')
    met_df=pd.read_csv('Metricas.csv', encoding='latin-1', sep=';')
    #st.dataframe(met_df)
    m1, m2, m3 =st.columns([1,1,1])

    id1=met_df[(met_df['ID_Campana']== camp)]
    m1.write('Métricas filtradas')
    m1.metric(label= 'Métrica 1', value=sum(id1['Conversiones']),
                  delta=str(sum(id1['Rebotes']))+' Total de Rebotes', 
                  delta_color='inverse')
    m2.metric(label= 'Métrica 2', value=np.mean(id1['Clics']),
        delta=str(np.mean(id1['Impresiones']))+' promedios',
               delta_color='inverse')
    
