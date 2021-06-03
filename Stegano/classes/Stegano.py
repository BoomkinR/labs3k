import string


class Stegano:
    def __init__(self, word, text):
        self.word = word.replace('\n', '')
        self.text = text
        self.str2 = 'eEaATMHpPByKxXoOcC' #'!!!!!!!!!!!!!!!!!!'
        self.str1 = 'еЕаАТМНрРВуКхХоОсС'  # русские

    def tobin(self):
        a = []
        result = ''
        b = ''
        for i in self.word:
            a.append(ord(i))
        for i in a:
            while i > 0:
                b = str(i % 2) + b
                i = i // 2
            result += b
        return result

    def RU_ENG(self):
        k = 0
        i = 0
        newtext = ''
        bin = self.tobin()
        while i < len(self.text):
            if self.text[i] in self.str1 and k < len(bin):
                if bin[k] == '1':
                    newtext += self.str2[self.str1.find(self.text[i])]
                else:
                    newtext += self.text[i]
                k += 1
            else:
                newtext += self.text[i]
            i += 1

        return newtext

    def EndSpace(self):
        start = 0
        k = 0
        end = 0
        oldtext = self.text[27]
        newtext = ''
        bin = self.tobin()
        end = self.text.find('\n', 0)
        while start < len(self.text):
            oldtext = self.text
            if k < len(bin):
                if bin[k] == '1':
                    newtext += self.text[start:end  ] + ' ' + '\n'
                else:
                    newtext += self.text[start:end+1 ]
                k += 1
            else:
                newtext += self.text[start:end+1]
            start = end+1
            end = self.text.find('\n', start+1)

        return newtext

        return 0

    def DoubleSpace(self):
        k = 0
        i = 0
        newtext = ''
        bin = self.tobin()
        while i < len(self.text):
            if self.text[i] ==' ' and k < len(bin):
                if bin[k] == '1':
                    newtext += chr(160)+chr(160)
                else:
                    newtext += self.text[i]
                k += 1
            else:
                newtext += self.text[i]
            i += 1

        return newtext

    def Simbol(self):
        k = 0
        i = 0
        newtext = ''
        bin = self.tobin()
        while i < len(self.text):
            if k < len(bin):
                if bin[k] == '1':
                    newtext += self.text[i] + chr(8204)
                else:
                    newtext += self.text[i]
                k += 1
            else:
                newtext += self.text[i]
            i += 1

        return newtext