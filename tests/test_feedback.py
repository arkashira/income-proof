from feedback import FeedbackSystem, Feedback

def test_submit_feedback():
    fs = FeedbackSystem()
    feedback = fs.submit_feedback("This is a test feedback")
    assert feedback.id == 1
    assert feedback.message == "This is a test feedback"

def test_get_feedback():
    fs = FeedbackSystem()
    fs.submit_feedback("Feedback 1")
    fs.submit_feedback("Feedback 2")
    feedback_list = fs.get_feedback()
    assert len(feedback_list) == 2
    assert feedback_list[0].id == 1
    assert feedback_list[0].message == "Feedback 1"
    assert feedback_list[1].id == 2
    assert feedback_list[1].message == "Feedback 2"

def test_save_and_load_feedback():
    fs = FeedbackSystem()
    fs.submit_feedback("Feedback 1")
    fs.submit_feedback("Feedback 2")
    fs.save_to_file("feedback.json")
    fs = FeedbackSystem()
    fs.load_from_file("feedback.json")
    feedback_list = fs.get_feedback()
    assert len(feedback_list) == 2
    assert feedback_list[0].id == 1
    assert feedback_list[0].message == "Feedback 1"
    assert feedback_list[1].id == 2
    assert feedback_list[1].message == "Feedback 2"
