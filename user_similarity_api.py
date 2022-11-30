import pandas as pd
import numpy as np
import pickle
from tqdm import tqdm

with open('pickled_files/user_user_similar.pkl', 'rb') as f:
    sim_users = pickle.load(f)
    f.close()

df = pd.concat([chunk for chunk in 
tqdm(pd.read_csv('data/train_triplets.txt', sep = '\t', index_col=None, names = ['User','Song', 'Count'],  chunksize=1000), 
desc='Loading User-Song Database')])

def get_similar_users(user):
    return sim_users[user]

def get_most_played(user_idx):
    return df[user_idx]['Song'].value_counts().index[:5]

def top_songs_from_similar(user_idx):
    similar_users = get_similar_users(user_idx)
    top_songs = []
    for user in similar_users:
        top_songs.extend(get_most_played(user))
        top_songs = list(set(top_songs))
    return top_songs