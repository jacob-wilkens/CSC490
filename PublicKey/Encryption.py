class Encryption:
    def __init__(self, keys):
        self.b = keys
        
    def EncryptText(self, input):
        result = []
        
        for word in input:
            result.append(self.Encrypt(word))
            
        return result

    def Encrypt(self, char):
        dec = ord(char)
        bin_str = bin(dec)[2:]
        
        while len(bin_str) < 7:
            bin_str = '0' + bin_str
            
        result = 0
        
        for i in range(len(self.b)):
            
            if bin_str[i] == '1':
                result += self.b[i]
                
        return result