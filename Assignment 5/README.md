### Assignment 5
To Decipher the AES we simply run [Decipher.ipynb](Decipher.ipynb) file cell by cell to obtain the deciphered password, 
We also have a [script.sh](script.sh) file which connects to the server and gets the ciphertexts corresponding to the plaintexts we provide. It is called from the [Decipher.ipynb](Decipher.ipynb) file. 

You can also run the notebook using the command `make decipher`, and a new file `final_pswd.txt` will be created containing the final password. 
