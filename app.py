from flask import Flask, render_template, request, url_for, redirect

def login_function(username_key, username_input, password_key, password_input, dictionary_list):
    '''This function handles the login function'''

    for i in dictionary_list: #itterates thru the list
        if i[username_key] == username_input: # for every dictionary in the list it checks at the key in the brackets aginst the user input to see if it matches
            if i[password_key] == password_input:
                #print("success")
                #print(dictionary_list) # this is just for testing purposes, could be cut out
                return True
                #break
            else:
                print("fail")
                #break
        else:
            print("fail")
            #break

def signup_function(username_key, username_input, email_key, email_input, password_input, dictionary_list):
    '''This function is used to handle the signup feature'''

    for i in dictionary_list: # itterates thru list
        if i[username_key] != username_input: # for every dictionary in the list at the key in brackets and it makes sure that the username is not already taken
            if i[email_key] != email_input:
                print("success")
                dictionary_list.append({"username" : username_input, "email" : email_input, "password" : password_input}) # creats a new dictionary that represents a user account and adds it the list
                print(dictionary_list) # this is just for testing purposes, could be cut out
                return True
            else:
                print('email already in use')
                break
        else:
            print("Username already in use")
            print(dictionary_list) # this is just for testing purposes, could be cut out
            break


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

account_dictionary_list = [
    {"username": "user1" , "email": "fake@email.com", "password": "1234"},
    {"username": "user2" , "email": "bogus@email.com", "password": "1234"}   
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

@app.route('/form_login', methods=['POST', 'GET'])
def login_attempt():
    name1 = request.form['username']
    password = request.form['password']
    if login_function("username", name1, "password", password, account_dictionary_list) == True:
        print(account_dictionary_list)
        return redirect(url_for('home'))
    else:
        print(account_dictionary_list)
        return redirect(url_for('login'))

@app.route('/signup')
def signup():
        return render_template('signup_page.html')

@app.route('/form_signup', methods=['POST', 'GET'])
def signup_attempt():
    name1 = request.form['username']
    password = request.form['password']
    email = request.form['email']
    conf_password = request.form['confirm_password']

    if password == conf_password:
        if signup_function("username", name1, "email", email, password, account_dictionary_list) == True:
            account_dictionary_list.append({"username" : name1, "email" : email, "password" : password})
            print(account_dictionary_list)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('signup'))
    else:
        return redirect(url_for('signup'))

if __name__ == '__main__':
    app.run(debug=True)
