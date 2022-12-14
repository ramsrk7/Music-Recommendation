# Music-Recommendation

### Model Requirements: 

```
pip install -r requirements.txt
```

To update the model requirement versions (incase the requirements do throw an error), run the following on a new environment:

```
pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt
```

### DATA:

* Lyrics = "TrackData.csv", 
* Words = "Words.txt"
* Database = "track_metadata.db"
* Encodings ="Encodings_numpy.pickle.npy"
* User-Song Database = "train-triplets.txt"
  
[Download the files from Google Drive](https://drive.google.com/drive/u/0/folders/1xaiv2sQPoAWkgihlLOAVM0ZVOG4km5lq).


The models can be run through the UI, which is developed using Streamlit. Run the streamlit app using the following command.

```
streamlit run ui.py
```