# -*- coding: UTF-8 -*-

class Japanese():
	"""docstring for JTransliterate"f __init__(self, arg):
		super(JTransliterate,.__init__()
		self.arg = arg
	"""
	def transliterate(self,sent):
		hira_dict =	{
						'あ':'a','い':'i','う':'u', 'え':'e','お':'o', 'か':'ka', 'き':'ki', 'こ':'ko',
						'け':'ke', 'く':'ku', 'さ':'sa', 'し':'shi', 'そ':'so', 'せ':'se','す':'su',
						'た':'ta', 'ち':'ti', 'と':'to', 'て':'te', 'つ':'tu', 'な':'na', 'に':'ni', 
						'の':'no','ね':'ne', 'ぬ':'nu', 'は':'ha', 'ひ':'hi', 'ほ':'ho', 'へ':'he',
						'ふ':'hu', 'ま':'ma', 'み':'mi', 'も':'mo', 'め':'me', 'む':'mu', 'や':'ya', 
						'よ':'yo','ゆ':'yu', 'ら':'ra', 'り':'ri', 'ろ':'ro', 'れ':'re', 'る':'ru',
						'わ':'wa', 'ゐ':'wi','を':'wo', 'ゑ':'we', 'ん':'n','が':'ga','ぎ':'gi','ぐ':'gu',
						'げ':'ge','ご':'go','ざ':'za','じ':'zi','ず':'zu','ぜ':'ze','ぞ':'zo','だ':'da',
						'ぢ':'di','づ':'du','で':'de','ど':'do','ば':'ba','び':'bi','ぶ':'bu','べ':'be',
						'ぼ':'bo','ぱ':'pa','ぴ':'pi','ぷ':'pu','ぺ':'pe','ぽ':'po','ゔ':'vu'
					}
		hira_list = 	[
							'あ','い','う','え','お','か','き','こ','け','く','さ','し','そ','せ','す','た','ち','と','て',
							'つ','な','に','ぬ','の','ね','は','ひ','ほ','へ','ふ','ま','み','む','め','も','や','よ','ゆ',
							'ら','り','ろ','れ','る','わ','ゐ','を','ゑ','ん','が','ぎ','ぐ','げ','ご','ざ','じ','ず','ぜ','ぞ',
							'だ','ぢ','ど','で','づ','ば','び','ぶ','べ','ぼ','ぱ','ぴ','ぷ','ぺ','ぽ','ゔ'
						]
		hira_special_dict = 	{
									'きゃ':'kya','きゅ':'kyu','きょ':'kyo','しゃ':'sha','しゅ':'shu','しょ':'sho','ちゃ':'cha','ちゅ':'chu','ちょ':'cho',
									'にゃ':'nya','にゅ':'nyu','にょ':'nyo',
									'ひゃ':'hya','ひゅ':'hyu','ひょ':'hyo','みゃ':'mya','みゅ':'myu','みょ':'myo','りゃ':'rya','りゅ':'ryu','りょ':'ryo',
									'ぎゃ':'gya','ぎゅ':'gyu','ぎょ':'gyo',
									'じゃ':'ja','じゅ':'ju','じょ':'jo','ぢゃ':'ja','ぢ':'ju','ぢ':'jo','':'bya','':'byu','':'byo','':'pya','':'pyu','':'pyo'
								}
		hira_special_list = 	[
									'ゃ','ゅ','ょ','っ','ゝ','ゞ'
								]
		romaji = []
		i=len(sent)
		for x in range(0,i):
			if sent[x] in hira_list:
				romaji.append(hira_dict[sent[x]])
			elif sent[x] in hira_special_list:
				romaji.pop()
				key = sent[x-1] + sent[x]
				romaji.append(hira_special_dict[key])
		joined = ''.join(romaji)
		return joined

