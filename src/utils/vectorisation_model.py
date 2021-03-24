from sentence_transformers import SentenceTransformer, models
import nltk
from nltk.tokenize import sent_tokenize

def get_model():
    # Google-Drive link: https://drive.google.com/drive/folders/1sUxvLCTJHOkPeB4thHO-RW8WI3DWLHos?usp=sharing
    PATH = "DeepPavlov/rubert-base-cased"
    
    model = models.Transformer(PATH)
    pooling_model = models.Pooling(model.get_word_embedding_dimension())
    model = SentenceTransformer(modules=[model, pooling_model])
    nltk.download('punkt')
    return model

def vectorize(model, description):
    tokens = sent_tokenize(description, language="russian")
    res = model.encode(tokens)[0]
    return res