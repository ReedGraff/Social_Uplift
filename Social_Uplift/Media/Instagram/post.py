
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from datetime import datetime

W,H = (1080,1080)

img = Image.new('RGB',(W,H),color = 'black')



draw = ImageDraw.Draw(img)

text = datetime.now().strftime("%H:%M:%S")

font = ImageFont.truetype('./Roboto-Medium.ttf',100)

w,h = draw.textsize(text,font=font)


draw.text(((W-w)/2,(H-h)/2),text,font=font)

img.save('cur_time.jpg')


# In[40]:

"""
import os

from instauto.api.client import ApiClient
from instauto.api import structs as st
from instauto.api.actions import post as ps


if os.path.isfile('./.instauto.save'):
    client = ApiClient.initiate_from_file('./.instauto.save')
else:
    client = ApiClient(user_name="plz.dont.hurt.me.im.sweedish", "123456tagliatelle")
    client.login()
    client.save_to_disk('./.instauto.save')

post = ps.PostFeed(
    path='./cur_time.jpg',
    caption=text
)
resp = client.post_post(post, 80)
print("Success: ", resp.ok)
"""