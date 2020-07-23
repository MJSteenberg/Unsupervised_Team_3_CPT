"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
import pickle

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview", "About Us",
                   "Contact Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('First Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("This page describes the winning approach.")
        
        solution_options = ["Problem Statement", "Exploratory Data Analysis"]
        
        solution_select = st.sidebar.selectbox("Choose Option", solution_options)
                       
        if solution_select == "Exploratory Data Analysis":
            st.subheader("Exploratory Data Analysis")
            st.write("""
            A summary of the insights in the movies data set.
                    """)

            # Reads in saved graphs
            st.image('resources/imgs/bar.png', use_column_width = True)
            st.write("""
            The bar chart describes the number of ratings in millions for each 
            movie in the database scaled from a rating of 0.5 to 5.0. The lowest 
            rated movies are given a 0.5 rating and the highest rated movies are
            given a 4.0. On average the ratings are 3.0 and above indicating
            that the users enjoy the movies in the data set.        
                     """)

            st.image('resources/imgs/fig.png', use_column_width = True)
            st.write("""
            The line chart describes a count of the number of ratings for each movie.
            The shape of the chart indicates a negative relationship between the count
            ratings and the number of movies. This means that a few movies have a 
            higher count of ratings, and as the number of movies increase the count of
            ratings decreases.""")
        
    if page_selection == "About Us":
        st.title("About Us")
        
        about_options = ["Team", "Mission Statement", "Problem Landscape", "Motivation"]
        
        about_select = st.sidebar.selectbox("Choose Option", about_options)

        if about_select == "Team":
            st.subheader("Team")
            st.write("We are a team of data scientists from Team_3_CPT.")
       
        if about_select == "Mission Statement":
            st.subheader("Our Mission")
            st.write("""
            We are a creative and passionate group of data scientists who are
            on a mission to make a difference in our community by bringing
            innovative programs and projects that promote ingenuity, inclusivity
            and integrity. We want to make our community a better place by 
            giving people tools and information to make better decisions.""")

        if about_select == "Problem Statement":
            st.subheader("Problem Statement")
            st.write("""
            To construct a recommendation algorithm based on content or 
            collaborative filtering, capable of accurately predicting how
            a user will rate a movie they have not yet viewed based on their 
            historical preferences.""")
            
        if about_select == "Problem Landscape":
            st.subheader("Problem Landscape")
            st.image('resources/imgs/cpt.jpg', use_column_width = True)
            st.write("""
            Providing an accurate and robust solution to this challenge has 
            immense economic potential, with users of the system being 
            exposed to content they would like to view or purchase - 
            generating revenue and platform affinity.""")

        if about_select == "Motivation":
            st.subheader("Motivation")
            st.write("""Improve customer experience by exposing users to 
            content that matches their taste.""")
            st.write("""Increase sales for service providers.""")
            st.write("""Reduce transaction costs of finding and selecting 
            relevant content in an online platform.""")
        
    if page_selection == "Contact Us":
        st.title("Contact Us")
        st.write("""Have any questions? We would love to hear from you.""")
           
        st.text_input("""Name:""")
        st.text_input("""Surname:""")
        st.text_input("""Comment:""")
        
        st.subheader("Contact Info")
        st.write("""Tel: 012 589 4856""")
        st.write("""Fax: 012 589 4800""")
        st.write("""Email: info@team3cpt.com""")
        st.write("""Postal Address""")
        st.write("""Private Bag X756, Observatory, Western Cape,
                 South Africa""")

        st.subheader("Social Media")
        st.write("""Facebook: Team_3_CPT""")
        st.write("""Twitter & Instagram: @team_3_cpt""")
        
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
