from flask import Flask, render_template, url_for
app = Flask(__name__)
# if __name__ == '__main__':
#     app.run(debug=True)


@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    # print(url_for('static', filename='favicon.ico'))
    return render_template('index.html', name=username, post_id=post_id)


@app.route('/blog')
def blog():
    return 'These are my thoughts on blogs'
