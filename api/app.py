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


def is_prime(number):
    num = int(number)
    root = num ** (1/2)
    for i in range(2, root+1):
        if num % i == 0:
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
            i = int(i)
            cube_root = i ** (1/3)
            square_root = i ** (1/2)
            if round(cube_root) ** 3 == i:
                if round(square_root) ** 2 == i:
                    return str(i)
    elif "multiplied" in query:
        return str(int(numbers[0]) * int(numbers[1]))
    elif "minus" in query:
        return str(numbers[0] - numbers[1])
    elif "prime" in query:
        return ", ".join(list(filter(is_prime, numbers)))
    elif "plus" in query:
        return str(sum(numbers))
    return "Unknown"


@app.route('/query', methods=['GET'])
def query():
    query_param = request.args.get('q')
    response = process_query(query_param)
    return response
