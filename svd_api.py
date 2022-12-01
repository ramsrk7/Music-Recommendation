import pandas as pd
import numpy as np
import pickle
import sqlite3
from tqdm import tqdm
import os
from surprise import Dataset, dump, SVD


db_conn = sqlite3.connect('data/track_metadata.db')
sql_query = pd.read_sql_query(''' SELECT * FROM songs ''', db_conn)
tracks = pd.DataFrame(sql_query)

# file locs
svd_bins = 'pickled_files/svd_model_bins.pkl'
df_path = 'data/train_triplets.txt'
svd_file = os.path.expanduser("pickled_files/svd_bins.pkl")



class SVDModel():
    def __init__(self, svd_file, df_path):    
        self.svd = dump.load(svd_file)

        self.df = pd.concat([chunk for chunk in 
        tqdm(pd.read_csv(df_path, sep = '\t', index_col=None, names = ['User','Song', 'Count'],  chunksize=1000), 
        desc='Loading User-Song Database')])

    def get_rating(self, user, track):
        prediction = self.svd.predict(uid=user, iid=track)
        return prediction

    def get_song_ranking(self, user, songs):
        predictions = pd.DataFrame()
        song_preds = []
        for song in songs:
            pred = self.svd.predict(uid=user, iid=song)
            song_preds.append(round(pred.est, 2))
        
        predictions['User'] = user
        predictions['Song'] = songs
        predictions['Predictions'] = song_preds
        predictions.sort_values(by=['Predictions'], ascending=False)
        return predictions
    
    def get_song_from_trackID(self, track):
        return tracks[tracks['track_id']==track]