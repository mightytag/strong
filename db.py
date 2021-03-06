from dotenv import load_dotenv
load_dotenv()  # noqa
from app.models import Equipment, Exercise_Type, Exercise, Instruction, Muscle, Exercise_Muscle, User
from app.data.index import equipment, exercise_types, exercises_muscles, exercises, instructions, muscles
from app import app, db

equipment = equipment.seeds
exercise_types = exercise_types.seeds
exercises_muscles = exercises_muscles.seeds
exercises = exercises.seeds
instructions = instructions.seeds
muscles = muscles.seeds


def seedDb():
    for seed in equipment:
        name = seed['name']
        db.session.add(Equipment(name=name))
        db.session.commit()

    for seed in exercise_types:
        db.session.add(Exercise_Type(type=seed['type']))
        db.session.commit()

    for seed in exercises:
        if 'equipmentId' not in seed.keys():
            db.session.add(Exercise(name=seed['name'], bbPageUrl=seed['bbPageUrl']))
        else:
            db.session.add(Exercise(name=seed['name'], bbPageUrl=seed['bbPageUrl'], equipmentId=seed['equipmentId']))
        db.session.commit()

    for seed in muscles:
        db.session.add(Muscle(name=seed['name']))
        db.session.commit()

    for seed in instructions:
        db.session.add(Instruction(instruction=seed['instruction'], exerciseId=seed['exerciseId']))
        db.session.commit()

    for seed in exercises_muscles:
        db.session.add(Exercise_Muscle(exerciseId=seed['exerciseId'], muscleId=seed['muscleId']))
        db.session.commit()


with app.app_context():
    # seedDb()
    db.session.add(User(firstName='Matt', lastName='Ramotar', username='mattramotar', email='matt.ramotar@jhu.edu', password='password'))
    db.session.commit()
