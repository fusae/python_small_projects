from flask import Flask, render_template, request, flash, redirect, url_for
from forms import guessBookForm
from pymongo import MongoClient
import datetime

app = Flask(__name__)

app.secret_key = 'You Never Guess know'

client = MongoClient()
db = client['msgBoard']

@app.route('/', methods=['GET', 'POST'])
def index():
    form = guessBookForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            msg_collection = db['msg']
            time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            post = {
                    'name': str(form.name.data),
                    'message': str(form.message.data),
                    'time': time
                    }
            msg_collection.insert(post)

            # let the form become empty after post
            form.name.data = ''
            form.message.data = ''
            return redirect(url_for('index'))

    return render_template('index.html', form=form, msglist=db['msg'].find().sort('time', -1))


if __name__ == '__main__':
    app.run(debug=True)
