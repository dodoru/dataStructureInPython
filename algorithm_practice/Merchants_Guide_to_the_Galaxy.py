# coding:utf-8

# import re   # match the farmat symbols with RegEx

SYMBOL_VALUES = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# SYMBOL_DICT = {'glob': 'I', 'prok': 'V', 'pish': 'X', 'tegj': 'L'}
WORD_SYMBOL_DICT = {}  # the word index different symbol
METAL_PRICE_DICT = {}  # the price of different metal


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
    '''
    :param s: input sentence
    :return: if question then answer with print , else insert into dict
    '''
    question_counts = 'how much is'
    question_amount = 'how many Credits is'

    if s.startswith(question_counts) and s.endswith('?'):
        # eg: how much is pish tegj glob glob ?
        word_para = s.split(question_counts)[-1]
        word_list = word_para.split()[:-1]  # ignore the '?'
        symbols = ''
        for word in word_list:
            symbols += WORD_SYMBOL_DICT.get(word)
        counts = Symbols(symbols).get_values()
        print u"{0} is {1}".format(word_para[:-2], counts)

    elif s.startswith(question_amount) and s.endswith('?'):
        # eg: how many Credits is glob prok Gold ?
        word_para = s.split(question_amount)[-1]
        word_list = word_para.split()[:-1]  # [-2]:metal name ;[-1]:? -> ignore
        symbols = ''
        for word in word_list[:-1]:  # now word_list[-1] is metal name
            symbols += WORD_SYMBOL_DICT.get(word)
        counts = Symbols(symbols).get_values()
        price = METAL_PRICE_DICT.get(word_list[-1])
        amount = int(counts * price)  # output type: int
        print u"{0} is {1} Credits ".format(word_para[:-2], amount)

    elif not s.endswith('?'):
        # pish 'is' so ,can't judge by s.split('is')
        # if assertive sentence , then add info into dict
        info = s.split()
        isn = -1  # index of 'is' but not in 'pish'
        try:
            isn = info.index('is')
        except:
            pass

        if len(info) == 3 and isn == 1:
            # eg : pish is X , add to WORD_SYMBOL_DICT
            WORD_SYMBOL_DICT[info[0]] = info[2]

        elif len(info) > 3 and isn > 1:
            # eg : glob glob Silver is 34 Credits , add to METAL_PRICE_DICT
            metal = info[isn - 1]
            amount = float(info[isn + 1])
            symbols = ''
            for word in info[:isn - 1]:
                symbols += WORD_SYMBOL_DICT.get(word)
            counts = Symbols(symbols).get_values()
            price = amount / counts  # the price of metal should be float
            METAL_PRICE_DICT[metal] = price

        else:
            error()
    else:
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
        interpret(sentence)
        print "  " * 20


def test_input(*args):
    sentence = raw_input("test input")
    interpret(sentence)


if __name__ == '__main__':
    test()
    # test_input()





