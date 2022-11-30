import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import pickle

# df = pd.read_csv('data/train_triplets.txt', sep='\t', names=['User', 'Song', 'Count'])
# users = df['User'].unique()

sim_users = pickle.load(open('pickled_files/user_user_similar.pkl', 'rb'))
user_to_idx = pickle.load(open('pickled_files/user_to_idx.pkl', 'rb'))
idx_to_user = pickle.load(open('pickled_files/idx_to_user.pkl', 'rb'))

users = list(user_to_idx.keys())

st.set_page_config(page_title="Song Recommendation", layout="wide")
title = "Song Recommendation Engine"
st.title(title)
st.write("Created by Amanbeer, Ram, and Shubhangi")

number = st.number_input('Selected the index of the user you want to recommend songs to', min_value=0, max_value=len(users)-1, value=0)
st.write('You have selected user ', number)
st.write('The anonymised name of this user is ', user_to_idx[number], ' but let\'s call them John Doe for now.')
st.markdown('---')
st.write('')
