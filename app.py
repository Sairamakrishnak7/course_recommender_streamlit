import streamlit as st
import pandas as pd

# Sample data
courses = pd.read_csv("data/courses.csv")

def recommend_courses(keywords):
    keywords = keywords.lower().split(",")
    matches = courses[courses['keywords'].apply(lambda x: any(kw in x for kw in keywords))]
    return matches.head(5)

st.title("📚 Course Recommender System")
st.write("Paste your skills or job description, and get course suggestions based on keyword matching.")

user_input = st.text_area("Enter skills or job description:")
if st.button("Recommend Courses"):
    if user_input.strip():
        results = recommend_courses(user_input)
        if not results.empty:
            st.write("### Recommended Courses:")
            for _, row in results.iterrows():
                st.markdown(f"- **{row['title']}** — _{row['provider']}_")
        else:
            st.warning("No matching courses found.")
    else:
        st.error("Please enter some text.")
