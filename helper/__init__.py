import string
import random

def id_generator(size=8, chars=string.ascii_lowercase + string.digits):
   return (''.join(random.choice(chars) for _ in range(size)))