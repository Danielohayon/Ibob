import time
# from instapy_cli import client
# import PostPublisher
# import config
# p = PostPublisher.PostPublisher('fdsafdsa', 'test.jpg')
#
# with client(config.username, config.password) as cli:
#     cli.upload("Posts/" + p.image, p.description)
# from instapy_cli import client
# 
# username = 'beautifullyfitpeople'
# password = 'Daniel979'
# cookie = '{COOKIE_STRING_JSON_OBJ}'
# 
# with client(username, password, cookie=cookie) as cli:
#     # get string cookies
#     cookies = cli.get_cookie()
#     print(type(cookies)) # == str
#     print(cookies)
#     # do stuffs with cli
#     ig = cli.api()
#     me = ig.current_user()
#     print(me)

# from instapy_cli import client
#
# username = 'beautifullyfitpeople'
# password = 'Daniel979'
# image = 'Posts/test.jpg'
# text = 'fdasfasfasfad'
#
# with client(username, password) as cli:
#     cli.upload(image, text)

# import time
# from InstagramAPI import InstagramAPI
# # 'DanielDoroDoro'
# # 'Password1'
# # 'beautifullyfitpeople'
# InstagramAPI = InstagramAPI("beautifullyfitpeople", "Daniel979")
# InstagramAPI.login()  # login
#
# time.sleep(5)
# photo_path = 'Posts/test.jpg'
# caption = "Sample photo"
# InstagramAPI.uploadPhoto(photo_path, caption=caption)

import instabot
bot = instabot.Bot(filter_users=False)
bot.login(username='beautifullyfitpeople', password='Daniel979')
bot.follow("ronaldinho")
