from wordpress_xmlrpc import Client, WordPressPost, WordPressTerm
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost, DeletePost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import taxonomies
import csv
from sina.settings import WORDPRESS_ADDRESS, WORDPRESS_ADMIN_NAME, WORDPRESS_ADMIN_PASSWORD


def get_wordpress_client():
    return Client(WORDPRESS_ADDRESS + 'xmlrpc.php', WORDPRESS_ADMIN_NAME, WORDPRESS_ADMIN_PASSWORD)


def post_wordpress(title, content, post_status, comment_status, post_tags, categories):
    wp = get_wordpress_client()
    post = WordPressPost()
    post.title = title
    post.content = content
    post.post_status = post_status
    post.comment_status = comment_status
    post.terms_names = {
        # 'post_tag': ['test', 'firstpost'],
        # 'category': ['Introductions', 'Tests']
        'post_tag': post_tags,
        'category': categories
    }
    return wp.call(NewPost(post))


def delete_wordpress(post_id_list):
    wp = get_wordpress_client()
    total_count = 0
    for id in post_id_list:
        id = tuple(id)[0]
        wp.call(DeletePost(id))
        total_count += 1
    return total_count

# post_wordpress('Test title', 'Test Content', 'publish', ['test'], [], ['Introductions'])

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
