# coding:utf-8

# import re   # match the farmat symbols with RegEx

SYMBOL_VALUES = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# SYMBOL_DICT = {'glob': 'I', 'prok': 'V', 'pish': 'X', 'tegj': 'L'}
WORD_DICT = {}
METAL_DICT = {}


class Symbols(object):
    '''
    symbols should only consist of characters in SYMBOL_VALUES.iteritems()
    '''

    def __init__(self, symbols):
        self.symbols = symbols

    def __repr__(self):
        return self.symbols

    def exist(self, para):
        return self.symbols.find(para) != -1

    def exist_batch(self, paras):
        for para in paras:
            if self.symbols.find(para) != -1:
                return True
        return False

    def is_format(self):
        if self.exist_batch(['IIII', 'XXXX', 'CCCC', 'MMMM']):
            return False
        elif self.exist_batch(['IL', 'IC', 'ID', 'IM', 'XD', 'XM']):
            return False
        else:
            for s in self.symbols:
                if s not in SYMBOL_VALUES.iterkeys():
                    print s
                    return False
            return True

    def get_values(self):
        '''
        MMVI is 1000 + 1000 + 5 + 1 = 2006
        MCMXLIV = 1000 + (1000 − 100) + (50 − 10) + (5 − 1) = 1944.
        :return: values of symbols
        '''
        if not self.is_format():
            return 'This is not a format symbol string, return no values. '
        else:
            i = 0
            value = 0
            while i < len(self.symbols) - 1:
                if SYMBOL_VALUES.get(self.symbols[i]) >= SYMBOL_VALUES.get(self.symbols[i + 1]):
                    value += SYMBOL_VALUES.get(self.symbols[i])
                    i += 1
                else:
                    value += SYMBOL_VALUES.get(self.symbols[i + 1]) - SYMBOL_VALUES.get(self.symbols[i])
                    i += 2
            if i < len(self.symbols):
                value += SYMBOL_VALUES.get(self.symbols[i])
            return value


def error():
    error_message = 'I have no idea what you are talking about '
    print(error_message)


def interpret(s):
    question_primitive = 'how much is'
    question_unit = 'how many'
    # a.split('how much is')[-1].split()
    # ['pish', 'tegj', 'glob', 'glob', '?']
    try:
        pass
        if s.startswith(question_primitive):
            alien_list = s.split(question_primitive)[-1].split()
            roman = roman_from_alien_list(alien_list)
        elif s.startswith(question_unit):
            pass
        elif len(s.split('is')) == 2:
            info = s.split('is')
            unit = info[1].split()
            if unit == 1:
                word_roman_dict[info[0]] = info[1]
            elif unit == 2:
                # add to currency_dict
                pass
            else:
                error()
        else:
            error()
            pass
    except Exception, e:
        error()


def test():
    a = Symbols('MMVI')
    b = Symbols('MCMXLIV')
    c = Symbols('XXXXIX')
    print a.get_values()
    print b.get_values()
    print c.get_values()
    print "**************test input ************"

    inputs = '''glob is I
prok is V
pish is X
tegj is L
glob glob Silver is 34 Credits
glob prok Gold is 57800 Credits
pish pish Iron is 3910 Credits
how much is pish tegj glob glob ?
how many Credits is glob prok Silver ?
how many Credits is glob prok Gold ?
how many Credits is glob prok Iron ?
how much wood could a woodchuck chuck if a woodchuck could chuck wood ?'''
    sentences = inputs.splitlines()
    for sentence in sentences:
        if check_sentence_symbol(sentence):
            print check_sentence_symbol(sentence)
            # print "*"*10


def test_input(*args):
    sentence = raw_input("test input")
    if check_sentence_symbol(sentence):
        print check_sentence_symbol(sentence)


if __name__ == '__main__':
    test()
    # test_input()





