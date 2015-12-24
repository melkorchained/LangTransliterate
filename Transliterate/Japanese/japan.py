# -*- coding: UTF-8 -*-

from japmaps import *

class Japanese():

	def jap_transliterate(self,sent):
		romaji = []
		i=len(sent)
		for x in range(0,i):
			if sent[x] in hira_list:
				romaji.append(hira_dict[sent[x]])
			elif sent[x] in hira_special_list:
				romaji.pop()
				key = sent[x-1] + sent[x]
				romaji.append(hira_special_dict[key])
			elif sent[x] == '|':
				romaji.append(' ')
			elif sent[x] in kata_list:
				romaji.append(kata_dict[sent[x]])
			elif sent[x] in kata_special_list:
				romaji.pop()
				key = sent[x-1] + sent[x]
				romaji.append(kata_special_dict[key])
		joined = ''.join(romaji)
		return joined

