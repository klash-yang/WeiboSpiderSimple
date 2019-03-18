from python_wpapi import python_wpapi


# @patch.object(python_wpapi.WpApi, '_request')
def test_delete_media(api):
    api.delete_media(id=434)
    # mock.assert_called_with('http://base.url/wp-json/wp/v2/media/7',
    #     force=False,
    #     method='DELETE')


api = python_wpapi.WpApi('https://www.onedaycp.com', user='poloyc', password='Suckerlove5')
test_delete_media(api)
print(00000)

# test_delete_media(api)
