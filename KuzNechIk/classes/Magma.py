class Magma:
    def __init__(self, key, text):
        self.P = [
            [12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1],
            [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15],
            [11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0],
            [12, 8, 2, 1, 13, 4, 15, 6, 7, 0, 10, 5, 3, 14, 9, 11],
            [7, 15, 5, 10, 8, 1, 6, 13, 0, 9, 3, 14, 11, 4, 2, 12],
            [5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0],
            [8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7],
            [1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2]]
        self.text = text
        self.key = key
        self.bin_text = self.ToBit(text)
        r = self.ToBit(key)
        self.bin_key = ''
        self.k=0
        for i in range(-1, len(r) * (-1), -1):
            self.bin_key += r[i]

    def ToBit(self, text):
        binary = ""

        for i in text:
            nf = bin(ord(i))[2::]
            while len(nf) < 8:
                nf = '0' + nf
            binary += nf
        return binary

    def ToString(self, strok1):
        binary = strok1
        stork = ""
        d = len(binary) // 8
        for i in range(d):
            k = binary[:8]
            binary = binary[8::]
            la = int(k, 2)
            stork += chr(la)
        return stork

    def g_k(self, stroka32, key):  # 32 bit сложение с ключем и сдвиг на 11 key-32bit
        result = bin(int(stroka32, 2) ^ int(key, 2))[2::]
        while len(result)<32:
            result = '0' + result
        self.k+=1
        print(self.k)
        return self.smesch11(self.t(result))

    def t(self, stroka32):  # замена 32 на вход двоичная строка

        res = ''
        for i in range(len(stroka32) // 4):
            k = int(stroka32[i * 4:i * 4 + 4], 2)
            sol = bin(self.P[-i - 1][k])[2::]
            while len(sol)<4:
                sol = '0' + sol
            res +=sol

        return res

    def Gk(self, stroka64, key):
        a1 = stroka64[:32]
        a0 = stroka64[32::]
        sol = bin(int(self.g_k(a0, key), 2) ^ int(a1, 2))[2::]
        while len(sol) < 32:
            sol = '0' + sol
        res64 = a0 + sol
        return res64

    def G_K(self, stroka64, key):
        a1 = stroka64[:32]
        a0 = stroka64[32::]
        sol = bin(int(self.g_k(a0, key), 2) ^ int(a1,2))[2::]
        while len(sol) < 32:
            sol = '0' + sol
        res64 = sol + a0
        return res64

    def smesch11(self, stroka):
        res = ''
        for i in range(11, 43):

            res += stroka[i % 32]
        return res

    def Crypt(self):
        keys = []
        res = ''
        for i in range(8):
            keys.append(self.bin_key[0 + i * 32:32 + i * 32])
        block64 = []
        while len(self.bin_text) % 64 != 0:
            self.bin_text += '0'
        for i in range(len(self.bin_text) // 64):
            block64.append(self.bin_text[0 + i * 64:64 + i * 64])
        for i in range(len(block64)):
            j = 31
            var = block64[i]

            while j > 0:
                var = self.G_K(var, keys[j % len(keys)])
                j -= 1
                var = self.Gk(var, keys[j % len(keys)])
                j -= 1
            if len(var)!=64:
                print('error' + self.k)
            res += var
        return self.ToString(res)

    def Decrypt(self):
        keys = []

        for i in range(8):
            keys.append(self.bin_key[0 + i * 32:32 + i * 32])
        block64 = []
        while len(self.bin_text) % 64 != 0:
            self.bin_text += '0'
        for i in range(len(self.bin_text) // 64):
            block64.append(self.bin_text[0 + i * 64:64 + i * 64])
        for i in range(len(block64)):
            j = 31
            var = block64[i]
            res = ''
            while j > 0:
                var = self.G_K(var, keys[(-1)*(j % len(keys))])
                j -= 1
                var = self.Gk(var, keys[(-1)*(j % len(keys))])
                j -= 1
            res += var
        return res
