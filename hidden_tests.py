def test_exercise_1(answers):
    expected = {
        "question_1": 3,
        "question_2": 2,
        "question_3": 1,
        "question_4": 4,
        "question_5": 1,
        "question_6": 2,
        "question_7": 1,
        "question_8": 2,
        "question_9": 4,
        "question_10": 4,
    }

    assert isinstance(answers, dict)
    try:
        for k in answers.keys():
            q, n = k.split('_')
            assert q == 'question'
            assert 1 <= int(n) <= 10
    except AssertionError:
        raise AssertionError("Answers dict has unexpected keys")

    correct_answers = 0
    for k in expected.keys():
        if k not in answers:
            continue
        if expected[k] == answers[k]:
            correct_answers += 1

    if correct_answers == 0:
        raise AssertionError("Not enough correct answers to score points :(")

    score = round(correct_answers * 0.4, 1)
    print(f"{correct_answers} correct answers. Your score is {score}.")
    return score
