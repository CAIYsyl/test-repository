import streamlit as st

def education_page():
    st.markdown(
        """
        ### Education
        - **University of XYZ**, Anytown, USA
          - Master of Science in Data Science, 2023
          - Thesis: "Predicting Customer Churn Using Machine Learning Techniques"
          - GPA: 3.8/4.0
        
        - **ABC College**, Sometown, USA
          - Bachelor of Science in Computer Science, 2021
          - Senior Project: "Developing a Recommendation System for E-commerce Websites"
          - GPA: 3.7/4.0
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        """
        ### Relevant Coursework
        - **Machine Learning** (A)
          - Developed and implemented various machine learning algorithms, including decision trees, random forests, and support vector machines
          - Completed a project on sentiment analysis using deep learning techniques
        
        - **Data Mining and Analytics** (A)
          - Learned techniques for data preprocessing, exploratory data analysis, and feature engineering
          - Applied data mining algorithms, such as association rule mining and clustering, to real-world datasets
        
        - **Big Data Technologies** (A-)
          - Gained hands-on experience with Hadoop, Spark, and Hive for processing and analyzing large-scale datasets
          - Implemented a distributed computing project using Apache Spark for processing log data
        
        - **Database Systems** (B+)
          - Studied relational and NoSQL database systems, including SQL and MongoDB
          - Designed and implemented a database schema for a web application
        
        - **Data Visualization** (A)
          - Learned principles of effective data visualization and storytelling
          - Created interactive dashboards using Tableau and D3.js
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")