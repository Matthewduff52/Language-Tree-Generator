import random

class phone:
  def __init__(self, symbols, weights):
    self.symbols = symbols
    self.weights = weights



phones_v = phone(['i','y','ɨ','ʉ','ɯ','u','ɪ','ʏ','ʊ','e','ø','ɘ','ɵ',
                  'ɤ','o','ə','ɛ','œ','ɜ','ɞ','ʌ','ɔ','æ','ɐ','a','ɶ',
                  'ɑ','ɒ'],
                 [0.8714,0.0532,0.1353,0.0133,0.0909,0.8182,0.1641,0.0089,
                  0.1463,0.2749,0.0266,0.0443,0.0089,0.0266,0.2905,0.1685,
                  0.4124,0.0177,0.0333,0.0022,0.0222,0.3592,0.0865,0.0310,
                  0.0576,0.0022,0.0554,0.0421])

phones_c = phone(['p','b','t','d','ʈ','ɖ','c','ɟ','k','g','q','ɢ','ʔ',
                  'm','ɱ','n','ɳ','ɲ','ŋ','ɴ','ʙ','r','ʀ','ⱱ','ɾ','ɽ',
                  'ɸ','β','f','v','θ','ð','s','z','ʃ','ʒ','ʂ','ʐ','ç',
                  'ʝ','x','ɣ','χ','ʁ','ħ','ʕ','h','ɦ','ɬ','ɮ','ʋ','ɹ',
                  'ɻ','j','ɰ','l','ɭ','ʎ','ʟ'],
                 [0.8315,0.6364,0.4013,0.2661,0.0754,0.0599,0.1197,0.0953,
                  0.8936,0.5610,0.1153,0.0310,0.4789,0.9424,0.0022,0.4479,
                  0.0532,0.3126,0.5255,0.0022,0.0022,0.2106,0.0089,0.0022,
                  0.2018,0.0310,0.0865,0.1197,0.3991,0.2106,0.0399,0.0488,
                  0.4346,0.1375,0.4146,0.2506,0.0510,0.0200,0.0244,0.0266,
                  0.2084,0.1220,0.0976,0.0488,0.0421,0.0222,0.6186,0.0355,
                  0.0488,0.0177,0.0133,0.0244,0.0377,0.8381,0.0266,0.3858,
                  0.0599,0.0443,0.0022,])



# generate number of vowels
v_rand_weights = [0.0013,0.0049,0.0165,0.0441,0.0918,0.1499,0.1915,0.1915,
                0.1499,0.0918,0.0441,0.0165,0.0049,0.0013]
v_rand_nums = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]
v = random.choices(v_rand_nums, v_rand_weights)[0]

#generate number of consonants
c_rand_weights = [0.0006,0.0011,0.0019,0.0031,0.0048,0.0074,0.0108,0.0154,
                  0.0211,0.0279,0.0356,0.0440,0.0524,0.0603,0.0669,0.0718,
                  0.0754,0.0744,0.0718,0.0669,0.0603,0.0524,0.0440,0.0356,
                  0.0279,0.0211,0.0154,0.0108,0.0074,0.0048,0.0031,0.0019,
                  0.0011,0.0006,]
c_rand_nums = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
               27,28,29,30,31,32,33,34,35,36,37,38,39]
c = random.choices(c_rand_nums, c_rand_weights)[0]



# generate phoneme list
phoneme_v = []
phoneme_c = []

while v > 0:
    result = random.choices(phones_v.symbols, phones_v.weights)[0]
    if result in phoneme_v:
        pass
    else:
        phoneme_v.append(result)
        v -= 1
# vowel length + tone

while c > 0: #proof of concept - consonants should be more uniform
    result = random.choices(phones_c.symbols, phones_c.weights)[0]
    if result in phoneme_c:
        pass
    else:
        phoneme_c.append(result)
        c -= 1
#use consonants.txt to normalize distribution


# generate OVCs and compile them into a list
Onsets = [] # consonants + affricates + clusters
Vowels = [] # monophthongs + diphthongs + triphthongs
Codas = []  # consonants + affricates + clusters

Vowels.extend(phoneme_v)
#diphthongs

# generate syllable structure
O = ""
V = ""
C = ""
syllable = O + V + C
print(phoneme_c)
print(phoneme_v)
