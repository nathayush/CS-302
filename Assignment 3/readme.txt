Attached programs: keygen.py, encrypt.py, decrypt.py
Also attached (sample text file): message.txt

Process:
    1. To GENERATE SECRET KEY AND PRIVATE KEY, run keygen.py (eg. 'python keygen.py')

        This will generate two files:
            a. sk.txt- This file contains the secret key
            b. pk.pem- This file contains the public key

    2. To ENCRYPT A MESSAGE, run encrypt.py (with argument: <message_file>, eg. 'python encrypt.py message.txt')

        This program will read two files:
            1. pk.pem
            2. message.txt

        It will also generate one file:
            1. ciphertext.txt

    3. To DECRYPT A CIPHERTEXT, run decrypt.py (eg. 'python decrypt.py')

        This program will read three files:
            1. sk.txt
            2. pk.pem
            3. ciphertext.txt

        This program will generate one file:
            1. plaintext.txt
