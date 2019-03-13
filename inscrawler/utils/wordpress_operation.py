from wordpress_xmlrpc import Client, WordPressPost, WordPressTerm
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost, DeletePost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import taxonomies, media, posts
from wordpress_xmlrpc.compat import xmlrpc_client
import csv
from inscrawler.settings import WORDPRESS_ADDRESS, WORDPRESS_ADMIN_NAME, WORDPRESS_ADMIN_PASSWORD
import inscrawler.utils.scrap_info_operation as scrap_info_operation


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


def post_picture(dataset_id, pic_ins_id, category):
    wp = get_wordpress_client()

    # set to the path to your file
    filename = '../data/edcee3000//image.jpg'

    # prepare metadata
    data = {
        'name': 'picture.jpg',
        'type': 'image/jpeg',  # mimetype
    }

    # read the binary file and let the XMLRPC library encode it into base64
    with open(filename, 'rb') as img:
        data['bits'] = xmlrpc_client.Binary(img.read())

    response = wp.call(media.UploadFile(data))
    pic_wp_id = response['attachment_id']
    scrap_info_operation.insert_pic_record(pic_wp_id=pic_wp_id, pic_ins_id=pic_ins_id, dataset_id=dataset_id,
                                           category=category)
    print(response)


post_picture('weqw')

# {'attachment_id': '429', 'date_created_gmt': <DateTime '20190311T15:56:28' at 0x23c71092860>, 'parent': 0, 'link': 'https://www.onedaycp.com/wp-content/uploads/2019/03/picture-1.jpg', 'title': 'picture.jpg', 'caption': '', 'description': '', 'metadata': {'width': 1080, 'height': 1080, 'file': '2019/03/picture-1.jpg', 'sizes': {'thumbnail': {'file': 'picture-1-150x150.jpg', 'width': 150, 'height': 150, 'mime-type': 'image/jpeg'}, 'medium': {'file': 'picture-1-300x300.jpg', 'width': 300, 'height': 300, 'mime-type': 'image/jpeg'}, 'medium_large': {'file': 'picture-1-768x768.jpg', 'width': 768, 'height': 768, 'mime-type': 'image/jpeg'}, 'large': {'file': 'picture-1-1024x1024.jpg', 'width': 1024, 'height': 1024, 'mime-type': 'image/jpeg'}, 'twentyseventeen-thumbnail-avatar': {'file': 'picture-1-100x100.jpg', 'width': 100, 'height': 100, 'mime-type': 'image/jpeg'}}, 'image_meta': {'aperture': '0', 'credit': '', 'camera': '', 'caption': '', 'created_timestamp': '0', 'copyright': '', 'focal_length': '0', 'iso': '0', 'shutter_speed': '0', 'title': '', 'orientation': '0', 'keywords': []}}, 'type': 'image/jpeg', 'thumbnail': 'https://www.onedaycp.com/wp-content/uploads/2019/03/picture-1-150x150.jpg', 'id': '429', 'file': 'picture.jpg', 'url': 'https://www.onedaycp.com/wp-content/uploads/2019/03/picture-1.jpg'}


# content_list = ['<!-- wp:paragraph -->\n', '<p>评论:</p>\n', '<!-- /wp:paragraph -->\n\n']
# content_list.append('<!-- wp:paragraph -->\n')
# content_list.append('<p>测试图片</p>\n')
# content_list.append('<!-- /wp:paragraph -->\n\n')
# content_list.append('<!-- wp:image {"id":424} -->\n')
# content_list.append('<figure class="wp-block-image"><img src="https://www.onedaycp.com/wp-content/uploads/2019/03/picture-819x1024.jpg" alt="" class="wp-image-424"/></figure>\n')
# content_list.append('<!-- /wp:image -->\n\n')
# content = ''.join(content_list)
#
#
# post_wordpress('Test title', content, 'publish', ['test'], [], ['Introductions'])

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
