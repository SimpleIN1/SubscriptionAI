from django.test import TestCase
import hashlib

secret_word_2="wmC4=.5,3Wv%r./"


datas = {'AMOUNT': '1499',
 'CUR_ID': '25',
 'MERCHANT_ID': '70161',
 'MERCHANT_ORDER_ID': '568412793',
 'P_EMAIL': 'serbinovichgs@ict.er',
 'P_PHONE': '',
 'SIGN': '11548f8eeef1ebb8a52e5dd009bef4ab',
 'commission': '0',
 'intid': '0'}


data = {'AMOUNT': '1499',
 'CUR_ID': '25',
 'MERCHANT_ID': '70161',
 'MERCHANT_ORDER_ID': '568412793',
 'P_EMAIL': 'serbinovichgs@ict.er',

 # 'P_PHONE': '',
 # 'commission': '0',
 # 'intid': '0'
        }

sign = '11548f8eeef1ebb8a52e5dd009bef4ab'
msg = f"70161:1499:{secret_word_2}:568412793"

hash = hashlib.md5(msg.encode()).hexdigest()
print(hash)
print(sign, "except")
#check sign