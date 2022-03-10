import os
from utils import generate_input_output

# Characteristics choosen for 6 Round DES with 1/16 probability
characteristic1 = "40 08 00 00 04 00 00 00"
characteristic2 = "00 20 00 08 00 00 04 00"

no_of_input_pairs = 10000

# Generate files for Characteristic 1
def create_files_1():
    file = open("plaintext.txt", 'r')
    input_list = [x[:-1] for x in file.readlines()]
    file = open("ciphertext.txt")
    output_list = [x[:-1] for x in file.readlines()]
    return (input_list,output_list)

# Generate files for Characteristic 2
def create_files_2():
    file = open("plaintext1.txt", 'r')
    input_list1 = [x[:-1] for x in file.readlines()]
    file = open("ciphertext1.txt")
    output_list1= [x[:-1] for x in file.readlines()]
    return (input_list1,output_list1)

if not(os.path.exists("plaintext.txt") and os.path.exists("ciphertext.txt")):
    generate_input_output(no_of_input_pairs, characteristic1)
(input_list,output_list)=create_files_1()

if not(os.path.exists("plaintext1.txt") and os.path.exists("ciphertext1.txt")):
    generate_input_output(no_of_input_pairs, characteristic2)
(input_list1,output_list1)=create_files_2()
