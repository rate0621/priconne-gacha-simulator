import random

class Gacha():
  def __init__(self):
    self.high_rarity_list = [
      "★★★アンナ",
      "★★★マホ",
      "★★★リノ",
      "★★★ハツネ",
      "★★★イオ",
      "★★★サレン",
      "★★★ノゾミ",
      "★★★ニノン",
      "★★★アキノ",
      "★★★マコト",
      "★★★シズル",
      "★★★モニカ",
      "★★★ジータ",
      "★★★アリサ",
      "★★★ジュン",
      "★★★キョウカ",
      "★★★イリヤ",
      "★★★ペコリーヌ_夏",
#      "★★★スズメ_夏",
      "★★★キャル_夏"
      ]

    self.middle_rarity_list = [
      "★★アカリ",
      "★★ミヤコ",
      "★★アヤネ",
      "★★ユキ",
      "★★スズナ",
      "★★カオリ",
      "★★ミミ",
      "★★エリコ",
      "★★シノブ",
      "★★マヒル",
      "★★シオリ",
      "★★チカ",
      "★★クウカ",
      "★★タマキ",
      "★★ミフユ",
      "★★ミツキ",
      "★★ミサト",
      "★★リン",
      "★★ツムギ"
    ]


    self.low_rarity_list = [
#      "★ミフユ_夏",
#      "★コッコロ_夏",
      "★ペコリーヌ",
      "★コッコロ",
      "★キャル",
      "★ユイ",
      "★ヒヨリ",
      "★レイ",
      "★ミソギ",
      "★クルミ",
      "★ヨリ",
      "★スズメ",
      "★ユカリ",
      "★アオイ",
      "★ミサキ",
      "★リマ"
    ]

  def get_list(self, rank):

    if rank == 1:
      return (self.low_rarity_list)
    elif rank == 2:
      return (self.middle_rarity_list)
    elif rank == 3:
      return (self.high_rarity_list)
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

  def roll_god_gacha(self):
    character_list = self.get_list(3)
    return random.choice(character_list)


