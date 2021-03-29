import nltk
import pandas as pd
import re
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
import pyLDAvis
import pyLDAvis.gensim 
nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))
from nltk.stem import WordNetLemmatizer
stemmer = WordNetLemmatizer()
import warnings
warnings.filterwarnings("ignore")

class LdaModeling():
    def __init__(self, data):
        self.df = pd.read_csv(data)
        self.df = self.df.drop(columns=['ID'])
        self.corpus_superlist = self.df[['text']].values.tolist()
        #corpus_superlist
        self.corpus = []
        for sublist in self.corpus_superlist:
            for item in sublist:
                self.corpus.append(item)


    def preprocessing(self):
        def preprocess_text(document):
        # Remove all the special characters
            document = re.sub(r'\W', ' ', str(document))

            # remove all single characters
            document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

            # Remove single characters from the start
            document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)

            # Substituting multiple spaces with single space
            document = re.sub(r'\s+', ' ', document, flags=re.I)

            # Removing prefixed 'b'
            document = re.sub(r'^b\s+', '', document)

            # Converting to Lowercase
            document = document.lower()

            # Lemmatization
            tokens = document.split()
            tokens = [stemmer.lemmatize(word) for word in tokens]
            tokens = [word for word in tokens if word not in en_stop]
            tokens = [word for word in tokens if len(word)  > 5]

            return tokens

    def preprocessing(self):
        def preprocess_text(document):
        # Remove all the special characters
            document = re.sub(r'\W', ' ', str(document))

            # remove all single characters
            document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

            # Remove single characters from the start
            document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)

            # Substituting multiple spaces with single space
            document = re.sub(r'\s+', ' ', document, flags=re.I)

            # Removing prefixed 'b'
            document = re.sub(r'^b\s+', '', document)

            # Converting to Lowercase
            document = document.lower()

            # Lemmatization
            tokens = document.split()
            tokens = [stemmer.lemmatize(word) for word in tokens]
            tokens = [word for word in tokens if word not in en_stop]
            tokens = [word for word in tokens if len(word)  > 5]

            return tokens