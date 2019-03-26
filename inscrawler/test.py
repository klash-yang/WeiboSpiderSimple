# from inscrawler.utils import mongodb_operation
# import inscrawler.utils.scrap_info_operation as scrap_info_operation
#
# latest_dataset_id = scrap_info_operation.get_latest_dataset_id('edcee3000', 'Instagram')
# # latest_dataset_id = '270dd05e-48b7-11e9-b4c9-4c3275997092'
# db = mongodb_operation.get_mongo_db()
# records = db['ins'].find({"dataset_id": 'b5538933-4f9c-11e9-9365-1245e3aa661c'}).sort("dateTime", -1)
# for record in records:
#     comments = record['commentMessages']
#     print(666)

import re

result = "nmsltiefive5: @zs1012 您能说点有攻击力的话🐎？给我在这挠痒痒呢贴废物？4 days agoLog in to like or comment.SearchLog In to InstagramLog in to see photos and videos from friends and discover other accounts you'll love.Log InSign UpLog InSign UpAbout usSupportPressAPIJobsPrivacyTermsDirectoryProfilesHashtagsLanguageAfrikaansČeštinaDanskDeutschΕλληνικάEnglishEspañol (España)EspañolSuomiFrançaisBahasa IndonesiaItaliano日本語한국어Bahasa MelayuNorskNederlandsPolskiPortuguês (Brasil)Português (Portugal)РусскийSvenskaภาษาไทยFilipinoTürkçe中文(简体)中文(台灣)বাংলাગુજરાતીहिन्दीHrvatskiMagyarಕನ್ನಡമലയാളംमराठीनेपालीਪੰਜਾਬੀසිංහලSlovenčinaதமிழ்తెలుగుTiếng Việt中文(香港)БългарскиFrançais (Canada)RomânăСрпскиУкраїнська© 2019 Instagram"

result = "yunggoat____: @jztqyn 🔥🔥🔥🔥1 day agoLog in to like or comment.SearchLog In to InstagramLog in to see photos and videos from friends and discover other accounts you'll love.Log InSign UpLog InSign UpAbout usSupportPressAPIJobsPrivacyTermsDirectoryProfilesHashtagsLanguageAfrikaansČeštinaDanskDeutschΕλληνικάEnglishEspañol (España)EspañolSuomiFrançaisBahasa IndonesiaItaliano日本語한국어Bahasa MelayuNorskNederlandsPolskiPortuguês (Brasil)Português (Portugal)РусскийSvenskaภาษาไทยFilipinoTürkçe中文(简体)中文(台灣)বাংলাગુજરાતીहिन्दीHrvatskiMagyarಕನ್ನಡമലയാളംमराठीनेपालीਪੰਜਾਬੀසිංහලSlovenčinaதமிழ்తెలుగుTiếng Việt中文(香港)БългарскиFrançais (Canada)RomânăСрпскиУкраїнська© 2019 Instagram"


result = re.findall(r"(.*)agoLog in to like or comment.SearchLog In to InstagramLog in to see photos and videos from friends and discover other",result)[0]
result = re.findall(r"(.*)\d+ day", result)[0]

print(888)
