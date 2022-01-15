from random import choice

class Termoo:
    def __init__(self):
        self.history = []
        self.choice()
    
    def choice(self):
        with open('bot/termoo.csv') as e:
            self.words = set(e.readlines())
        self.word = choice(list(self.words)).strip()
        self.over = False
        
    def validate(self, guess):
        return guess in self.words

    def make_guess(self, guess):
        res = ['G' if g == r else '' for g, r in zip(guess, self.word)]
        setr = [r for g, r in zip(guess, self.word) if g != r]
        self.over = True
        for k in range(len(guess)):
            if not res[k]:
                self.over = False
                if guess[k] in setr:
                    res[k] = 'Y'
                    setr.remove(guess[k])
                else:
                    res[k] = 'R'
        self.history.append((guess, res))

    def output_tuple(self, word, lis):
        fword = ''.join([f':regional_indicator_{x}: ' for x in word])
        flis = ''.join([emoji(x) for x in lis])
        return f'\n> {fword} \n> {flis}\n'.lower()

    def e2e(self, guess):
        if not(self.validate(guess)):
            return "invalid word"
        self.make_guess(guess)
        ret = ''.join([self.output_tuple(x, y) for x, y in self.history])
        return ret

def emoji(ch): 
    colors = {'R':'red', 'G': 'green', 'Y':'yellow'}
    return ':{}_circle: '.format(colors.get(ch.upper(), ''))
