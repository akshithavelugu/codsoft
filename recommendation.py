import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
data={
    'title':[
        'RRR','Kaithi','Drishyam','KGF','Asuran','3 Idiots'
    ],
    'Language':[
        'Telugu','Tamil','Malayalam','Kannada','Tamil','Hindi'
    ],
    'description':[
        'A tale of two revolutionaries in the 1920s.',
        'A convict escapes to save his daughter.',
        'A gripping thriller about a family’s secrets.',
        'A story of power and revenge in the gold mines.',
        'A farmer fights against the system for justice.',
        'A comedy-drama about friendship and education.'
    ]
}
df=pd.DataFrame(data)
df['combined_features']=df['description']+" "+df['Language']
vectorizer=TfidfVectorizer(stop_words='english')
tfidf_matrix=vectorizer.fit_transform(df['combined_features'])
similarity_matrix=cosine_similarity(tfidf_matrix,tfidf_matrix)
def recommend(movie_title):
    if movie_title not in df['title'].values:
        return "Movie not found in the database."
    idx=df.index[df['title']== movie_title].tolist()[0]
    sim_scores=list(enumerate(similarity_matrix[idx]))
    sim_scores=sorted(sim_scores,key=lambda x:x[1],reverse=True)[1:4]
    return[df['title'][i]+"("+df['Language'][i]+")" for i, score in sim_scores]
fav_movie=input("Enter your favourite movie: ")
print(f"\n Because you liked '{fav_movie}', you might also like:")
for suggestion in recommend(fav_movie):
    print(f"->{suggestion}")