#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import random
import math
import base64
from .common import *
from Crypto.Cipher import AES

class Core:

    def __init__(self):
        self.maxDigits = None
        self.ZERO_ARRAY = None
        self.bigZero = None
        self.bigOne = None
        self.biRadixBits = 16
        self.bitsPerDigit = self.biRadixBits
        self.biRadix = 65536
        self.biHalfRadix = urs(self.biRadix, 1)
        self.biRadixSquared = self.biRadix * self.biRadix
        self.maxDigitVal = self.biRadix - 1
        self.lowBitMasks = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535]
        self.highBitMasks = [0, 32768, 49152, 57344, 61440, 63488, 64512, 65024, 65280, 65408, 65472, 65504, 65520, 65528, 65532, 65534, 65535]
        self.hexToChar = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        self.hexatrigesimalToChar = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.barrett = {}

        #self.comment_param_init = {"rid": "", "offset": "0", "total": "true", "limit": "20", "csrf_token": ""}
        #self.comment_param = {"rid": "", "offset": "0", "total": "true", "limit": "20", "csrf_token": ""}
        #self.comment_param_limit_size = {"min":1, "max":100}
        self.third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
        self.second_param = "010001"
        self.forth_param = "0CoJUm6Qyw8W8jud"
        self.iv = '0102030405060708'

    def biHighIndex(self, a):
        b = len(a["digits"]) - 1
        while b > 0 and 0 == a["digits"][b]:
            b -= 1
        return b

    def biShiftRight(self, a, b):
        e = f = g = h = None
        c = math.floor(b / self.bitsPerDigit)
        d = self.BigInt()

        self.arrayCopy(a["digits"], c, d["digits"], 0, len(a["digits"]) - c)
        e = b % self.bitsPerDigit; f = self.bitsPerDigit - e; g = 0; h = g + 1
        while g < len(d["digits"]) - 1:
            d["digits"][g] = urs(d["digits"][g], e) | (d["digits"][h] & self.lowBitMasks[e]) << f
            g += 1; h += 1
        urs(d["digits"][len(d["digits"]) - 1], e); d["isNeg"] = a["isNeg"]
        return d

    def biAdd(self, a, b):
        c = d = e = f = None
        if a["isNeg"] != b["isNeg"]:
            b["isNeg"] = not b["isNeg"]; c = self.biSubtract(a, b); b["isNeg"] = not b["isNeg"]
        else:
            c = self.BigInt(); d = f = 0;
            while f < len(a["digits"]):
                e = a["digits"][f] + b["digits"][f] + d
                c["digits"][f] = 65535 & e
                d = int(e >= self.biRadix)
                f += 1
            c["isNeg"] = a["isNeg"]
        return c

    def biSubtract(self, a, b):
        c = d = e = f = None
        if a["isNeg"] != b["isNeg"]:
            b["isNeg"] = not b["isNeg"]; c = self.biAdd(a, b); b["isNeg"] = not b["isNeg"]
        else:
            c = self.BigInt(); e = f = 0
            while f < len(a["digits"]):
                d = a["digits"][f] - b["digits"][f] + e
                c["digits"][f] = 65535 & d
                if c["digits"][f] < 0:
                    c["digits"][f] += self.biRadix
                e = 0 - int(0 > d)
                f += 1
            if -1 == e:
                e = f = 0
                while f < len(a["digits"]):
                    d = 0 - c["digits"][f] + e
                    c["digits"][f] = 65535 & d
                    if c["digits"][f] < 0:
                        c["digits"][f] += self.biRadix
                    e = 0 - int(0 > d)
                    f += 1
                c["isNeg"] = not a["isNeg"]
            else:
                c["isNeg"] = a["isNeg"]
        return c

    def biCompare(self, a, b):
        if a["isNeg"] != b["isNeg"]:
            return 1 - 2 * int(a["isNeg"])
        c = len(a["digits"]) -1
        while c >= 0:
            if a["digits"][c] != b["digits"][c]:
                return 1 - 2 * int(a["digits"][c] > b["digits"][c]) if a["isNeg"] else 1 - 2 * int(a["digits"][c] < b["digits"][c])
            c -= 1
        return 0

    def arrayCopy(self, a, b, c, d, e):
        g = b; h = d; f = min(b + e, len(a))
        while f > g:
            c[h] = a[g]
            g += 1
            h += 1

    def biMultiplyByRadixPower(self, a, b):
        c = self.BigInt()
        self.arrayCopy(a["digits"], 0, c["digits"], b, len(c["digits"]) - b)
        return c

    def biShiftLeft(self, a, b):
        e = f = g = h = None
        c = math.floor(b / self.bitsPerDigit)
        d = self.BigInt()
        self.arrayCopy(a["digits"], 0 , d["digits"], c, len(d["digits"]) - c)
        e = b % self.bitsPerDigit
        f = self.bitsPerDigit - e
        g = len(d["digits"]) - 1
        h = g - 1
        while g > 0:
            d["digits"][g] = d["digits"][g] << e & self.maxDigitVal | (d["digits"][h] & urs(self.highBitMasks[e], f))
            g -= 1
            h -= 1
        d["digits"][0] = d["digits"][g] << e & self.maxDigitVal; d["isNeg"] = a["isNeg"]
        return d

    def biNumBits(self, a):
        b = self.biHighIndex(a)
        c = a["digits"][b]
        d = (b + 1) * self.bitsPerDigit
        e = d
        while e > d - self.bitsPerDigit and 0 == (32768 & c):
            c <<= 1
            e -= 1
        return e

    def biCopy(self, a):
        b = self.BigInt()
        b["digits"] = a["digits"][0:]
        b["digits"] = a["digits"]
        return b

    def biMultiplyDigit(self, a, b):
        c = d = e = f = None
        result = self.BigInt()
        c = self.biHighIndex(a)
        d = f = 0
        while c >= f:
            e = result["digits"][f] + a["digits"][f] * b + d
            result["digits"][f] = e & self.maxDigitVal
            d = urs(e, self.biRadixBits)
            f += 1
        result["digits"][1 + c] = d
        return result

    def biDivide(self, a, b):
        return self.biDivideModulo(a, b)[0]

    def biDivideModulo(self, a, b):
        f = g = h = i = j = k = l = m = n = o = p = q = r = s = None
        c = self.biNumBits(a)
        d = self.biNumBits(b)
        e = b["isNeg"]
        if d > c:
            if a["isNeg"]:
                f = self.biCopy(self.bigOne); f["isNeg"] = not b["isNeg"]; a["isNeg"] = not 1; b["isNeg"] = not 1; g = self.biSubtract(b, a); a["isNeg"] = not 0; b["isNeg"] = e
            else:
                f = self.BigInt(); g = self.biCopy(a)
            return f, g
        f = self.BigInt(); g = a; h = math.ceil(d / self.bitsPerDigit) - 1; i = 0
        while b["digits"][h] < self.biHalfRadix:
              b = self.biShiftLeft(b, 1)
              i += 1; d += 1
              h = math.ceil(d /self.bitsPerDigit) - 1
        g = self.biShiftLeft(g, i); c += i; j = math.ceil(c / self.bitsPerDigit) - 1; k = self.biMultiplyByRadixPower(b, j - h)
        while -1 != self.biCompare(g, k):
            f["digits"][j - h] += 1
            g = self.biSubtract(g, k)
        l = j
        while l > h:
            m = 0 if l >= len(g["digits"]) else g["digits"][l]
            n = 0 if l - 1 >= len(g["digits"]) else g["digits"][l - 1]
            o = 0 if l - 2 >= len(g["digits"]) else g["digits"][l - 2]
            p = 0 if h >= len(b["digits"]) else b["digits"][h]
            q = 0 if h - 1 >= len(b["digits"]) else b["digits"][h - 1]
            f["digits"][l - h - 1] = self.maxDigitVal if m == p else math.floor((m * self.biRadix + n) / p)
            r = f["digits"][l - h - 1] * (p * self.biRadix + q)
            s = m * self.biRadixSquared + (n * self.biRadix + o)
            while r > s:
                f["digits"][l - h - 1] -= 1
                r = f["digits"][l - h - 1] * (p * self.biRadix | q)
                s = m * self.biRadix * self.biRadix + (n * self.biRadix + o)
            k = self.biMultiplyByRadixPower(b, l - h - 1)
            g = self.biSubtract(g, self.biMultiplyDigit(k, f["digits"][l - h - 1]))
            if g["isNeg"]:
                g = self.biAdd(g, k); f["digits"][l - h - 1] -= 1
            l -= 1
        g = self.biShiftRight(g, i)
        f["isNeg"] = a["isNeg"] != e
        if a["isNeg"]:
            f = self.biAdd(f, self.bigOne) if e else self.biSubtract(f, self.bigOne)
            b = self.biShiftRight(b, i)
            g = self.biSubtract(b, g)
        if 0 == g["digits"][0]:
             if 0 == self.biHighIndex(g):
                  g["isNeg"] = not 1
        return f, g

    def biMultiply(self, a, b):
        d = h = i = k = None
        c = self.BigInt()
        e = self.biHighIndex(a)
        f = self.biHighIndex(b)
        k = 0
        while f >= k:
            d = 0; i = k; j = 0; e >= j;
            while e >= j:
                h = c["digits"][i] + a["digits"][j] * b["digits"][k] + d
                c["digits"][i] = h & self.maxDigitVal
                d = urs(h, self.biRadixBits)
                j += 1; i += 1
            c["digits"][k + e + 1] = d
            k += 1
        c["isNeg"] = a["isNeg"] != b["isNeg"]
        return c

    def biDivideByRadixPower(self, a, b):
        c = self.BigInt()
        self.arrayCopy(a["digits"], b, c["digits"], 0, len(c["digits"]) - b)
        return c

    def biModuloByRadixPower(self, a, b):
        c = self.BigInt()
        self.arrayCopy(a["digits"], 0, c["digits"], 0, b)
        return c

    def BarrettMu_modulo(self, a):
        i = None
        b = self.biDivideByRadixPower(a, self.barrett["k"] - 1)
        c = self.biMultiply(b, self.barrett["mu"])
        d = self.biDivideByRadixPower(c, self.barrett["k"] + 1)
        e = self.biModuloByRadixPower(a, self.barrett["k"] + 1)
        f = self.biMultiply(d, self.barrett["modulus"])
        g = self.biModuloByRadixPower(f, self.barrett["k"] + 1)
        h = self.biSubtract(e, g);
        if h["isNeg"]:
            h = self.biAdd(h, self.barrett["bkplus1"])
        i = self.biCompare(h, self.barrett["modulus"]) >= 0
        while i:
            h = self.biSubtract(h, self.barrett["modulus"])
            i = self.biCompare(h, self.barrett["modulus"]) >= 0
        return h

    def BarrettMu_multiplyMod(self, a, b):
        c = self.biMultiply(a, b)
        return self.barrett["modulo"](c)

    def BarrettMu_powMod(self, a, b):
        d = e = None
        c = self.BigInt()
        c["digits"][0] = 1; d = a; e = b
        while True:
            if 0 != (1 & e["digits"][0]):
                c = self.barrett["multiplyMod"](c, d)
            e = self.biShiftRight(e, 1)
            if 0 == e["digits"][0] and 0 == self.biHighIndex(e):
                break
            d = self.barrett["multiplyMod"](d, d)
        return c

    def BarrettMu(self, a):
        modulus = self.biCopy(a)
        k = self.biHighIndex(modulus) + 1
        b = self.BigInt()
        b["digits"][2 * k] = 1
        mu = self.biDivide(b, modulus)
        bkplus1 = self.BigInt()
        bkplus1["digits"][k + 1] = 1
        modulo = self.BarrettMu_modulo
        multiplyMod = self.BarrettMu_multiplyMod
        powMod = self.BarrettMu_powMod

        self.barrett = {"modulus":modulus, "k":k, "mu":mu, "bkplus1":bkplus1, "modulo":modulo, "multiplyMod":multiplyMod, "powMod":powMod}

    def biHighIndex(self, a):
        b = len(a["digits"]) - 1
        while b > 0 and 0 == a["digits"][b]:
            b -= 1
        return b

    def charToHex(self, a):
        h = None
        b = 48
        c = b + 9
        d = 97
        e = d + 25
        f = 65
        g = 90
        a = int(a)
        if(a >= b and c >= a):
            h = a -b
        elif (a >= f and g >= a):
           h = 10 + a -f
        elif (a >= d and e >= a):
           h =  10 + a -d
        else:
           h = 0

        return h

    def hexToDigit(self, a):
        d = 0
        b = 0
        c = min(len(a), 4)
        while c > d:
            b <<= 4
            b |= self.charToHex(ord(a[d]))
            d += 1
        return b

    def biFromHex(self, a):
        e = 0
        b = self.BigInt()
        c = len(a)
        d = c
        while d > 0:
            f = a[max(d - 4, 0):min(d, c)]
            b['digits'][e] = self.hexToDigit(f)
            d -= 4
            e += 1
        return b

    def RSAKeyPair(self, a, b, c):
        e = self.biFromHex(a)
        d = self.biFromHex(b)
        m = self.biFromHex(c)
        self.BarrettMu(m)
        return {"e":e, "d":d, "m":m, "chunkSize":2 * self.biHighIndex(m), "radix":16, "barrett":self.barrett}

    def setMaxDigits(self, num):
        self.maxDigits = num
        self.ZERO_ARRAY = []
        for i in range(num):
            self.ZERO_ARRAY.append(0)
        self.bigZero = self.BigInt()
        self.bigOne = self.BigInt()
        self.bigOne["digits"][0] = 1

    def BigInt(self, a = None):
        if a:
            return {"digits":None, "isNeg":False}
        else:
            return {"digits":self.ZERO_ARRAY[:], "isNeg":False}

    def random16(self): # 生成16位随机数
        b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        c = ""
        for i in range(int(16)):
            e = random.random() * len(b)
            e = math.floor(e)
            c += b[e:e+1]
        return c

    def c(self, a, b, c):
        d = e = None
        self.setMaxDigits(131)
        d = self.RSAKeyPair(b, "", c)
        e = self.encryptedString(d, a)
        return e

    def encryptedString(self, a, b):
        f = g = h = i = j = k = l = None
        c = []
        d = len(b)
        e = 0
        while d > e:
            c.append(ord(b[e]))
            e += 1
        
        while 0 != len(c) % a["chunkSize"]:
            c.append(0); e += 1

        f = len(c); g = ""; e = 0
        while f > e:
            j = self.BigInt(); h = 0; i = e
            while i < e + a["chunkSize"]:
                j["digits"][h] = c[i]; i += 1
                j["digits"][h] += c[i] << 8; i += 1
                h += 1
            k = a["barrett"]["powMod"](j, a["e"])
            if 16 == a["radix"]:
                l = self.biToHex(k)
            else:
                l = biToString(k, a["radix"])
            g += l + " "
            e += a["chunkSize"]
        return g[0:len(g) - 1]

    def biToHex(self, a):
        d = None
        b = ""
        self.biHighIndex(a)
        d = self.biHighIndex(a)
        while d > -1:
            b += self.digitToHex(a["digits"][d])
            d -= 1
        return b

    def digitToHex(self, a):
        b = 15
        c = ""
        i = 0
        while 4 > i:
            c += self.hexToChar[a & b]
            a = urs(a, 4)
            i += 1
        return self.reverseStr(c)
        
    def reverseStr(self, a):
        c = None
        b = ""
        c = len(a) - 1
        while c > -1:
            b += a[c]
            c -= 1
        return b

    def biToString(self, a, b):
        d = e = None
        c = BigInt()
        c["digits"][0] = b
        d = self.biDivideModulo(a, c)
        e = self.hexatrigesimalToChar[d[1]["digits"][0]]
        while 1 == self.biCompare(d[0], self.bigZero):
            d = self.biDivideModulo(d[0], c)
            digit = d[1]["digits"][0]
            e += self.hexatrigesimalToChar[d[1]["digits"][0]]
        return ("-" if a["isNeg"] else "") + self.reverseStr(e)

    def AES_encrypt(self, text, key, iv):
        pad = 16 - len(text) % 16
        text = text + pad * chr(pad)
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        encrypt_text = encryptor.encrypt(text)
        encrypt_text = base64.b64encode(encrypt_text)
        return bytes.decode(encrypt_text)
    
    #self.comment_param = {"rid": "", "offset": "20", "total": "true", "limit": "20", "csrf_token": ""}
    def get_post_data(self, post_data = {}):
        i = self.random16()
        return {"params":self.AES_encrypt(self.AES_encrypt(json.dumps(post_data), self.forth_param, self.iv), i, self.iv), "encSecKey":self.c(i, self.second_param, self.third_param)}
