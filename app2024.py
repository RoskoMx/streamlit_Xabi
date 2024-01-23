"""!pip install streamlit -q
!pip install streamlit-lottie
!pip install Pillow


%%writefile app.py Esto se hace cuasndo estamos usando Colab"""

!pip intsall streamlit_lottie

import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


#Funcion para generar nuestra animacion. La podemos sacar de lottiefile.com
def load_lottieurl(url): #Nombre y parámetro
  r = requests.get(url) #Guardamos la url
  if r.status_code != 200: #Si la solicitu de la animación no está disponible
    return None
  return r.json() #En caso contrario. Función que mandamos a llamar más abajo

#Creamos dos variables una para la imagen y otra para la animación
lottie_coding = load_lottieurl("https://lottie.host/715c7d3a-9133-4bb0-a617-0a4693f610c9/GdFoQ9wiAi.json")
imagen_video = Image.open("rosko.jpg") #Pon la ruta de tu imagen

with st.container():
  st.subheader("Hola bienvenido a mi sitio web dentro de una función :wave:")
  st.title("Información random de contacto")
  st.write("Bienvenido a mi canal. Mi canal de Youtube está destinado a compartir música que aparece en películas y series del mundo.")
  st.write("[Mas informacion >](https://www.youtube.com/channel/UCAd74yI_c0q9b7UA1KLBqMA")

with st.container():
  st.write("---") #Separa la primer sección de la segunda
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("Mi objetivo")
    st.write(
      """
        Como esto es un texto más grande vamos a escribir entre comillas triples
        con saltos de línea y todo lo va a tomar como un string
        Veremos si lo centra o lo pone desrodenado.
      """
    )
    st.write("[Youtube >](https://www.youtube.com/watch?v=_vnF1nYcUys)")
  
  with right_column: #Aquí tiene que aparecer la animación lottie
    st_lottie(lottie_coding, height=300, key="coding") #nombre, altura 300, key

with st.container():
  st.write("--")
  st.header("Mis videos")
  image_column, text_column = st.columns((1, 2)) #tupla que especifica que queremos un renglón y dos columnas
  with image_column:
    st.image(imagen_video)
  with text_column:
    st.write(
      """
      Este es mi emblema pegado en una bicicleta. Vean el video más reproducido
      en mi canal con el siguiente enlace:
      """
    )
    st.markdown("[Ver video...](https://www.youtube.com/watch?v=hhSnVpR6Ul4)")

#!streamlit run app.py & npx localtunnel esto es para correrlo desde la terminal en VSC
