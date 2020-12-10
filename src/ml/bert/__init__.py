import pandas as pd
import numpy as np
from tqdm import tqdm
from scipy import spatial
from pathlib import Path

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

import sentence_transformers
from sentence_transformers import SentenceTransformer, models

class BERT:
    def __init__(self, path_to_data="../ml/bert/"):
    
        data_folder = Path(path_to_data)
        df = pd.read_csv(data_folder / "winestyle_vectors_final.csv")
        self.df = df[["name", "vector"]]

        df_rec = pd.read_csv(data_folder / "wines_winestyle.csv")
        self.df_rec = df_rec[["name"]]

        for index, _ in tqdm(self.df.iterrows()): 
            self.df.at[index,'vector'] = self.to_str(self.df.at[index,'vector'])
        try:
            word_embedding_model = models.Transformer("../ml/bert/rubert-base-cased")
            pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())

            self.bert_model = SentenceTransformer(modules=[word_embedding_model, pooling_model])
        except Exception as e:
            print("Exception while loading bert,", str(e))

    def to_str(self, string_vec):
        res = string_vec.strip('][').replace("\n", "").split(" ")
        res = [float(x) for x in res if x != ""]
        return res

    def predict(self, input_data):
        try:
            description = input_data["description"]
            n = input_data["n_nbrs"]
            
            bert_vectors = self.df["vector"].tolist()
            
            string_tokens = sent_tokenize(description, language="russian")
            string_vector = self.bert_model.encode(string_tokens)[0]
            
            cos_sim = []
            for v in bert_vectors:
                cos_sim.append(1 - spatial.distance.cosine(string_vector, v))
            
            recommended = []
            indices = pd.Series(self.df['name'])

            score_series = pd.Series(cos_sim).sort_values(ascending = False)
            # print(score_series.iloc[0:n])
            top_indices = list(score_series.iloc[0:n].index)

            for i in top_indices:
                recommended.append(list(self.df['name'])[i])

            res = self.df_rec[self.df_rec['name'].isin(recommended)]
            res = res['name'].to_list()

            return {"description": description,
                    "predictions": res}
            
        except Exception as e:
                return {"status": "Error", "message": str(e)}