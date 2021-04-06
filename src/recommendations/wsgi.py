import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recommendations.settings')
application = get_wsgi_application()


from ml.registry import MLRegistry
# from ml.knn import KNN
from ml.bert import BERT

from utils import custom_logging

try: 
    registry = MLRegistry()
    # knn = KNN('/code/ml/knn/')
    # registry.add_algorithm("knn", knn)

    bert = BERT()
    registry.add_algorithm("bert", bert)
    print('ke')

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))
