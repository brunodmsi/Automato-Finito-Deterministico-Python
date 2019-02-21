import os
import random

def randomize(word, word_size):
	if(word_size != 0):
		for i in range(0, word_size):
			word += str(random.choice([0, 1]))
	return word

def start_with_1(word_size):
	word = '1'
	word += randomize(word[:-1], word_size-1)
	return word

def contains_atleast_1(word_size):
	ok = False
	word = ''
	while(ok):
		word = randomize(word, word_size)
		if('1' in word):
			ok = True
	return word

def start_1_end_0(word_size):
	word = '1'
	word += randomize(word[:-1], word_size-2)
	word += '0'
	return word

def contains_atleast_3_1(word_size):
	word = ''
	word = randomize(word, word_size)
	count = 0
	for i in range(len(word)):
		if(word[i] == '1'): count += 1

	if(count < 3):
		word = contains_atleast_3_1(word_size)
	return word

if __name__ == "__main__":
	string = ''
	out = True
	
	while(out):
		print("AUTOMATO FINITO DETERMINISTICO")
		print("  1 -> w começa com um 1\n  2 -> w contenha ao menos um 1\n  3 -> w começa com um 1 e termina com um 0\n  4 -> w contem pelo menos três 1's\n  5 -> Sair")
		choice = int(input(" Escolha -> "))
		if(choice >= 5): exit()
		word_size = int(input(" Escolha o tamanho da palavra -> "))

		if(choice == 1): string = start_with_1(word_size)
		if(choice == 2): string = contains_atleast_1(word_size)
		if(choice == 3): string = start_1_end_0(word_size)
		if(choice == 4): string = contains_atleast_3_1(word_size)
		
		print(string)
