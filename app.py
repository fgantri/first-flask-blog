from flask import Flask, request, redirect, url_for, render_template
from uuid import uuid4 as gen_uuid

app = Flask(__name__)

blog_posts = []

@app.route('/')
def index():
    # add code here to fetch the job posts from a file
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_post = dict(request.form)
        new_post["id"] = gen_uuid()
        blog_posts.append(new_post)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<uuid:post_id>', methods=['POST'])
def delete(post_id):
    filtered = list(filter(lambda post: post["id"] != post_id, blog_posts))
    blog_posts.clear()
    blog_posts.extend(filtered)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
