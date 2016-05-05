# all the imports

from flask import Flask, request,  redirect, url_for, \
     abort, render_template, flash
from basic_models import Idea, session, Comment




# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


# Routes

@app.route('/home')
def home():
	return render_template('home.html')


# for basic demonstration

@app.route('/share', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        form = {
            'title': request.form['title'],
            'description':  request.form['description']
        }
        entry = Idea(**form)
        entry.save()
    return render_template('share_idea.html')

@app.route('/ideas')
def show_entries():
    entries = session.query(Idea).all()
    # import pdb; pdb.set_trace()
    return render_template('show_ideas.html', entries=entries)

@app.route('/display/<int:post_id>')
def display_ideas(post_id):
    #show the post with the given id
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run(debug=True, port=8000)

