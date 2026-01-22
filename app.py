import streamlit as st
import pandas as pd

st.title("Anketa for age")

# Инициализация на данните
if "students" not in st.session_state:
    st.text-input()
  
st.subheader("How old are you")
st.text-input()

st.divider()

st.subheader("📈 Резултати")

# Средна оценка за всеки ученик
average_grades = {
    student: (sum(grades) / len(grades) if grades else 0)
    for student, grades in st.session_state.students.items()
}

df = pd.DataFrame.from_dict(
    average_grades, orient="index", columns=["Средна оценка"]
)

st.bar_chart(df)
