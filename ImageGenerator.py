import sys, os
from PIL import Image, ImageDraw, ImageFilter

here = os.path.join( os.path.dirname(os.path.abspath(__file__)))
sys.path.append(here)
import CHARAS

class ImageGenerator:
  def __init__(self):
    #self.base_image = Image.open('data/priconne_base.jpg')

    # base_imageに対する各画像の配置場所を定義
    self.paste_position = {
      0 : [116, 71],
      1 : [201, 71],
      2 : [284, 71],
      3 : [367, 71],
      4 : [452, 71],
      5 : [116, 160],
      6 : [201, 160],
      7 : [284, 160],
      8 : [367, 160],
      9 : [452, 160],
    }


  def gacha_result_generator(self, charactor_list):
    '''
    charactor_listをもとにガチャを回したときの結果画像を作成。
    作成した画像へのパスを返す
    '''

    # ガチャ結果画面の背景となる画像
    base_image = Image.open('data/gacha_result_base.jpg')

    here = os.path.join( os.path.dirname(os.path.abspath(__file__)))

    for i, charactor in enumerate(charactor_list):
      memory_piece_filename = CHARAS.CHARACTOR_PNG[charactor]
      memory_piece_image_path = here + '/data/charactors/memory_piece/' + memory_piece_filename
      memory_piece_image = Image.open(memory_piece_image_path)

      x, y = self.paste_position[i]
      base_image.paste(memory_piece_image, (x, y))

    output_path = here + '/output/gacha_result.jpg'
    base_image.save(output_path, quality=95)

    return output_path

