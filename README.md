
# Movie Recommendation System (Microsoft Mentee project on Algorithms)

## Author
- [@RC2208](https://www.github.com/RC2208)


## Steps:<br>
- Download all files<br>
- Download and install all requirements in requirement.txt<br>
- run python test1.py in terminal<br>
- click link on terminal or copy link and open ip on browser.

## Deployment

To deploy this project in browser, run

```bash
  pip install -r requirements.txt
  python test1.py
```
## Tech Stack

- **Backend:** Flask, Python, JS

- **Frontend:** HTML, CSS, Bootstrap 

## Points to Note
- Requires a strong and stable internet connection
- It might show an alert: Error in recommendation (after clicking the search button) when you run the project for the 1st time (after you run python test1.py). You just need to hard refresh it (ctl + F5) and it will work smoothly.
- The kaggle dataset only has movies till the year 2017 thus as long as you enter a mobie name that released before 2017 you will get all details and recommendations since my recommendation algorithm uses the movies in the dataset (after I have done pre-processing) to calculate similarity
- I have created the recommendation system based on content based filtering.

## To Get API KEY
Create an account in https://www.themoviedb.org/, click on the API link in your account settings and fill all  details to apply for API key. Fill website URL as "NA" if you don't have one. You will see the API key to copy once your request is approved. <br>

In file `static/recommned.js` and `static/rec.js` replce my_api_key value with your own API key.
<br>
Replace your API key on:<br>
1. `static/recommned.js` line 15 and 31<br>
2. `static/rec.js` line 4 and 20<br>

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `my_api_key` | `string` | **Required**. Your API key |



## Search Engine and type of Sort used:<br>
<br>

- **Search Engine:** Fast Autocomplete & Typeahead Library – autoComplete.js <br> 
https://www.cssscript.com/fast-autocomplete-typeahead/

- **Sort:** Python's Tim sort <br>
<br>

![image](https://user-images.githubusercontent.com/70155541/169867952-1490cc3e-17be-4c6f-98f5-be87d91a9141.png)


<br>

## Pre-processing using Machine Learning <br>
All pre-processing to obtain final TMDB2.csv file done in the colab files(.pynb)

## Workflow:

## **Home page(home.html)**

![image](https://user-images.githubusercontent.com/70155541/169860918-686f9837-7f28-4e19-88db-13a3ce67261f.png)

- Here you may enter name of any movie (`autocomplete.js` and `get_mvsuggest` function in test1.py file suggests the full movie names. Thus as soon as you start typing some matching movie names will come up) and if its's present in the database, once you click the search button , the `recommend.js` file has a function that fetched the movie title as soon as you click the search button. <br>

- It then calls several other functions that fetch the details of the movie from the TMDB site using your API keys like genre, plot, casts, cast details, poster etc.
<br>
(in case you get an error in recommendation alert refresh or hard refresh (ctrl + F5) the browser aftr clicking ok)
<br><br>


![image](https://user-images.githubusercontent.com/70155541/169867567-f21a2d2d-3a46-4ea9-8833-e267157b75af.png)



![image](https://user-images.githubusercontent.com/70155541/169867632-883d948c-ebd2-46f7-b6de-6ef1e47db868.png)

- At the same time in the python file you reach the /similarity routing.This calls functions to calculates cosine similarity of the movie by making count vectors of the `tags` column in the TMDV2.csv file. The `tag` cloumn is a mix of the movie genres, directors, actors and plot. <br>


- After calculating similarity the `recmnd()` function sorts the movies in order from highest similarity to lowest using python's sort function.<br> Python's sort function uses `Tim sort` which is a mix of merge and insertion sort.<br>

- Fetch details of recommended movies (according to the sorted similarity list) and display in the correct order

![image](https://user-images.githubusercontent.com/70155541/169870803-5d23a76e-a626-4b97-8b50-897835243256.png)

## TOP10 (Top10.html) 

- List of top 10 movies of all genres sorted according to decreasing popularity. Click on any of the listed movies, you'll get the details of the movie as well as recommendations. File uses the `rec.js` file

![image](https://user-images.githubusercontent.com/70155541/170509604-f244e9c7-e490-407c-b024-eb7901ce4150.png)



##  TOPRATED (Toprated.html) 

- List of top 10 most rated movies of all genres sorted according to decreasing ratings. Click on any of the listed movies, you'll get the details of the movie as well as recommendations. File uses the `rec.js` file for recommendation

![image](https://user-images.githubusercontent.com/70155541/170510166-4523f14f-049f-4f80-85c0-db37b5bc1e00.png)


##  POPULAR (popular.html) <br>

- List of most popular movies sorted according to genre. Click on any of the listed movies, you'll get the details of the movie as well as recommendations. File uses the `rec.js` file for recommendation<br>
Listed according to the output csv files obtained from the colab files eg) Crime.csv , Romance.csv etc.

![image](https://user-images.githubusercontent.com/70155541/170510400-5ec44bbb-cbd5-449b-82a4-400957eec408.png)

![image](https://user-images.githubusercontent.com/70155541/170510511-5e9924b9-bd4e-4f44-9b98-f34c56128033.png)

![image](https://user-images.githubusercontent.com/70155541/170510582-52e33bee-721e-4c94-84e8-eecdc4739430.png)

![image](https://user-images.githubusercontent.com/70155541/170510642-b4a756dd-1d3d-4b09-9b1c-c0073fb29b0f.png)

![image](https://user-images.githubusercontent.com/70155541/170510717-9d9342ec-8592-4b89-9d25-4a1d295d516e.png)


## How I planned it:

- In the starting week I did some research work and watched YouTube videos on how a recommendation system is built. I knew the ML part since I am already familiar with it. 
- I got to know the different types of searches and recommendation algorithms and figured out which would work the best in the limited time frame i.e., content-based filtering using cosine similarity. 
- Next, I decided on the features of my project. 
- The ML part was the easy part for me. What I didn’t know was how to display the results of the algorithm or build a UI around it. So, I searched up different ways to display the colab file results in a website. One way was through the streamlit API, but I wasn’t able to install it in my system properly and was getting a lot of errors thus I had to scrap the idea and once again start the search. 
- There were 2 backend frameworks that worked on python i.e., Flask and Django. Both were new to me, but I chose to try and work with flask. I watched a few tutorial videos and got to know the workings of flask.
- Since I already knew web development the rest of the parts were simpler. Still, I had to find out how to how to get posters, movie and cast details through the TMDB website and display the same in my website which was a tedious task.

