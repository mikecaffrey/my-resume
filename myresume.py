from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/courses')
def get_all_courses():
    courses =[
    'MISY350',
    'BUAD470',
    'MISY430'
    ]
    return render_template('courses.html', courses = courses)



@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
