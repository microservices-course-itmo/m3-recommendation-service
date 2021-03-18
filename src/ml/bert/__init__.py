import yaml
from utils import bd_connection as con


class BERT:
    def __init__(self):

        with open('ml/bert/db_params.yaml', "r") as ini:
            cfg = yaml.load(ini)
        param_dict_ml3 = {
            "database": cfg['M_DB_NAME'],
            "user": cfg['M_USER_NAME'],
            "password": cfg['M_PASSWD'],
            "host": cfg['M_HOST'],
            "port": cfg['M_PORT']
        }
        self.ml3_conn = con.connect(param_dict_ml3)

    def predict(self, input_data):
        try:
            wine_id = input_data["id"]

            vector_select_query = f"SELECT * FROM wine_bert_neighbors WHERE id='{wine_id}'"
            columns = ["id", "n_1", "n_2", "n_3", "n_4", "n_5"]
            wine_vectors = con.postgresql_to_dataframe(self.ml3_conn, vector_select_query, columns)

            return {"id": wine_vectors["id"][0],
                    "n_1": wine_vectors["n_1"][0],
                    "n_2": wine_vectors["n_2"][0],
                    "n_3": wine_vectors["n_3"][0],
                    "n_4": wine_vectors["n_4"][0],
                    "n_5": wine_vectors["n_5"][0],}
            
        except Exception as e:
                return {"status": "Error", "message": str(e)}