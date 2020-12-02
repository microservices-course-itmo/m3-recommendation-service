import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recommendations.settings')
application = get_wsgi_application()


from ml.registry import MLRegistry
from ml.knn import KNN

try: 
    registry = MLRegistry()
    knn = KNN()
    registry.add_algorithm("knn", knn)
except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))
