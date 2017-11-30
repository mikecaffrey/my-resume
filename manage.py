from flask_script import Manager
from myresume import app, db, Professor, Course

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    wang = Professor(name='Harry Wang', department='MISY')
    baylor = Professor(name='Mark Baylor', department='BUAD')
    white = Professor(name='Skip White', department='MISY')

    course1 = Course(course_number='MISY 350', title='Web Design', description='web apps.')
    course2 = Course(course_number='MISY 302', title='Sales Management', description='Learning how to run sales processes and sell to clients.')
    course3 = Course(course_number='BUAD 309', title='Systems Analysis and Design', description='Learning Systems Analysis and BPM tools.')
    db.session.add(wang)
    db.session.add(baylor)
    db.session.add(white)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
