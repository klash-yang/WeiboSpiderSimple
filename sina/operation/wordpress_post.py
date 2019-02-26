from wordpress_xmlrpc import Client, WordPressPost, WordPressTerm
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import taxonomies
import csv
from sina.settings import WORDPRESS_ADDRESS


def post_wordpress(title, content, post_status, post_tags, categories):
    wp = Client(WORDPRESS_ADDRESS + 'xmlrpc.php', 'poloyc', 'Suckerlove5')
    post = WordPressPost()
    post.title = title
    post.content = content
    post.post_status = post_status
    post.terms_names = {
        # 'post_tag': ['test', 'firstpost'],
        # 'category': ['Introductions', 'Tests']
        'post_tag': post_tags,
        'category': categories
    }
    wp.call(NewPost(post))


# post_wordpress('Test title', 'Test Content', 'publish', ['test'], ['Introductions'])

# wp = Client(WORDPRESS_ADDRESS + 'xmlrpc.php', 'poloyc', 'Suckerlove5')
#
# post = WordPressPost()
# post.title = 'My new title'
# post.content = 'This is the body of my new post.'
# post.post_status = 'publish'
# post.terms_names = {
#   'post_tag': ['test', 'firstpost'],
#   'category': ['Introductions', 'Tests']
# }
#
# wp.call(NewPost(post))

# https://my.oschina.net/ranvane/blog/390684
