import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import requests

def create_similarity():
    data = pd.read_csv('TMDBdata2.csv')
    # count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['tags'])
    # creating similarity score matrix
    similarity = cosine_similarity(count_matrix)
    return data,similarity

def recmnd(mv):
    mv = mv.lower()
    try:
        data.head()
        similarity.shape
    except:
        data, similarity = create_similarity()
    if mv not in data['title'].unique():
        return('Sorry! The movie you requested is not in our database. Please try with some other movies')
    else:
        i = data.loc[data['title']==mv].index[0]
        lst = list(enumerate(similarity[i]))
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[1:11] # excluding first item since it is the requested movie itself
        l = []
        for i in range(len(lst)):
            recm = lst[i][0]
            l.append(data['title'][recm])
        return l
    
# converting list of strings to list
def convert_to_list(list1):
    list1 = list1.split('","')
    list1[0] = list1[0].replace('["','')
    list1[-1] = list1[-1].replace('"]','')
    return list1

def get_mvsuggest():
    data = pd.read_csv('TMDBdata2.csv')
    return list(data['title'].str.capitalize())

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    suggestions = get_mvsuggest()
    return render_template('home.html',suggestions=suggestions)

@app.route("/top10")
def top10():
    datat = pd.read_csv('top10/Top10.csv')
    return render_template('Top10.html')

@app.route("/toprate")
def toprate():
    return render_template('Toprated.html')

    
@app.route("/pop")
def pop():
    return render_template('popular.html')


@app.route("/similarity",methods=["POST"])
def similarity():
    movie = request.form['name']
    rc = recmnd(movie)
    if type(rc)==type('string'):
        return rc
    else:
        m_str="---".join(rc)
        return m_str

@app.route("/recommend",methods=["POST"])
def recommend():
    # getting data from AJAX request
    title = request.form['title']
    cast_ids = request.form['cast_ids']
    cast_names = request.form['cast_names']
    cast_chars = request.form['cast_chars']
    cast_bdays = request.form['cast_bdays']
    cast_bios = request.form['cast_bios']
    cast_places = request.form['cast_places']
    cast_profiles = request.form['cast_profiles']
    imdb_id = request.form['imdb_id']
    poster = request.form['poster']
    genres = request.form['genres']
    overview = request.form['overview']
    vote_average = request.form['rating']
    vote_count = request.form['vote_count']
    release_date = request.form['release_date']
    runtime = request.form['runtime']
    rec_movies = request.form['rec_movies']
    rec_posters = request.form['rec_posters']

    # get movie suggestions for auto complete
    suggestions = get_mvsuggest()

    # call convert_to_list function for string to be converted to list
    rec_movies = convert_to_list(rec_movies)
    rec_posters = convert_to_list(rec_posters)
    cast_names = convert_to_list(cast_names)
    cast_chars = convert_to_list(cast_chars)
    cast_profiles = convert_to_list(cast_profiles)
    cast_bdays = convert_to_list(cast_bdays)
    cast_bios = convert_to_list(cast_bios)
    cast_places = convert_to_list(cast_places)
    
    # convert cast ids string to list (eg. "[a,b,c]" to [a,b,c])
    cast_ids = cast_ids.split(',')
    cast_ids[0] = cast_ids[0].replace("[","")
    cast_ids[-1] = cast_ids[-1].replace("]","")
    
    # rendering string to python format
    for i in range(len(cast_bios)):
        cast_bios[i] = cast_bios[i].replace(r'\n', '\n').replace(r'\"','\"')
    
    # combining multiple lists as dictionary which can be passed to the html file and be processed easily ,order is preserved
    movie_cards = {rec_posters[i]: rec_movies[i] for i in range(len(rec_posters))}
    casts = {cast_names[i]:[cast_ids[i], cast_chars[i], cast_profiles[i]] for i in range(len(cast_profiles))}
    cast_dets = {cast_names[i]:[cast_ids[i], cast_profiles[i], cast_bdays[i], cast_places[i], cast_bios[i]] for i in range(len(cast_places))}

   
    # passing data to the html file
    return render_template('recommend.html',title=title,poster=poster,overview=overview,vote_average=vote_average,
        vote_count=vote_count,release_date=release_date,runtime=runtime,genres=genres,
        movie_cards=movie_cards,casts=casts,cast_details=cast_dets)

if __name__ == '__main__':
    app.run(debug=True)
