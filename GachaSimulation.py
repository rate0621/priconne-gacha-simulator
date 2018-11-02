import random
import sys, os

here = os.path.join( os.path.dirname(os.path.abspath(__file__)))
sys.path.append(here)
import ImageGenerator
#import Gacha
import Gacha_kai

class GachaSimulation(Gacha_kai.Gacha):
  def __init__(self):
    super().__init__()


  def roll_normal_gacha(self):
    character_list = self.get_list(self.get_rank_normal())
    chara_name, chara_img_name = random.choice(list(character_list.items()))

    #return random.choice(character_list)
    return chara_name, chara_img_name

  def roll_special_gacha(self):
    character_list = self.get_list(self.get_rank_special())
    chara_name, chara_img_name = random.choice(list(character_list.items()))

    #return random.choice(character_list)
    return chara_name, chara_img_name

  def is_completed(self, c_list):
    for key in c_list:
      if c_list[key] == 0:
        return False

    return True

  def roll_gacha_until_complete(self):
    #獲得したキャラを記憶しておく辞書作成
    self.got_character_list = {}

    #初期化
    for character in self.get_list(1):
      self.got_character_list[character] = 0

    for character in self.get_list(2):
      self.got_character_list[character] = 0

    for character in self.get_list(3):
      self.got_character_list[character] = 0

    gacha_count = 1

    while(1):
      #ノーマルガチャを9回
      for var in range(0, 9):
        chara_name, dummy = self.roll_normal_gacha()
        self.got_character_list[chara_name] += 1

      #10回目のガチャを1回
      chara_name, dummy = self.roll_special_gacha()
      self.got_character_list[chara_name] += 1

      if not self.is_completed(self.got_character_list):
        gacha_count += 1
        continue

      break

    return gacha_count


  def roll10(self):
    get_chara_list = []

    for var in range(0, 9):
      get_chara_list.append(self.roll_normal_gacha())

    get_chara_list.append(self.roll_special_gacha())

    return get_chara_list

  def challenge(self, target_chara_name):
    is_find = self.characterNameCheck(target_chara_name)

    if is_find:
      challenge_count = self.letsChallenge(target_chara_name)
      message = 'あなたが' + target_chara_name + 'を引くまでにかかった金額は、' + str(challenge_count * 3000) + '円で、' + str(challenge_count * 10) + '連しました。お疲れ様でした！'

    else:
      challenge_count = 0
      message = 'そんなキャラクターはいないみたいですよ？フルネームでもう一度入れてみてください。'

    return challenge_count, message


  def characterNameCheck(self, target_chara_name):
    for rank in self.gacha_character_list:
      if target_chara_name in self.gacha_character_list[rank].keys():
        return True

    return False
    


  def letsChallenge(self, target_chara_name):
    get_chara_list = []

    gacha_count = 1
    is_get = 0
    while(1):
      get_chara_list = self.roll10()
      for chara_name, chara_image_name in get_chara_list:
        if chara_name == target_chara_name:
          return gacha_count
          #is_get = 1
          #break

      gacha_count += 1


if __name__ == '__main__':
  gs = GachaSimulation()

#  print (gs.roll_normal_gacha())
  challenge_count, message = gs.challenge('クリスティーナ')

#  for i in range(0, 100000):
#    completed_count = gs.roll_gacha_until_complete()
#    print (completed_count)

#  get_chara_list = gs.roll10()
#  ig = ImageGenerator.ImageGenerator()
#  print (ig.gacha_result_generator(get_chara_list))

