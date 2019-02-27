from collections import OrderedDict

cihuibiao = OrderedDict()


cihuibiao['loop'] = 'iterations of the code'
cihuibiao['if'] = 'tiaojian yuju if-elif-else'
cihuibiao['dictionary'] = 'key-value pair'
cihuibiao['sohu'] = 'a website'
cihuibiao['dell'] = 'computer'
cihuibiao['tianchao'] = 'You got it!'

for key,value in cihuibiao.items():
    print(key + ": " + value)