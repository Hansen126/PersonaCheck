import pickle
import numpy as np
import re
import pandas as pd
import seaborn as sns
import glob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import FunctionTransformer
from sklearn.svm import LinearSVC
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix

# print test
print("line test")

all_files = glob.glob("mbti/MBTI500_part_*.csv")
data = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

# data = pd.read_csv(df)
X = data['posts']
y = data['type']

type_counts = {}

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state= 42)

def to_dense(X):
    return X.toarray()

pipeSVC = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')), 
    ('svd', TruncatedSVD(n_components=100)),  
    ('gnb', LinearSVC())  
])

pipeSVC.fit(X_train, y_train)
print("Model training complete")


def predict_mbti(text):
    
    result = pipeSVC.predict([text])
    
    return result[0]

# test
sample_text = "I enjoy spending time alone, reading books, and analyzing situations deeply."
print("Making prediction...")
mbti_type = predict_mbti(sample_text)
print(f"The predicted MBTI type is: {mbti_type}")