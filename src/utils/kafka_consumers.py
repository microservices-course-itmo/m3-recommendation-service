from kafka import KafkaConsumer
import new_wine_saved_message_sent_event_pb2 as new_wine

from bd_connection import wine_catalog_info_insert, wine_vectors_insert, wine_bert_neighbours_update
from vectorisation_model import vectorize, get_model

TOPIC_WINE = 'eventTopic'
BOOTSTRAP_SERVER = "localhost:29092"
AUTO_OFFSET_RESET = "earliest"
GROUP_ID = "wine.catalog-service"
# OUR_ADDRESS = os.environ["S_OUR_ADDRESS"]

wine_consumer = KafkaConsumer(
    TOPIC_WINE,
    bootstrap_servers=BOOTSTRAP_SERVER,
    auto_offset_reset=AUTO_OFFSET_RESET,
    group_id=GROUP_ID
)

model = get_model()

def consume_new_wines(consumer):
    # new_wines = []
    for message in consumer:
        message = message.value
        result = new_wine.NewWineSavedMessageSentEvent()
        result.ParseFromString(message)
        wine_id = result.wineId
        wine_name = result.wineName
        # wine_catalog_info_insert(wine_id)
        # wine_vectors_insert(wine_id, wine_name, vectorize(#TODO somehow get description from catalog))
        print(result)


if __name__ == "__main__":
    consume_new_wines(wine_consumer)
