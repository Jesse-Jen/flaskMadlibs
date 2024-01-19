from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] ='secret'
debug = DebugToolbarExtension(app)

@app.route('/', methods = ['GET'])
def get_answers():
    prompts = story.prompts
    return render_template('questions.html', prompts = prompts)

@app.route('/story', methods = ['GET'])
def full_story():
    text = story.generate(request.args)
    return render_template('story.html', text = text)


if __name__ == '__main__':
    app.run(debug = True)
