import pandas as pd
from scipy.spatial import KDTree
from ast import literal_eval
from tqdm import tqdm

from bd_connection import wine_bert_neighbours_update, connect


def recalculate():
    # wines = read_all_wines_vectors() ##TODO
    # names = wines.name
    # ids = wines.id
    # vectors = wines.vectors
    # tree = KDTree(vectors)
    # for i,vector in tqdm(enumerate(vectors)):
    #     dist, indexes = tree.query(vector, 6)
    #     if not wine_in_neighbour_table(id[i]):
    #         wine_bert_neighbours_insert(names[i]) ##TODO
    #     else: wine_bert_neighbours_update(ids[i], [vectors[x] for x in indexes[1:]])
    pass