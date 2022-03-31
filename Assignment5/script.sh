cat bash_input.txt | sshpass -p 'cs641a' ssh students@172.27.26.188 &> bash_screen.txt 2> /dev/null
grep -A 1 'Slowly' bash_screen.txt | grep -vE 'Slowly|--' > bash_output.txt 