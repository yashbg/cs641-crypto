#!/bin/bash

cat plaintext.txt | sshpass -p 'cs641a' ssh students@172.27.26.188 &> output.txt 2> /dev/null