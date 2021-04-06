from kafka import KafkaConsumer
import new_wine_saved_message_sent_event_pb2 as new_wine

import  bd_connection as bd
from vectorisation_model import vectorize, get_model
from neighbours_recalculation import recalculate
import configparser
import os

import custom_logging


script_path = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()  
config.read(script_path + "/config.ini")
# print(config.sections())

TOPIC_WINE = config['CONFIG']['TOPIC_WINE']
BOOTSTRAP_SERVER = config['CONFIG']['BOOTSTRAP_SERVER']
AUTO_OFFSET_RESET = config['CONFIG']['AUTO_OFFSET_RESET']
GROUP_ID = config['CONFIG']['GROUP_ID']
# OUR_ADDRESS = os.environ["S_OUR_ADDRESS"]

wine_consumer = KafkaConsumer(
    TOPIC_WINE,
    bootstrap_servers=BOOTSTRAP_SERVER,
    auto_offset_reset=AUTO_OFFSET_RESET,
    group_id=GROUP_ID
)

model = get_model()

def consume_new_wines(consumer):
    counter = 0
    for message in consumer:
        message = message.value
        result = new_wine.NewWineSavedMessageSentEvent()
        result.ParseFromString(message)
        wine_id = result.wineId
        wine_name = result.wineName
        wine_description, wine_gastrobomy = bd.wine_info_get(wine_id)
        bd.wine_catalog_info_insert(wine_id, wine_name, wine_description, wine_gastrobomy)
        vector = vectorize(model, wine_description + wine_gastrobomy)
        bd.wine_vectors_insert(wine_id, wine_name, vector)
        print(result)
        if counter > 0 and counter % 500 == 0: recalculate()


if __name__ == "__main__":
    # print(TOPIC_WINE)
    consume_new_wines(wine_consumer)
