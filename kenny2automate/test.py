import os
print(__file__)
print(os.path.dirname(__file__))
print(os.listdir(os.path.dirname(__file__) or '.'))
