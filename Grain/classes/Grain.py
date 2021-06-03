import numpy


# 80bit
class Grain:
    def __init__(self, text, key):
        self.text = text
        self.key = key
        self.binary = self.ToBit(self.text)
        self.LFSR = self.binary[:63]
        self.FIll_LFSR()
        self.NFSR = self.ToBit(key)[0:79]
        self.binary = self.binary[64::]
        self.A = {1, 2, 4, 10, 31, 43, 56}

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
            print(chr(la)+ ' - ' + k + ' - '+str(la))
        return stork

    def FIll_LFSR(self):
        # Дополнение LFSR
        for i in range(16):
            self.LFSR += '1'

    def TakeBit(self, bit):
        # Sum B index(i+k) k∈A
        for i in self.A:
            bit = bin(int(bit, 2) + int(self.NFSR[i]))[-1]
        bit = bin(
            int(bit, 2) + int(self.h(self.LFSR[3], self.LFSR[25], self.LFSR[46], self.LFSR[64], self.NFSR[63]), 2))[-1]
        self.Move()
        return bit

    def h(self, x0, x1, x2, x3, x4):

        return bin(int(x1, 2) + int(x4, 2) + (int(bin(int(x0, 2) & int(x3, 2))[2::], 2)) + (
            int(bin(int(x2, 2) & int(x3, 2))[2::], 2)) + int(bin(int(x3, 2) & int(x4, 2))[2::], 2) + int(
            bin(int(x0, 2) & int(x1, 2) & int(x2, 2))[2::], 2) + int(bin(int(x0, 2) & int(x2, 2) & int(x3, 2))[-1],
                                                                     2) +
                   int(bin(int(x0, 2) & int(x2, 2) & int(x4, 2))[-1], 2) + int(
            bin(int(x1, 2) & int(x2, 2) & int(x4, 2))[-1], 2)
                   + int(bin(int(x2, 2) & int(x3, 2) & int(x4, 2))[-1], 2))[-1]

    def Move(self):
        s = self.LFSR[0]
        self.LFSR = self.LFSR[1::] + bin(
            int(s, 2) + int(self.LFSR[62], 2) + int(self.LFSR[51], 2) + int(self.LFSR[38], 2) + int(self.LFSR[23],
                                                                                                    2) + int(
                self.LFSR[13], 2))[-1]
        self.NFSR = self.NFSR[1::] + self.g()


    def g(self):
        return bin(int(self.LFSR[0], 2) + int(self.NFSR[62], 2) + int(self.NFSR[60], 2) + int(self.NFSR[52], 2) +
                   int(self.NFSR[45], 2) +
                   int(self.NFSR[21], 2) + int(self.NFSR[37], 2) + int(self.NFSR[33], 2) +
                   int(self.NFSR[28], 2) + int(self.NFSR[14], 2) + int(self.NFSR[9], 2) +
                   int(self.NFSR[0], 2) + int(bin(int(self.NFSR[63]) & int(self.NFSR[60]))[-1], 2)
                   + int(bin(int(self.NFSR[37]) & int(self.NFSR[33]))[-1], 2)
                   + int(bin(int(self.NFSR[15]) & int(self.NFSR[9]))[-1], 2)
                   + int(bin(int(self.NFSR[60], 2) & int(self.NFSR[52], 2) & int(self.NFSR[45], 2))[-1], 2)
                   + int(bin(int(self.NFSR[33], 2) & int(self.NFSR[28], 2) & int(self.NFSR[21], 2))[-1], 2)
                   + int(
            bin(int(self.NFSR[63], 2) & int(self.NFSR[25], 2) & int(self.NFSR[48], 2) & int(self.NFSR[9], 2))[-1], 2)
                   + int(
            bin(int(self.NFSR[60], 2) & int(self.NFSR[52], 2) & int(self.NFSR[37], 2) & int(self.NFSR[33], 2))[-1], 2)
                   + int(
            bin(int(self.NFSR[63], 2) & int(self.NFSR[60], 2) & int(self.NFSR[23], 2) & int(self.NFSR[15], 2))[-1], 2)
                   + int(bin(
            int(self.NFSR[63], 2) & int(self.NFSR[60], 2) & int(self.NFSR[52], 2) & int(self.NFSR[45], 2) & int(
                self.NFSR[37], 2))[-1], 2)
                   + int(bin(
            int(self.NFSR[33], 2) & int(self.NFSR[28], 2) & int(self.NFSR[21], 2) & int(self.NFSR[15], 2) & int(
                self.NFSR[9], 2))[-1], 2)
                   + int(bin(
            int(self.NFSR[52], 2) & int(self.NFSR[45], 2) & int(self.NFSR[37], 2) & int(self.NFSR[33], 2) & int(
                self.NFSR[28], 2) & int(self.NFSR[21], 2))[-1], 2)
                   )[-1]
