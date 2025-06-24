import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Loading movies.pkl
movies = pickle.load(open("movies.pkl", "rb"))

# Vectorize the 'tags' column
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Similarity matrix
similarity = cosine_similarity(vectors)

# Saving the similarity matrix
pickle.dump(similarity, open("similarity.pkl", "wb"))

print("Similarity matrix generated and saved as similarity.pkl")