import streamlit as st

def experience_page():
    st.markdown(
        """
        ##### Data Science Intern at XYZ Company
        - Developed a machine learning model to predict customer churn, resulting in a 20% reduction in churn rate
        - Collaborated with cross-functional teams to identify and prioritize data-driven initiatives
        - Conducted exploratory data analysis and presented insights to stakeholders
        - Technologies used: Python, Scikit-learn, Pandas, Matplotlib
        """,
        unsafe_allow_html=True
    )

    with st.expander("Click here to see more details"):
        st.write(
            """
            - Preprocessed and cleaned large datasets to ensure data quality and consistency
            - Implemented and evaluated various machine learning algorithms, including logistic regression, random forests, and gradient boosting
            - Performed feature engineering and selection to improve model performance
            - Created interactive dashboards using Tableau to visualize key metrics and insights
            - Participated in weekly stand-up meetings and presented progress updates to the data science team
            """
        )

    st.markdown("---")

    st.markdown(
        """
        ##### Research Assistant at ABC University
        - Assisted in conducting research on deep learning techniques for image classification
        - Implemented and evaluated convolutional neural network (CNN) architectures using TensorFlow and Keras
        - Contributed to the preparation of research papers and presentations
        - Technologies used: Python, TensorFlow, Keras, OpenCV
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        ##### Teaching Assistant at DEF University
        - Assisted in teaching an undergraduate course on data structures and algorithms
        - Conducted weekly lab sessions and provided guidance to students on programming assignments
        - Graded assignments and provided constructive feedback to help students improve their coding skills
        - Technologies used: Java, Python, C++
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")