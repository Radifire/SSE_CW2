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
    numbers is the largest: 1, 72, 61") == 72
