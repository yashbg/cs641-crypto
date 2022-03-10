import os
from utils import generate_input_output 

characteristic1 = "40 08 00 00 04 00 00 00"
characteristic2 = "00 20 00 08 00 00 04 00"

#generate_input_output(no_of_input_pairs, characteristic1)
#generate_input_output(no_of_input_pairs, characteristic2)

no_of_input_pairs=10000

if os.path.exists("plaintext.txt") and os.path.exists("ciphertext.txt"):
    file = open("plaintext.txt",'r')
    input_list = [x[:-1] for x in file.readlines()]
    file = open("ciphertext.txt")
    output_list= [x[:-1] for x in file.readlines()]
else:
    generate_input_output(no_of_input_pairs, characteristic1)
    file = open("plaintext.txt",'r')
    input_list = [x[:-1] for x in file.readlines()]
    file = open("ciphertext.txt")
    output_list= [x[:-1] for x in file.readlines()]

if os.path.exists("plaintext1.txt") and os.path.exists("ciphertext1.txt"):
    file = open("plaintext1.txt",'r')
    input_list1 = [x[:-1] for x in file.readlines()]
    file = open("ciphertext1.txt")
    output_list1= [x[:-1] for x in file.readlines()]
else:
    generate_input_output(no_of_input_pairs, characteristic2)
    file = open("plaintext1.txt",'r')
    input_list1 = [x[:-1] for x in file.readlines()]
    file = open("ciphertext1.txt")
    output_list1= [x[:-1] for x in file.readlines()]
