from dalle2 import Dalle2
dalle = Dalle2("sess-m5P8qcas7Sv7A5vq2OiAvw9iJmmpW99IdMv5q0kB") 
generations = dalle.generate_amount("portal to another dimension, digital art",4)
print(generations)