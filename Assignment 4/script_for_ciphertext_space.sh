#!/bin/bash

cat random_plaintexts.txt | sshpass -p 'cs641a' ssh students@172.27.26.188 &> output_for_ciphertext_space.txt 2> /dev/null
grep -A 1 'Slowly' output_for_ciphertext_space.txt | grep -vE 'Slowly|--' > random_ciphertexts.txt
