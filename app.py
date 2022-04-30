# Importing modules

import pickle # For loading model.
import streamlit as st # For web app
import numpy

# Main heading
st.markdown("<h1 style='text-align: center; color: white;'>RECOMMENDED MANGA</h1>", unsafe_allow_html=True)

# Loading data frame
animes = pickle.load(open('manga.pkl', 'rb'))

# Loading first similarity file
similarity = pickle.load(open('s100.pkl','rb'))

# Adding other similarity files 
for i in range(200,14601,100):
    nam = "s" + str(i) + ".pkl"
    similarity = numpy.append(similarity,pickle.load(open(nam,"rb")),axis=0)

# This will recommend different mangas based on selected one.
def recommend(manga):
    
    # Finding index of selected manga
    index = animes[animes['Name'] == manga].index[0]
    
    # Sorting dataframe with similarity matrix based on name at index 1 in reverse order 
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    
    # Creating list
    names = []
    link = []
    img = []
    for i in distances[1:13]:
        try:
            # Adding row values in respective list
            names.append(animes.iloc[i[0]].Name)
            img.append(animes.iloc[i[0]].img)
            link.append(animes.iloc[i[0]].Link)
        except:
            pass
    
    # returning lists
    return names,link,img

# Collecting values of manga names
anime = animes['Name'].values

# Select box
selected_anime = st.selectbox(
    "Type or select manga out of 14000+ manga's from the dropdown list & click on the image of selected one.",
    anime
)

# Show recommendation button
if st.button('Show Recommendation'):
    
    # Recommended row's name, link, img
    names,link,img = recommend(selected_anime)
    
    for i in range(0,10,3):
        col1, col2, col3 = st.columns(3)
        with col1: # Row (i) and Column (1)
            try:
                st.text(names[i])
                st.markdown("""<h6 style='text-align: center;'><a href={}><img src={}></a></h6>""".format(link[i], img[i]),unsafe_allow_html=True)
            except:
                pass
        with col2: # Row (i) and Column (2)
            try:
                st.text(names[i+1])
                st.markdown("""<h6 style='text-align: center;'><a href={}><img src={}></a></h6>""".format(link[i+1],img[i+1]), unsafe_allow_html=True)
            except:
                pass
        with col3: # Row (i) and Column (3)
            try:
                st.text(names[i+2])
                st.markdown("""<h6 style='text-align: center;'><a href={}><img src={}></a></h6>""".format(link[i+2],img[i+2]), unsafe_allow_html=True)
            except:
                pass
    
    # Bottom text
    st.markdown("<h6 style='text-align: center; color: white;'>Data set credit : kaggle </h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: white;'>Developer : Udhay Brahmi </h6>", unsafe_allow_html=True)

