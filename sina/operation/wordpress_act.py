from wordpress_xmlrpc import Client, WordPressPost, WordPressTerm
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import taxonomies
import csv


wp = Client('https://www.onedaycp.com/xmlrpc.php', 'poloyc', 'Suckerlove5')

tag = WordPressTerm()
tag.taxonomy = 'category'#这里为category的话插入的是category，为post_tag的话插入的是tag
tag.name = 'My New Tag'
tag.id = wp.call(taxonomies.NewTerm(tag))


post = WordPressPost()
post.title = 'My new title'
post.content = 'This is the body of my new post.'
post.post_status = 'publish'
post.terms_names = {
  'post_tag': ['test', 'firstpost'],
  'category': ['Introductions', 'Tests']
}

# https://my.oschina.net/ranvane/blog/390684