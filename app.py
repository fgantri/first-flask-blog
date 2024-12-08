from flask import Flask, request, redirect, url_for, render_template
from uuid import uuid4 as gen_uuid
from posts_storage import fetch_blog_posts, add_blog_post, delete_blog_post, update_blog_post, fetch_blog_post

app = Flask(__name__)

@app.route('/')
def index():
    """Returns the index page render showing all blog posts"""
    return render_template('index.html', posts=fetch_blog_posts())


@app.route('/add', methods=['GET', 'POST'])
def add():
    """GET: Renders a form to create a blog post, POST: stores post in json file
    and redirects to index"""
    if request.method == 'POST':
        new_post = dict(request.form)
        new_post["id"] = str(gen_uuid())
        add_blog_post(new_post)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<string:post_id>', methods=['POST'])
def delete(post_id):
    """Deletes post from json file and redirects to index"""
    delete_blog_post(post_id)
    return redirect(url_for('index'))


@app.route('/update/<string:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """GET: Renders a form to update a blog post, POST: updates post in json file
    and redirects to index"""
    post_to_update = fetch_blog_post(post_id)
    if request.method == 'POST':
        updated_post = dict(request.form)
        update_blog_post(post_id, updated_post)
        return redirect(url_for('index'))
    return render_template('update.html', post=post_to_update)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
