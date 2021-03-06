# -*- coding: utf-8 -*-

hira_dict =	{
			'あ':'a','い':'i','う':'u', 'え':'e','お':'o', 'か':'ka', 'き':'ki', 'こ':'ko',
			'け':'ke', 'く':'ku', 'さ':'sa', 'し':'shi', 'そ':'so', 'せ':'se','す':'su',
			'た':'ta', 'ち':'ti', 'と':'to', 'て':'te', 'つ':'tsu', 'な':'na', 'に':'ni',
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

kata_dict = 	{
			'ア':'a','イ':'i','ウ':'u','エ':'e','オ':'o','カ':'ka','キ':'ki','ク':'ku',
			'ケ':'ke','コ':'ko','サ':'sa','シ':'shi','ス':'su','セ':'se','ソ':'so','タ':'ta',
			'チ':'ti','ツ':'tsu','テ':'te','ト':'to','ナ':'na','ニ':'ni','ヌ':'nu','ネ':'ne',
			'ノ':'no','ハ':'ha','ヒ':'hi','フ':'fu','ヘ':'he','ホ':'ho','マ':'ma','ミ':'mi',
			'ム':'mu','メ':'me','モ':'mo','ヤ':'ya','ユ':'yu','ヨ':'yo','ラ':'ra','リ':'ri',
			'ル':'ru','レ':'re','ロ':'ro','ワ':'wa','ヲ':'wo','ン':'nn','ガ':'ga','ギ':'gi',
			'グ':'gu','ゲ':'ge','ゴ':'go','ザ':'za','ジ':'zi','ズ':'zu','ゼ':'ze','ゾ':'zo',
			'ダ':'da','ヂ':'ji','ヅ':'zu','デ':'de','ド':'do','バ':'ba','ビ':'bi','ブ':'bu',
			'ベ':'be','ボ':'bo','パ':'pa','ピ':'pi','プ':'pu','ペ':'pe','ポ':'po'
		}

kata_list = 	[
			'ア','イ','ウ','エ','オ','カ','キ','ク','ケ','コ','サ','シ','ス','セ','ソ',
			'タ','チ','ツ','テ','ト','ナ','ニ','ヌ','ネ','ノ','ハ','ヒ','フ','ヘ','ホ',
			'マ','ミ','ム','メ','モ','ヤ','ユ','ヨ','ラ','リ','ル','レ','ロ','ワ','ヲ',
			'ン','ガ','ギ','グ','ゲ','ゴ','ザ','ジ','ズ','ゼ','ゾ','ダ','ヂ','ズ','デ',
			'ド','バ','ビ','ブ','ベ','ボ','パ','ピ','プ','ペ','ポ'
		]

kata_special_dict = 	{
				'キャ':'kya','キュ':'kyu','キョ':'kyo','ギャ':'gya','ギュ':'gyu','ギョ':'gyo','ニャ':'nya',
				'ニュ':'nyu','ニョ':'nyo','ヒャ':'hya','ヒュ':'hyu','ヒョ':'hyo','ビャ':'bya','ビュ':'byu',
				'ビョ':'byo','ピャ':'pya','ピュ':'pyu','ピョ':'pyo','ミャ':'mya','ミュ':'myu','ミョ':'myo',
				'リャ':'rya','リュ':'ryu','リョ':'ryo','ジャ':'ja','ジュ':'ju','ジェ':'je','ジョ':'jo',
				'チャ':'cha','チュ':'chu','チェ':'che','チョ':'cho','シャ':'sha','シュ':'shu','シェ':'she',
				'ショ':'sho','ウィ':'wi','ウェ':'we','ヂュ':'wo','フィ':'fi','フェ':'fe','フォ':'fo','フュ':'fyu'
			}

kata_special_list = 	[
				'ッ','ャ','ュ','ョ','ー','ヽ','ェ','ィ','ォ'
			]
