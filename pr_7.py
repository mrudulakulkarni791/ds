7
Text Analytics 1. Extract Sample
document and apply following document
preprocessing methods: Tokenization,
POS Tagging, stop words removal,
Stemming and Lemmatization.
2. Create representation of documents by
calculating Term Frequency and Inverse
Document Frequency.
  
#7th
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')  # ✅ FIX
document = """Text Analytics is a crucial step in analyzing unstructured data.
It involves tokenization, lemmatization, and stop words removal."""

tokens = wordpunct_tokenize(document)
print("\nTokens:\n", tokens)

pos_tags = nltk.pos_tag(tokens)
print("\nPOS Tags:\n", pos_tags)

stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("\nFiltered Tokens:\n", filtered_tokens)

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_tokens]
print("\nStemmed Words:\n", stemmed_words)

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_tokens]
print("\nLemmatized Words:\n", lemmatized_words)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([document])
print("\nTF-IDF Matrix:\n", tfidf_matrix.toarray())
print("\nFeature Names:\n", vectorizer.get_feature_names_out())


