#!/bin/bash

cat xor_plaintexts.txt | sshpass -p 'cs641a' ssh students@172.27.26.188 &> output_for_xor_ciphertextx.txt 2> /dev/null
grep -A 1 'Slowly' output_for_xor_ciphertextx.txt | grep -vE 'Slowly|--' > xor_ciphertexts.txt
