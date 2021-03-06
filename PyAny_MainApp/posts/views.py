from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from PyAny_MainApp import db
from PyAny_MainApp.models import BlogPost
from PyAny_MainApp.posts.forms import BlogPostForm
from datetime import datetime

blog_posts = Blueprint('blog_posts',__name__)

# Create Blog Post
@blog_posts.route('/create_post',methods=['GET','POST'])
@login_required
def create_post():
  form = BlogPostForm()
  username = current_user.username
  if form.validate_on_submit():
    blog_post = BlogPost( title = form.title.data,
                          text=form.text.data,
                          user_id=current_user.id,
                          timestamp=datetime.now(),
                          )
    db.session.add(blog_post)
    db.session.commit()
    flash('Blog post created!')
    return redirect(url_for('core.index'))

  return render_template('create_post.html',form=form,username=username)

# View(Read) Blog Post
@blog_posts.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
  blog_post = BlogPost.query.get_or_404(blog_post_id)
  return render_template('blog_post.html',
                         title=blog_post.title,
                         timestamp=blog_post.timestamp,
                         post=blog_post
                        )

# Update Blog Post
@blog_posts.route('/<int:blog_post_id>/update_post',methods=['GET','POST'])
@login_required
def update_post(blog_post_id):
  blog_post = BlogPost.query.get_or_404(blog_post_id)

  if blog_post.author != current_user:
    abort(403)

  form = BlogPostForm()

  if form.validate_on_submit():
    blog_post.title = form.title.data
    blog_post.text = form.text.data
    db.session.commit()
    flash('Blog post updated!')
    return redirect(url_for('blog_posts.blog_post',blog_post_id=blog_post.id))

  elif request.method == 'GET':
    form.title.data = blog_post.title
    form.text.data = blog_post.text

  return render_template('create_post.html',
                         form=form,
                         title='Updating'
                         )

# Delete Blog Post
@blog_posts.route('/<int:blog_post_id>/delete_post',methods=['POST'])
@login_required
def delete_post(blog_post_id):
  blog_post = BlogPost.query.get_or_404(blog_post_id)

  if blog_post.author != current_user:
    abort(403)
  
  db.session.delete(blog_post)
  db.session.commit()
  flash('Blog post deleted!')
  return redirect(url_for('core.index'))