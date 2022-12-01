import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import pickle
from PIL import Image
from os.path import exists
from lyrics_similarity_api import Method1 as LyricsSimilarityModel
from user_similarity_api import UserSimilarityModel

def show_image(path):
    img = Image.open(path)
    st.image(img)

sim_users = pickle.load(open('pickled_files/user_user_similar.pkl', 'rb'))
user_to_idx = pickle.load(open('pickled_files/user_to_idx.pkl', 'rb'))
idx_to_user = pickle.load(open('pickled_files/idx_to_user.pkl', 'rb'))
df_path = 'data/train_triplets.txt'

lsm = LyricsSimilarityModel()
usm = UserSimilarityModel(sim_users, df_path)

users = list(user_to_idx.keys())
songs = lsm.track_lyrics_df['Title'].unique()

st.set_page_config(page_title="Song Recommendation", layout="wide")
title = "Song Recommendation Engine"
st.title(title)
st.write("Created by Amanbeer, Ram, and Shubhangi")

# tab1, tab2, tab3 = st.tabs(["Lyric-Based Similarity", "User-Based Similarity", "Hybrid Approach"])

# def find_songs(number):
#     # user = idx_to_user[number]
#     songs = usm.get_most_played(number, names=True)
#     for song in songs:
#         lsm.RecommendSongs(song)
#         songs = lsm.temp[['Title', 'Artist', 'Lyrics']].values.tolist()
#         print(songs)

# with st.container():

#     number = st.number_input('Selected the index of the user you want to recommend songs to', min_value=0, max_value=len(users)-1, value=0)
#     st.write('You have selected user ', number)
#     st.write('The anonymised name of this user is ', idx_to_user[number], ' but let\'s call them John Doe for now.')
#     # # song = st.selectbox('Select a song to see similar songs', songs)
#     # # st.write('You have selected song ', song)    
#     if st.button('Show song recommendations'):
#         st.write('Based on the most played songs of similar users, we recommend the following songs to John Doe:')
#         song = usm.get_most_played(number, names=True)[0]
#         lsm.RecommendSongs(song)
#         lsm.LyricCloud(song)
#         st.write('The top 5 similar songs to ', song, ' are:')
#         st.write(lsm.temp[['Title','Artist name']].values)
#         st.markdown('---')
#         st.write('Here\'s a word cloud of the lyrics of the similar songs:')
#         show_image('images/temp_wordcloud.jpg' if not exists('images/wordcloud.png') else 'images/wordcloud.png')

        # st.write('The top 5 recommended songs for John Doe are: ')
    #     if usm.get_similar_users(number) == []:
    #         st.write('Hold up. There are no similar users! Let\'s try finding their most played songs instead.')
    #         st.markdown('**Most played songs:**')
    #         st.write(usm.get_most_played(number, names=True))
    #         st.markdown('---')
    #         st.write('Here are the top 5 songs that are most similar to the most played songs.')
    #         temp_songs = usm.get_song_from_trackID(usm.get_most_played(number))
    #         for song in temp_songs:
    #             temp = []
    #             lsm.RecommendSongs(song)
    #             for row in lsm.temp[['Title','Artist name']].values:
    #                 temp.append(row)
    #         for song in usm.sort_by_familiarity(temp):
    #             st.write(song)
    #     else:
    #         for song in usm.get_recommendations(number):
    #             st.write(song)

# with st.container():
#     number = st.number_input('Selected the index of the user you want to recommend songs to', min_value=0, max_value=len(users)-1, value=0)
#     st.write('You have selected user ', number)
#     st.write('The anonymised name of this user is ', user_to_idx[number], ' but let\'s call them John Doe for now.')
#     st.markdown('---')
#     st.write('The top 5 songs that John Doe has listened to are:', user_to_idx[number])
#     st.markdown('---')
#     st.write('Here\'s a word cloud of the lyrics of the songs that John Doe has listened to:')
#     show_image('images/temp_wordcloud.png')

# if __name__ == '__main__':
#     find_songs(0)