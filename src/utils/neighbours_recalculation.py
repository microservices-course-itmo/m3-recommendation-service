import pandas as pd
from scipy.spatial import KDTree
from ast import literal_eval
from tqdm import tqdm

import  bd_connection as bd


def recalculate():
    wines = bd.wine_vectors_get() ##TODO
    # names = wines.name
    ids = wines.wine_id
    vectors = wines.vector
    tree = KDTree(vectors)
    for i,vector in tqdm(enumerate(vectors)):
        dist, indexes = tree.query(vector, 6)
        bd.wine_bert_neighbours_update(ids[i], [vectors[x] for x in indexes[1:]])