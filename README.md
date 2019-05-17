priconne-gacha-simulator
=================

プリコネのガチャシミュレーター

## 環境設定

* version : Python 3.6.2

```shell
git clone https://github.com/rate0621/priconne-gacha-simulator.git
pip install -r requirements.txt
```

これで使えるようになるはず。  

※ mecabのインストールでコケる可能性がある。その場合はmecabの行を消して再度 `pip install -r requirements.txt` を実行で良い（使っていないため）

## 使い方

* GachaSimulation.py

を別のファイルからimportすればOK。  

とりあえずは、 `GachaSimulation.py` の `roll10` のメソッドを叩けば１０連が回せる。  

試しに、  
```shell
python GachaSimulation.py
```

叩いてみるよろし。


### メモ

実際使っているのは、  

* GachaSimulation.py
* Gacha_kai.py
* ImageGenerator.py

なので他のファイルはなくても問題ない。（じゃあ消しとけ）

