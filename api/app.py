from flask import Flask, render_template, request
import requests


app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


def get_numbers(query):
    query_words = query.split(" ")
    numbers = []
    for word in query_words:
        if word and word[0].isdigit():
            new_word = ""
            for w in word:
                if w.isdigit():
                    new_word += w
            numbers.append(int(new_word))
    return numbers


def is_prime(number):
    root = number ** (1/2)
    for i in range(2, round(root)+1):
        if number % i == 0:
            return False
    return True


def process_query(query):
    numbers = get_numbers(query)
    if (query == "dinosaurs"):
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif ("name" in query):
        return "Fly Devs"
    elif ("largest" in query):
        return str(max(numbers))
    elif "square" in query:
        for i in numbers:
            cube_root = i ** (1/3)
            square_root = i ** (1/2)
            if round(cube_root) ** 3 == i:
                if round(square_root) ** 2 == i:
                    return str(i)
    elif "multiplied" in query:
        return str(numbers[0] * numbers[1])
    elif "minus" in query:
        return str(numbers[0] - numbers[1])
    elif "prime" in query:
        primes = list(filter(is_prime, numbers))
        return ', '.join([str(i) for i in primes])
    elif "plus" in query:
        return str(sum(numbers))
    return "Unknown"


@app.route('/query', methods=['GET'])
def query():
    query_param = request.args.get('q')
    response = process_query(query_param)
    return response


@app.route('/extension')
def extension():
    return render_template("extension.html")


@app.route('/extension/response', methods=['GET'])
def response():
    git_user_name = request.args.get("username")
    commits = []
    contributors = []

    response = requests.get(f"https://api.github.com/users/\
{git_user_name}/repos")
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            repo_response = requests.get(f"{repo['commits_url'][:-6]}")
            if repo_response.status_code == 200:
                commits.append(repo_response.json())
            contributors_response = requests.get(f"{repo['contributors_url']}")
            if contributors_response.status_code == 200:
                contributors.append(contributors_response.json())
        return render_template(
                            "repo_list.html", repos=repos,
                            git_name=git_user_name, commits=commits,
                            contributors=contributors)
    return f"Could not find Github account {git_user_name}. \
    Please check the name and try again"
