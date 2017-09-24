from datetime import datetime
from logging import DEBUG

from flask import Flask, render_template, url_for, redirect, flash

from classes import Users
from classes.forms import BookmarkForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '(\x86w\x94Cz\x99\xda\x1e^K=\x06\x9e\xc1(e\xd72\r\x9a\xc9\xc5\xc8'
app.logger.setLevel(DEBUG)


user = Users.User('Piotr', 'Slawek')

bookmarks = []
def store_bookmark(url, description):
    bookmarks.append(dict(
        url = url,
        description = description,
        user = 'Piotr',
        date = datetime.utcnow()
    ))

def new_bookmark(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]

@app.route('/')
@app.route('/index')
def index():
   #return render_template('index.html', user=user)
   return render_template('index.html', new_bookmarks=new_bookmark(5))

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
    #if request.method == 'POST':
        #url = request.form['url']
        #if url == 'test':
        #    return render_template('add.html')
        url = form.url.data
        description = form.description.data
        store_bookmark(url, description)
        app.logger.debug('stored url: {} {}'.format(url, description))
        flash("Stored '{}'".format(description))
        return redirect(url_for('index'))
    else:
        print form.url.errors
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

app.run(host='0.0.0.0', debug=True)


# if __name__ == '__main__':
#     app.run(host='0.0.0.0')

