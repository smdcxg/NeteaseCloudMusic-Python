#!/usr/bin/env python3
# -*- coding -*-


from urllib import parse
from .common import *

class playListCore:

    def __init__(self):
        self.bSb5g = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        self.k1x = {}
        self.DD2x = {}
        self.LE4I = 64
        self.bal0x = 64
        self.ciE9v = [82, 9, 106, -43, 48, 54, -91, 56, -65, 64, -93, -98, -127, -13, -41, -5, 124, -29, 57, -126, -101, 47, -1, -121, 52, -114, 67, 68, -60, -34, -23, -53, 84, 123, -108, 50, -90, -62, 35, 61, -18, 76, -107, 11, 66, -6, -61, 78, 8, 46, -95, 102, 40, -39, 36, -78, 118, 91, -94, 73, 109, -117, -47, 37, 114, -8, -10, 100, -122, 104, -104, 22, -44, -92, 92, -52, 93, 101, -74, -110, 108, 112, 72, 80, -3, -19, -71, -38, 94, 21, 70, 87, -89, -115, -99, -124, -112, -40, -85, 0, -116, -68, -45, 10, -9, -28, 88, 5, -72, -77, 69, 6, -48, 44, 30, -113, -54, 63, 15, 2, -63, -81, -67, 3, 1, 19, -118, 107, 58, -111, 17, 65, 79, 103, -36, -22, -105, -14, -49, -50, -16, -76, -26, 115, -106, -84, 116, 34, -25, -83, 53, -123, -30, -7, 55, -24, 28, 117, -33, 110, 71, -15, 26, 113, 29, 41, -59, -119, 111, -73, 98, 14, -86, 24, -66, 27, -4, 86, 62, 75, -58, -46, 121, 32, -102, -37, -64, -2, 120, -51, 90, -12, 31, -35, -88, 51, -120, 7, -57, 49, -79, 18, 16, 89, 39, -128, -20, 95, 96, 81, 127, -87, 25, -75, 74, 13, 45, -27, 122, -97, -109, -55, -100, -17, -96, -32, 59, 77, -82, 42, -11, -80, -56, -21, -69, 60, -125, 83, -103, 97, 23, 43, 4, 126, -70, 119, -42, 38, -31, 105, 20, 99, 85, 33, 12, 125]
        self.bNd2x = 4
        
        i = 0
        l = len(self.bSb5g)
        c = None
        while i < l:
            c = self.bSb5g[i];
            self.DD2x[c] = i
            i += 1

    def bRZ5e(self, j1x):
        r1x = 0
        o1x = []
        j1x = j1x.replace("\n", '').replace("\r", '').replace("=", '')
        i = 0
        l = len(j1x)
        while i < l:
            o1x.append(self.DD2x[j1x[i]] << 2 | self.DD2x[j1x[(i + 1 if i + 1 < l else 0)]] >> 4)
            o1x.append((self.DD2x[j1x[(i + 1 if i + 1 < l else 0)]] & 15) << 4 | self.DD2x[j1x[(i + 2 if i + 2 < l else 0)]] >> 2)
            o1x.append((self.DD2x[j1x[(i + 2 if i + 2 < l else 0)]] & 3) << 6 | self.DD2x[j1x[(i + 3 if i + 3 < l else 0)]])
            i += 4
        bq2x = len(o1x)
        fl4p = len(j1x) % 4
        if fl4p == 2:
            o1x = o1x[0:bq2x - 2]
        if fl4p == 3:
            o1x = o1x[0:bq2x - 1]
        return o1x

    def cvb3x(self, j1x):
        iv5A = self.bRZ5e(j1x)
        dr3x = len(iv5A)
        it5y = None
        r1x = 0
        while True:
            it5y = iv5A[r1x]
            if not it5y:
                break
            if it5y > 128:
                iv5A[r1x] = it5y - 256
            r1x += 1
        return iv5A

    def Cy2x(self, jr5w):
        if jr5w < -128:
            return self.Cy2x(128 - (-128 - jr5w))
        elif jr5w >= -128 and jr5w <= 127:
            return jr5w
        elif jr5w > 127:
            return self.Cy2x(-129 + jr5w - 127)
        else:
            raise Error("1001")
    
    def bNg2x(self, ZW0x):
        if ZW0x == None or len(ZW0x) == 0:
            return ZW0x
        bng5l = ZW0x[:]
        qK8C = []
        bq2x = len(bng5l) / 2
        bi2x = 0
        
        i = 0
        while i < bq2x:
            oA7t = int(bng5l[bi2x], 16) << 4
            bi2x += 1
            oD7w = int(bng5l[bi2x], 16)
            bi2x += 1
            qK8C.append(self.Cy2x(oA7t + oD7w))
            i += 1
        return qK8C

    def bNf2x(self, cI3x):
        if cI3x == None:
            return cI3x
        QE6y = parse.quote(cI3x)
        tQ9H = []
        bNe2x = len(QE6y)
        
        i = 0
        while i < bNe2x:
            if QE6y[i] == "%":
                if (i + 2) < bNe2x:
                    i += 1
                    a = QE6y[i] + ""
                    i += 1
                    a += QE6y[i]
                    tQ9H.append(self.bNg2x(a)[0])
                else:
                    raise Error("1009")
            else:
                tQ9H.append(ord(QE6y[i]))
            i += 1
        return tQ9H

    def ciH9y(self, cS3x, bnx5C, bq2x):
        dB3x = []
        if cS3x == None or len(cS3x) == 0:
            return dB3x
        if len(cS3x) < bq2x:
            raise Error("1003")
        i = 0
        while i < bq2x:
            dB3x[i] = cS3x[bnx5C + i]
            i += 1
        return dB3x
  
    def ciF9w(self, bq2x):
        br2x = []
        i = 0
        while i < bq2x:
            br2x[i] = 0
            i += 1
        return br2x

    def cit9k(self, rf8X):
        bMZ2x = []
        if rf8X == None:
            return self.ciF9w(self.bal0x)
        if len(rf8X) >= self.bal0x:
            return self.ciH9y(rf8X, 0, bal0x)
        else:
            i = 0
            while i < self.bal0x:
                bMZ2x.append(rf8X[i % len(rf8X)])
                i += 1
        return bMZ2x

    def ciq9h(self, baA0x):
        if baA0x == None or len(baA0x) % self.LE4I != 0:
            raise Error("1005")
        bod6X = []
        bi2x = 0
        cip9g = len(baA0x) / self.LE4I
        
        i = 0
        while i < cip9g:
            bod6Xj = []

            j = 0
            while j < self.LE4I:
                bod6Xj.append(baA0x[bi2x])
                bi2x += 1
                j += 1
            
            bod6X.append(bod6Xj[:])
            i += 1
        return bod6X

    def cio9f(self, bMX2x):
        oA7t = urs(bMX2x, 4) & 15
        oD7w = bMX2x & 15
        bi2x = oA7t * 16 + oD7w
        return self.ciE9v[bi2x]

    def bMW2x(self, bou6o):
        if bou6o == None:
            return None
        bMV2x = []
        
        i = 0
        bq2x = len(bou6o)
        while i < bq2x:
            bMV2x.append(self.cio9f(bou6o[i]))
            i += 1
        return bMV2x

    def cjb0x(self, bmE5J, QM6G):
        bmE5J = self.Cy2x(bmE5J)
        QM6G = self.Cy2x(QM6G)
        return self.Cy2x(bmE5J ^ QM6G)

    def bNl2x(self, QL6F, bmT5Y):
        if QL6F == None or bmT5Y == None or len(QL6F) != len(bmT5Y):
            return QL6F
        qK8C = []
        ciX0x = len(QL6F)
        
        i = 0
        bq2x = ciX0x
        while i < bq2x:
            qK8C.append(self.cjb0x(QL6F[i], bmT5Y[i]))
            i += 1
        return qK8C

    def cjr0x(self, jr5w, bi2x):
        return self.Cy2x(jr5w + bi2x)

    def cjl0x(self, ZP0x, bmg5l):
        if ZP0x == None:
            return None
        if bmg5l == None:
            return ZP0x
        qK8C = []
        cjh0x = len(bmg5l)
        
        i = 0
        bq2x = len(ZP0x)
        while i < bq2x:
            qK8C.append(self.cjr0x(ZP0x[i], bmg5l[i % cjh0x]))
            i += 1
        return qK8C

    def cjd0x(self, ZT0x):
        if ZT0x == None:
            return ZT0x
        qK8C = []
        cjc0x = len(ZT0x)
        
        i = 0
        bq2x = cjc0x
        while i < bq2x:
            qK8C.append(self.Cy2x(0 - ZT0x[i]))
            i += 1
        return qK8C

    def bny5D(self, cS3x, bnx5C, rs8k, ciG9x, bq2x):
        if cS3x == None or len(cS3x) == 0:
            return rs8k
        if rs8k == None:
            raise Error("1004")
        if len(cS3x) < bq2x:
            raise Error("1003")
        
        i = 0
        while i < bq2x:
            rs8k.insert(ciG9x + i, cS3x[bnx5C + i])
            i += 1

    def ciJ9A(self, xa0x):
        bc2x = 0
        bc2x += (xa0x[0] & 255) << 24
        bc2x += (xa0x[1] & 255) << 16
        bc2x += (xa0x[2] & 255) << 8
        bc2x += xa0x[3] & 255
        return bc2x

    def bMT2x(self, LL4P, rf8X):
        if LL4P == None:
            return None
        if len(LL4P) == 0:
            return []
        if len(LL4P) % (self.LE4I != 0):
            raise Error("1005")
        rf8X = self.cit9k(rf8X)
        boE6y = rf8X
        boF6z = self.ciq9h(LL4P)
        PZ6T = []
        cii9z = len(boF6z)
        
        i = 0
        while i < cii9z:
           boJ6D = self.bMW2x(boF6z[i])
           boJ6D = self.bMW2x(boJ6D)
           boK6E = self.bNl2x(boJ6D, boE6y)
           cih9Y = self.cjl0x(boK6E, self.cjd0x(boE6y))
           boK6E = self.bNl2x(cih9Y, rf8X)
           self.bny5D(boK6E, 0, PZ6T, i * self.LE4I, self.LE4I)
           boE6y = boF6z[i]
           i += 1

        bMR2x = []
        self.bny5D(PZ6T, len(PZ6T) - self.bNd2x, bMR2x, 0, self.bNd2x)
        bq2x = self.ciJ9A(bMR2x)
        if bq2x > len(PZ6T):
            raise Error("1006")
        qK8C = []
        self.bny5D(PZ6T, 0, qK8C, 0, bq2x)
        return qK8C

    def ciV9M(self, dv3x):
        bNk2x = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        Lz4D = []
        Lz4D.append(bNk2x[urs(dv3x, 4) & 15])
        Lz4D.append(bNk2x[dv3x & 15])
        return "".join(Lz4D)

    def bNh2x(self, tQ9H):
        bq2x = len(tQ9H)
        if tQ9H == None or bq2x < 0:
            return ""
        Lz4D = []

        i = 0
        while i < bq2x:
           Lz4D.append(self.ciV9M(tQ9H[i]))
           i += 1
        return "".join(Lz4D)

    def chR9I(self, bpv6p, J1x):
        bpn6h = self.bMT2x(bpv6p, self.bNf2x(J1x))
        Es2x = self.bNh2x(bpn6h)[:]
        zL1x = []
        bpr6l = len(Es2x) / 2
        bi2x = 0

        i = 0
        while i < bpr6l:
            zL1x.append("%")
            zL1x.append(Es2x[bi2x])
            bi2x += 1
            zL1x.append(Es2x[bi2x])
            bi2x += 1
            i += 1
       
        return "".join(zL1x)

    def cln0x(self, bpv6p, J1x):
        return self.chR9I(self.cvb3x(bpv6p), J1x)

    def decodeURIComponent(self, s=None, key=None):
        return parse.unquote(self.cln0x(s, "param="+key))
