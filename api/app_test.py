from app import process_query


def test_knows_about_dinosaurs():

    assert process_query("dinosaurs") == "Dinosaurs ruled the Earth"\
        " 200 million years ago"


def test_does_not_know_about_asteroids():

    assert process_query("asteroids") == "Unknown"


def test_team_name():

    assert process_query("What is your name?") == "Fly Devs"


def test_largest_number():

    assert process_query("Which of the following \
    numbers is the largest: 1, 72, 61?") == 72


def test_addition():

    assert process_query("What is 39 plus 52?") == 91


def test_multiplication():

    assert process_query("What is 45 multiplied by 5?") == 225


def test_find_square_and_cube():

    assert process_query("Which of the following numbers is both a square \
     and a cube: 3819, 944, 1772, 125, 319, 4356, 64?") == 64
