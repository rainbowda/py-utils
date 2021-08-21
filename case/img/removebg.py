# encoding=utf-8
from PIL import Image
from removebg import RemoveBg

# removebg涉及到api_key,需要到其官网申请
api_key = 'PysKLJueeoyK9NbJXXXXXXXXX'

def change_bgcolor(file_in, file_out, api_key, color):
  '''
      #必须为png格式
  '''
  p, s = file_in.split(".")
  rmbg = RemoveBg(api_key, 'error.log')
  rmbg.remove_background_from_img_file(file_in)
  file_no_bg = "{}.{}_no_bg.{}".format(p, s, s)
  no_bg_image = Image.open(file_no_bg)
  x, y = no_bg_image.size
  new_image = Image.new('RGBA', no_bg_image.size, color=color)
  new_image.paste(no_bg_image, (0, 0, x, y), no_bg_image)
  new_image.save(file_out)


# 修改照片尺寸
def change_size(file_in, file_out, width, height):
  image = Image.open(file_in)
  resized_image = image.resize((width, height), Image.ANTIALIAS)
  resized_image.save(file_out)


if __name__ == "__main__":
  file_in = 'photo.png'
  file_out = 'photo2.png'
  # 尺寸可按需求自修改
  # change_size(file_in, file_out, width, height)

  # 换背景色
  color = (0, 125, 255)
  change_bgcolor(file_in, file_out, api_key, color)