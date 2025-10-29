from lib.models.activity import Activity

def test_activity_initialises():
    activity = Activity(1, 'Paintball')
    assert activity.id == 1
    assert activity.activity == "Paintball"

def test_activities_are_equal():
    activity1 = Activity(1, 'Paintball')
    activity2 = Activity(1, 'Paintball')
    assert activity1 == activity2

def test_if_activity_is_formatted_correctly():
    activity = Activity(1, 'Paintball')
    assert str(activity) == 'Activity(1, Paintball)'