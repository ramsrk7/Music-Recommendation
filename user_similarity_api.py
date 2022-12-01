import pandas as pd
import numpy as np
import pickle
import sqlite3
from tqdm import tqdm

db_conn = sqlite3.connect('data/track_metadata.db')
sql_query = pd.read_sql_query (''' SELECT * FROM songs ''', db_conn)
tracks = pd.DataFrame(sql_query)

# file locs
sim_users = 'pickled_files/user_user_similar.pkl'
df_path = 'data/train_triplets.txt'
idx_to_user = pickle.load(open('pickled_files/idx_to_user.pkl', 'rb'))
user_to_idx = pickle.load(open('pickled_files/user_to_idx.pkl', 'rb'))


class UserSimilarityModel():
    def __init__(self, sim_users, df_path):    
        with open(sim_users, 'rb') as f:
            self.sim_users = pickle.load(f)
            f.close()

        self.df = pd.concat([chunk for chunk in 
        tqdm(pd.read_csv(df_path, sep = '\t', index_col=None, names = ['User','Song', 'Count'],  chunksize=1000), 
        desc='Loading User-Song Database')])

    def get_similar_users(self, user):
        return self.sim_users[user]

    def get_most_played(self, user_idx):
        return self.df[self.df['User']==idx_to_user[user_idx]]['Song'].value_counts().index[:5].tolist()

    def get_recommendations(self, user_idx):
        similar_users = self.get_similar_users(user_idx)
        top_songs = []
        for user in similar_users:
            top_songs.extend(self.get_most_played(user))
            top_songs = list(set(top_songs))
            for songs in self.get_most_played(user_idx):
                if songs in top_songs:
                    top_songs.remove(songs)
        return self.sort_by_familiarity(top_songs)
    
    def get_song_from_trackID(self, track):
        return tracks[tracks['track_id']==track]

    def sort_by_familiarity(self, top_songs):
        subset_tracks = tracks[tracks['track_id'].isin(top_songs)]
        subset_tracks = subset_tracks.sort_values(by=['artist_familiarity'], ascending=False)
        return subset_tracks['title'].values[:5]