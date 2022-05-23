Microsoft Mentee project on Algorithms:
# Movie Recommendation System

### Steps:<br>
-Download all files<br>
-Download and install all requirements in requirement.txt<br>
-run python test1.py in terminal<br>
-click link on terminal or copy link and open ip on browser.

# To Get API KEY
Create an account in https://www.themoviedb.org/, click on the API link in your account settings and fill all  details to apply for API key. Fill website URL as "NA" if you don't have one. You will see the API key to copy once your request is approved. <br>

In file `static/recommned.js` and `static/rec.js` replce my_api_key value with your own API key.
<br>
Replace your API key on:<br>
1. `static/recommned.js` line 15 and 31<br>
2. `static/rec.js` line 4 and 20<br>

## Search Engine and type of Sort used:<br>
<br>
1. **Search engine:** Fast Autocomplete & Typeahead Library – autoComplete.js 
https://www.cssscript.com/fast-autocomplete-typeahead/
<br>
2. **Sort:**  Python's Tim sort <br>
<br>

![image](https://user-images.githubusercontent.com/70155541/169867952-1490cc3e-17be-4c6f-98f5-be87d91a9141.png)


<br>



## Pre-processing using Machine Learning <br>
All pre-processing to obtain final TMDB2.csv file done in the colab files(.pynb)

# Workflow:

#### Home page(home.html)

![image](https://user-images.githubusercontent.com/70155541/169860918-686f9837-7f28-4e19-88db-13a3ce67261f.png)

--> Here you may enter name of any movie (`autocomplete.js` and `get_mvsuggest` function in test1.py file suggests the full movie names. Thus as soon as you start typing some matching movie names will come up) and if its's present in the database, once you click the search button , the `recommend.js` file has a function that fetched the movie title as soon as you click the search button. <br>

--> It then calls several other functions that fetch the details of the movie from the TMDB site using your API keys like genre, plot, casts, cast details, poster etc.
<br>
(in case you get an error in recommendation alert refresh or hard refresh (ctrl + F5) the browser aftr clicking ok)
<br>
<br>
![image](https://user-images.githubusercontent.com/70155541/169867567-f21a2d2d-3a46-4ea9-8833-e267157b75af.png)

![image](https://user-images.githubusercontent.com/70155541/169867632-883d948c-ebd2-46f7-b6de-6ef1e47db868.png)

<br>
--> At the same time in the python file you reach the /similarity routing.This calls functions to calculates cosine similarity of the movie by making count vectors of the `tags` column in the TMDV2.csv file. The `tag` cloumn is a mix of the movie genres, directors, actors and plot. <br>
<br>

-->After calculating similarity the `recmnd()` function sorts the movies in order from highest similarity to lowest using python's sort function.<br> Python's sort function uses `Tim sort` which is a mix of merge and insertion sort.<br>
<br>
--> Fetch details of recommended movies (according to the sorted similarity list) and display in the correct order

![image](https://user-images.githubusercontent.com/70155541/169870803-5d23a76e-a626-4b97-8b50-897835243256.png)

###  TOP10 (Top10.html) <br>
--> List of top 10 movies of all genres sorted according to decreasing popularity. Click on any of the listed movies, you'll get the details of the movie as well as recommendations. File uses the `rec.js` file

![image](https://user-images.githubusercontent.com/70155541/169868160-215cb660-15e6-4caa-a20d-d997af3edf5d.png)
<br>


###  TOPRATED (Toprated.html) <br>
--> List of top 10 most rated movies of all genres sorted according to decreasing ratings. Click on any of the listed movies, you'll get the details of the movie as well as recommendations. File uses the `rec.js` file for recommendation

![image](https://user-images.githubusercontent.com/70155541/169868578-0412e0a9-21bc-49e3-8394-11982d56bb8d.png)
<br>

###  POPULAR (popular.html) <br>
--> List of most popular movies sorted according to genre. Click on any of the listed movies, you'll get the details of the movie as well as recommendations. File uses the `rec.js` file for recommendation<br>
Listed according to the output csv files obtained from the colab files eg) Crime.csv , Romance.csv etc.

![image](https://user-images.githubusercontent.com/70155541/169868626-a29b84bc-1637-4d2f-a465-b991c1eb0494.png)
![image](https://user-images.githubusercontent.com/70155541/169868700-bfa948c4-bf7e-40d3-ab3c-fac0c1c73cb3.png)
![image](https://user-images.githubusercontent.com/70155541/169870884-80ca6a89-c5e6-482b-b745-21e066e821ef.png)

