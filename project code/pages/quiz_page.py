'''
CS 5001 Final Project
Name: quiz_page
Author: Yuhao Lu
Date: 2023-12-04
This file includes the quiz page of the app.
'''

import streamlit as st

questions = [
    {
        'question': 'What is the largest planet in our solar system?',
        'options': ['Please choose your answer', 'Earth', 'Jupiter', 'Mars', 'Venus'],
        'correct_answer': 'Jupiter'
    },
    {
        'question': 'Which galaxy is the Milky Way a part of?',
        'options': ['Please choose your answer', 'Andromeda', 'Whirlpool', 'Triangulum', 'Local Group'],
        'correct_answer': 'Local Group'
    },
    {
        'question': 'What is the closest star to Earth?',
        'options': ['Please choose your answer', 'Alpha Centauri', 'Sirius', 'Proxima Centauri', 'Betelgeuse'],
        'correct_answer': 'Proxima Centauri'
    }
]


def astronomy_quiz():
    """
    Display an astronomy quiz using Streamlit.

    The quiz consists of multiple-choice questions with options, and the user
    can select their answers. After answering all questions, the final score is displayed.

    Questions:
    1. What is the largest planet in our solar system?
    2. Which galaxy is the Milky Way a part of?
    3. What is the closest star to Earth?

    Options:
    - Please choose your answer
    - Earth, Jupiter, Mars, Venus (Question 1)
    - Andromeda, Whirlpool, Triangulum, Local Group (Question 2)
    - Please choose your answer, Alpha Centauri, Sirius, Proxima Centauri, Betelgeuse (Question 3)

    Returns:
    None
    """
    st.title('Astronomy Quiz App')
    score = 0

    # Iterate through questions
    for i, q in enumerate(questions, 1):
        st.header(f'Question {i}: {q["question"]}')

        # Display options
        selected_option = st.radio("Choose an option", q['options'], key=f'question_{i}')

        # Check if an option is selected and if it's correct
        if selected_option is not None:
            if selected_option == q['correct_answer']:
                st.success('Correct!')
                score += 1
            else:
                st.error('Incorrect! ')
        else:
            st.warning('Please select an option before moving to the next question.')

    # Display final score
    st.subheader(f'Your final score: {score}/{len(questions)}')


# Run the astronomy_quiz function
if __name__ == '__main__':
    astronomy_quiz()
