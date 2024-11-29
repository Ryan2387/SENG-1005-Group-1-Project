from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'KN Key'

# Sample questions
questions = [
    {"id": 1, "question": "What is the chemical formula for water?", "options": ["CO₂", "H₂O", "O₂", "NaCl"], "answer": "H₂O"},
    {"id": 2, "question": "Which element has the atomic number 1?", "options": ["Helium", "Hydrogen", "Oxygen", "Carbon"], "answer": "Hydrogen"},
    {"id": 3, "question": "What type of bond is formed by the sharing of electrons?", "options": ["Ionic Bond", "Covalent Bond", "Metallic Bond", "Hydrogen Bond"], "answer": "Covalent Bond"},
    {"id": 4, "question": "Which gas is most commonly associated with causing global warming?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
    {"id": 5, "question": "What is the pH of a neutral substance?", "options": ["0", "7", "14", "10"], "answer": "7"}
]

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Route for the practice test page
@app.route('/practice_test', methods=['GET', 'POST'])
def practice_test():
    if request.method == 'POST':
        # Process answers and generate feedback
        user_answers = request.form
        score = 0
        feedback = []

        for question in questions:
            qid = str(question["id"])
            user_answer = user_answers.get(f"q{qid}")
            correct_answer = question["answer"]

            # Feedback for each question
            feedback.append({
                "question": question["question"],
                "user_answer": user_answer if user_answer else "No Answer",
                "correct_answer": correct_answer,
                "correct": user_answer == correct_answer
            })

            if user_answer == correct_answer:
                score += 1

        # Render results and show feedback
        return render_template('Practice_test.html', questions=questions, feedback=feedback, score=score, total=len(questions))

    # Render blank form
    return render_template('Practice_test.html', questions=questions, feedback=None, score=None, total=None)

# Additional routes
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login_page.html')

@app.route('/signup')
def signup():
        return render_template('signup_page.html')

if __name__ == '__main__':
    app.run(debug=True)
