import json
import numpy as np
import pandas as pd

dataset = pd.read_csv('CharityDrives.csv')

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words = 'english')
dataset['description'] = dataset['description'].fillna("")
tfidf_matrix = tfidf.fit_transform(dataset['description'])

from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(dataset.index, index = dataset['name']).drop_duplicates()


def get_recommendation_F_name(title, cosine_sim = cosine_sim):
  idx = indices[title]
  sim_scores = enumerate(cosine_sim[idx])
  sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)
  sim_scores = sim_scores[1:11]
  # for i in sim_scores:
  #   print(i)
  sim_index = [i[0] for i in sim_scores]
  # print(sim_index)
  return dataset[['name', 'category', 'description']].iloc[sim_index]


def get_recommendation_F_category(title, cosine_sim = cosine_sim):
  idx = indices[title]
  sim_scores = enumerate(cosine_sim[idx])
  sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)
  sim_scores = sim_scores[1:11]
  # for i in sim_scores:
  #   print(i)
  sim_index = [i[0] for i in sim_scores]
  # print(sim_index)
  return dataset[['name', 'category', 'description']].iloc[sim_index]

# get_recommendation_F_name('Yad Ezra')