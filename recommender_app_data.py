import pandas as pd
  
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Preprocesamiento de datos y creacion de la matriz de similitud
# Carga el dataset
file = pd.read_csv('anime.csv')

# Limpieza de datos
file = file.reset_index()
file.head()

file.columns
# Caracteristicas combinadas
features = ['Rating Score','Number Votes','Studios','Synopsis', 'Tags', 'Episodes']

def combined_features(row):
    return str(row["Rating Score"])+" "+ str(row["Number Votes"])+" "+ str(row["Studios"])+" "+ str(row["Synopsis"])+" "+ str(row["Tags"])+" "+ str(row["Episodes"])

def get_index_from_title(title):
    return file[file["Name"] == title]["index"].values[0]
# archivo combined_features para cada fila en el archivo de datos
file["combined_feature"]=file.apply(combined_features,axis=1)
file["combined_feature"].head()

cv = CountVectorizer()
count_matrix=cv.fit_transform(file["combined_feature"])

cosine_sim = cosine_similarity(count_matrix)
# Funcion para obtener recomendaciones
import pickle

pickle.dump(file.to_dict(),open('animes_dict.pkl','wb'))
similarity=cosine_sim
pickle.dump(similarity,open('similarity.pkl','wb'))
#Comentarios