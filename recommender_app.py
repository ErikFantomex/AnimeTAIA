# Modules
import streamlit as st
import pandas as pd
import pickle
from PIL import Image

#C:\Users\lokil\Desktop\Recomendadoranime\recommender_app.py
#Vamos
animes_dict = pickle.load(open('animes_dict.pkl','rb'))
animes = pd.DataFrame(animes_dict)
@st.cache() # streamlit que cuando se llama a una función, necesita verificar algunas cosas
def recommend(anime): # Funcion Principal
    # USa el pkl archivo que contiene el conjunto de datos limpio para el algoritmo
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    index = animes[animes["Name"] == anime]["index"].values[0]
    # Enumarate permite que pasemos por una lista de elementos mientras mantenemos el valor del índice en una variable separada
    # lambda crea una función anónima en línea
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    # Lista vacia para almacenar datos filtrados basados en la entrada del usuario
    recommended_anime_names = []
    recommended_anime_summary = []
    recommended_anime_startYear = []
    recommended_anime_endYear = []
    recommended_anime_finished = []
    recommended_anime_episodes = []
    recommended_anime_type = []
    recommended_anime_studios = []
    recommended_anime_tags = []
    for i in distances[1:6]:
        # Adjunta el resultado filtrado a las listas vacías
        recommended_anime_names.append(animes.iloc[i[0]].Name)
        recommended_anime_summary.append(animes.iloc[i[0]].Synopsis)
        recommended_anime_finished.append(animes.iloc[i[0]].Finished)
        recommended_anime_startYear.append(animes.iloc[i[0]].StartYear)
        recommended_anime_endYear.append(animes.iloc[i[0]].EndYear)
        recommended_anime_episodes.append(animes.iloc[i[0]].Episodes)
        recommended_anime_type.append(animes.iloc[i[0]].Type)
        recommended_anime_studios.append(animes.iloc[i[0]].Studios)
        recommended_anime_tags.append(animes.iloc[i[0]].Tags)

    return recommended_anime_names,recommended_anime_summary,recommended_anime_finished,recommended_anime_startYear,recommended_anime_endYear,recommended_anime_episodes,recommended_anime_type,recommended_anime_studios,recommended_anime_tags


# Cualquier cosa con "st." actúa como una etiqueta HTML que muestra títulos, texto, imagen, etc.
# Titulos  y subtitulos
st.title('Recommendador de Anime')
st.caption('Por Horacio Araiza Gonzalez')
st.write('Este es un recomendador de anime ')
# Anime image

image = Image.open('./Imagen.jpg') 
st.image(image, use_column_width=True)
#Selecciona caja
selected_anime = st.selectbox(
'Entonces ¿qué anime te gustó?',
(animes['Name'].values))
# A gimmick para decirle al usuario que las sugerencias se basarán en su entrada
st.write('La recomendacion estara basada en::',selected_anime)


if st.button('Recommendar'):
    # Pantaalla de carga
    with st.spinner(text='En progreso'):
         recommendations,summary,finished,startYear,endYear,episodes,type,studios,tags = recommend(selected_anime)
         # Output
         for i in range(5): 
             st.title(f"{i+1})"+"Titulo  :  "+str(recommendations[i]))
             st.write("Descripcion  : ")
             st.write(str(summary[i]))
             st.write("Tipo : "+str(type[i]))
             st.write("Finalizo: "+str(finished[i]))
             st.write("Inicio  / Año Final  : "+str(startYear[i])+ " - " +str(endYear[i]))
             st.write("Episodios : "+str(episodes[i]))
             st.write("Estudio(s) : "+str(studios[i]))
             st.write("Etiquetas:  "+str(tags[i]))


