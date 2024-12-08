import json

def fetch_blog_posts():
    """Fetches all blog posts from json file"""
    with open("posts.json", "r") as f:
        return json.loads(f.read())


def fetch_blog_post(post_id):
    """Fetches blog post with given id from json file"""
    blog_posts = fetch_blog_posts()
    for post in blog_posts:
        if post["id"] == post_id:
            return post
    return None


def add_blog_post(post):
    """Adds a blog post to json file"""
    blog_posts = fetch_blog_posts()
    blog_posts.append(post)
    with open("posts.json", "w") as f:
        f.write(json.dumps(blog_posts))


def update_blog_post(post_id, updated_post):
    """Updates a blog post in json file"""
    blog_posts = fetch_blog_posts()
    # find index
    post_index = -1
    for i, post in enumerate(blog_posts):
        if post["id"] == post_id:
            post_index = i
    updated_post["id"] = post_id
    blog_posts[post_index] = updated_post
    with open("posts.json", "w") as f:
        f.write(json.dumps(blog_posts))


def delete_blog_post(post_id):
    """Deletes a blog post from json file"""
    blog_posts = fetch_blog_posts()
    blog_posts = list(filter(lambda p: p["id"] != post_id, blog_posts))
    with open("posts.json", "w") as f:
        f.write(json.dumps(blog_posts))
