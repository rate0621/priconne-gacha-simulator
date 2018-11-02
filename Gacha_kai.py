import random

class Gacha():
  def __init__(self):

    # キーがそのキャラのレア度を表す
    self.gacha_character_list = {
      3: {
        "アンナ"        : 'anna_crop.PNG',
        "マホ"          : 'maho_crop.PNG',
        "リノ"          : 'rino_crop.PNG',
        "ハツネ"        : 'hatsune_crop.PNG',
        "イオ"          : 'io_crop.PNG',
        "サレン"        : 'saren_crop.PNG',
        "ノゾミ"        : 'nozomi_crop.PNG',
        "ニノン"        : 'ninon_crop.PNG',
        "アキノ"        : 'akino_crop.PNG',
        "マコト"        : 'makoto_crop.PNG',
        "シズル"        : 'shizuru_crop.PNG',
        "モニカ"        : 'monica_crop.PNG',
        "ジータ"        : 'jiita_crop.PNG',
        "アリサ"        : 'arisa_crop.PNG',
        "ジュン"        : 'jun_crop.PNG',
        "キョウカ"      : 'kyouka_crop.PNG',
        "イリヤ"        : 'iriya_crop.PNG',
#        "ペコリーヌ_夏" : 'peco_summer_crop.PNG',
#        "スズメ_夏"     : 'suzume_summer_crop.PNG',
#        "キャル_夏"     : 'kyaru_summer_crop.PNG',
        "トモ"          : 'yajuu.jpeg',
        "クリスティーナ": 'yajuu.jpeg',
      },
      2: {
        "アカリ": 'akari_crop.PNG',
        "ミヤコ": 'miyako_crop.PNG',
        "アヤネ": 'ayane_crop.PNG',
        "ユキ"  : 'yuki_crop.PNG',
        "スズナ": 'suzuna_crop.PNG',
        "カオリ": 'kaori_crop.PNG',
        "ミミ"  : 'mimi_crop.PNG',
        "エリコ": 'eriko_crop.PNG',
        "シノブ": 'shinobu_crop.PNG',
        "マヒル": 'mahiru_crop.PNG',
        "シオリ": 'shiori_crop.PNG',
        "チカ"  : 'tika_crop.PNG',
        "クウカ": 'kuuka_crop.PNG',
        "タマキ": 'tamaki_crop.PNG',
        "ミフユ": 'mihuyu_crop.PNG',
        "ミツキ": 'mitsuki_crop.PNG',
        "ミサト": 'misato_crop.PNG',
        "リン"  : 'rin_crop.PNG',
        "ツムギ": 'tsumugi_crop.PNG',
      },
      1: {
#        "ミフユ_夏"  : 'mihuyu_summer_crop.PNG',
#        "コッコロ_夏": 'coccoro_summer_crop.PNG',
        "ペコリーヌ" : 'pecorine_crop.PNG',
        "コッコロ"   : 'coccoro_crop.PNG',
        "キャル"     : 'kyaru_crop.PNG',
        "ユイ"       : 'yui_crop.PNG',
        "ヒヨリ"     : 'hiyori_crop.PNG',
        "レイ"       : 'rei_crop.PNG',
        "ミソギ"     : 'misogi_crop.PNG',
        "クルミ"     : 'kurumi_crop.PNG',
        "ヨリ"       : 'yori_crop.PNG',
        "スズメ"     : 'suzume_crop.PNG',
        "ユカリ"     : 'yukari_crop.PNG',
        "アオイ"     : 'aoi_crop.PNG',
        "ミサキ"     : 'misaki_crop.PNG',
        "リマ"       : 'rima_crop.PNG',
      }
    }

  def get_list(self, rank):

    if rank in (1, 2, 3):
      return (self.gacha_character_list[rank])
    #elif rank == 2:
    #  return (self.middle_rarity_list)
    #elif rank == 3:
    #  return (self.high_rarity_list)
    else:
      print ("no support")

  def get_rank_normal(self):
    #1~9回目のノーマルガチャ
    num = random.randint(1,100)

    if num <= 80:
      return 1
    elif num >= 81 and num <= 98:
      return 2
    else:
      return 3

  def get_rank_special(self):
    #10回目のガチャ
    num = random.randint(1,100)

    if num <= 98:
      return 2
    else:
      return 3

  def roll_normal_gacha(self):
    character_list = self.get_list(self.get_rank_normal())
    return random.choice(character_list)

  def roll_special_gacha(self):
    character_list = self.get_list(self.get_rank_special())
    return random.choice(character_list)


if __name__ == '__main__':
  g = Gacha()
  print (g.get_list(1))
  #print (g.high_rarity_list[3]['アンナ'])
