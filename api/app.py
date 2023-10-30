from flask import Flask, render_template, request


app = Flask(__name__)


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
            numbers.append(new_word)
    return numbers


def process_query(query):
    if (query == "dinosaurs"):
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif ("name" in query):
        return "Fly Devs"
    elif ("largest" in query):
        numbers = get_numbers(query)
        return str(max(numbers))
    elif "square" in query:
        numbers = get_numbers(query)
        for i in numbers:
            i = int(i)
            cube_root = i ** (1/3)
            square_root = i ** (1/2)
            if round(cube_root) ** 3 == i:
                if round(square_root) ** 2 == i:
                    return str(i)
    elif "multiplied" in i:
        numbers = get_numbers(query)
        return str(numbers[0] * numbers[1])
    elif "plus" in query:
        query_words = query.split(" ")
        numbers = []
        for word in query_words:
            if word[0].isdigit():
                if word[-1] == '?':
                    word = word[:-1]
                numbers.append(int(word))
        if numbers:
            return str(sum(numbers))
        else:
            return "No numbers found in the query"
    return "Unknown"


@app.route('/query', methods=['GET'])
def query():
    query_param = request.args.get('q')
    response = process_query(query_param)
    return response
