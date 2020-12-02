import joblib
import pandas as pd
from pathlib import Path
import numpy as np

import pathlib

class KNN:
    def __init__(self, path_to_data="../ml/"):
        print(pathlib.Path().absolute())
        data_folder = Path(path_to_data)
        self.model = joblib.load(data_folder / "knn.joblib")
        self.data = pd.read_csv(data_folder / "winestyle_clean.csv")
        np_data = np.load(data_folder / "prep_data.npy", allow_pickle=True)
        self.samples = np_data[:, 1:]
        self.names = np_data[:, 0]
    
    def predict(self, input_data):
        try:
            ID = input_data['id']
            NEIGHBORS = input_data['n_nbrs'] + 1
            print(input_data)
            dist, nbrs = self.model.kneighbors([self.samples[ID]], NEIGHBORS)
            nbrs = nbrs[0]
            predictions = [wine for wine in self.names[nbrs] if wine != self.names[ID]]
            return {"sampled_wine": self.names[ID],
                    "predictions": predictions}
        except Exception as e:
            return {"status": "Error", "message": str(e)}

    