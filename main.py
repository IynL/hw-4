import random
class String:
    def __init__(self, Strings):
        self.Strings = Strings
    def printstring(self):
        print(self.Strings)
class Crypto(String):
    def cryptos(self):
        self.words = self.Strings.split()
    def Cryptoshuf(self):
        random.shuffle(self.words)
        for i in range(len(self.words)):
            word_list = list(self.words[i])
            random.shuffle(word_list)
            self.words[i] = ''.join(word_list)
        self.Strings = ' '.join(self.words)
    def printcryptos(self):
        print(self.Strings)
crypto_obj = Crypto("This is a test string")
crypto_obj.printcryptos()
crypto_obj.cryptos()
crypto_obj.Cryptoshuf()
crypto_obj.printcryptos()