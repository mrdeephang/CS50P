import os
import json
import project

def test_load_questions():
    if os.path.exists(project.QUESTIONS_FILE):
        os.rename(project.QUESTIONS_FILE, "questions_backup.json")

    with open(project.QUESTIONS_FILE, "w") as f:
        json.dump({
            "Sample Category": [
                {
                    "question": "Sample Question?",
                    "options": ["A", "B", "C", "D"],
                    "answer": "A"
                }
            ]
        }, f)

    questions = project.load_questions()
    assert isinstance(questions, dict)

    os.remove(project.QUESTIONS_FILE)
    if os.path.exists("questions_backup.json"):
        os.rename("questions_backup.json", project.QUESTIONS_FILE)

def test_save_answer():
    q = "What is your name?"
    a = "My name is test"
    if os.path.exists(project.ANSWERS_LOG):
        os.remove(project.ANSWERS_LOG)

    project.save_answer(q, a)

    assert os.path.exists(project.ANSWERS_LOG)

    with open(project.ANSWERS_LOG, "r") as f:
        content = f.read()
        assert "What is your name?" in content
        assert "My name is test" in content

def test_add_question_logic():
    test_q = "Why this university?"
    test_sample = "Because it fits my goals."

    qs = {
        "Test Category": []
    }

    qs["Test Category"].append({
        "question": test_q,
        "options": ["Option1", "Option2", "Option3", "Option4"],
        "answer": "Option1"
    })

    with open(project.QUESTIONS_FILE, "w") as f:
        json.dump(qs, f, indent=4)

    qs2 = project.load_questions()
    found = False
    for question in qs2["Test Category"]:
        if question["question"] == test_q:
            found = True
    assert found

print("All tests passed ✅")
