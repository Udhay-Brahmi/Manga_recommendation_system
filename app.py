import pickle
import streamlit as st
import numpy

st.markdown("<h1 style='text-align: center; color: white;'>RECOMMENDED MANGA</h1>", unsafe_allow_html=True)
animes = pickle.load(open('manga.pkl', 'rb'))
similarity = pickle.load(open('s100.pkl','rb'))
for i in range(200,14601,100):
    nam = "s" + str(i) + ".pkl"
    similarity = numpy.append(similarity,pickle.load(open(nam,"rb")),axis=0)

def recommend(manga):
    index = animes[animes['Name'] == manga].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    names = []
    link = []
    img = []
    for i in distances[1:13]:
        try:
            names.append(animes.iloc[i[0]].Name)
            img.append(animes.iloc[i[0]].img)
            link.append(animes.iloc[i[0]].Link)
        except:
            pass
    return names,link,img

anime = animes['Name'].values
selected_anime = st.selectbox(
    "Type or select manga out of 14000+ manga's from the dropdown list & click on the image of selected one.",
    anime
)
if st.button('Show Recommendation'):
    names,link,img = recommend(selected_anime)
    for i in range(0,10,3):
        col1, col2, col3 = st.columns(3)
        with col1:
            try:
                st.text(names[i])
                st.markdown("""<h6 style='text-align: center;'><a href={}><img src={}></a></h6>""".format(link[i], img[i]),unsafe_allow_html=True)
            except:
                pass
        with col2:
            try:
                st.text(names[i+1])
                st.markdown("""<h6 style='text-align: center;'><a href={}><img src={}></a></h6>""".format(link[i+1],img[i+1]), unsafe_allow_html=True)
            except:
                pass
        with col3:
            try:
                st.text(names[i+2])
                st.markdown("""<h6 style='text-align: center;'><a href={}><img src={}></a></h6>""".format(link[i+2],img[i+2]), unsafe_allow_html=True)
            except:
                pass
    st.markdown("<h6 style='text-align: center; color: white;'>Data set credit : kaggle </h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: white;'>Developer : Udhay Brahmi </h6>", unsafe_allow_html=True)

