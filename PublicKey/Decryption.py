class Decryption:
    def __init__(self):
        self.a = [2, 5, 18, 26, 82, 135, 280]
        self.q = 1209
        self.r = 1003
        self.r1 = self.inverse(self.r, self.q)

    def inverse(self, a, n):
        t = 0
        newT = 1

        while a != 0:
            q = n // a
            t, newT = newT, t - q * newT
            n, a = a, n - q * a

        if n > 1: return -1
        if t < 0: t = t + n

        return t
    
    def GeneratePublicKey(self):
        b = []
        
        for i in range(len(self.a)):
            b.append(self.a[i] * self.r % self.q)
            
        return b
    
    def DecryptText(self, cipherText):
        result = ''
        
        for word in cipherText:
            result += self.Decrypt(word)
            
        return result

    def Decrypt(self, value):
        str = ''
        newSum = value * self.r1 % self.q
        
        for i in range(len(self.a) - 1, -1, -1):
            
            if newSum >= self.a[i]:
                newSum -= self.a[i]
                str = '1' + str
                continue
            
            str = '0' + str
            
        return chr(int(str, 2))