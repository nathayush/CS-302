About decode.py:
    decode.py consists of 6 main functions:
        1. print_tables()
        2. most_common()
        3. least_common()
        4. top_bigrams()
        5. top_trigrams()
        6. decode()
        7. recover_key()
    The first 5 functions display the most frequent pattens and are only meant to help analyse the ciphertext.
    The decode() function reads the key from "key.txt" and applies it to the ciphertext. It then outputs the decrypted/ partially decrypted message to "output.txt". To run, make sure "key.txt" is present. Keep in mind, this is the "inverse" of the actual key.
    The recover_key() function calculates the inverse of the key present in "key.txt" and stores it back in the same file. This yields the ORIGINAL KEY. Run this function only when the inverse key has been found.

About key.txt:
    Each line number in the file represents the letter that is being replaced.
    For example, if E is in line 1,
                          1  -->  a  -->  E
    Keep in mind, there should always be 26 lines/letters in key.txt.
    key.txt starts as, a
                       b
                       c
                       d
                       e
                       f
                       g
                       h
                       i
                       j
                       k
                       l
                       m
                       n
                       o
                       p
                       q
                       r
                       s
                       t
                       u
                       v
                       w
                       x
                       y
                       z (This just means that 'a' will be replaced with 'a', and 'z' with 'z' when it runs initially.)

    Following the manual analysis and taking help from frequency analysis in decode.py, we keep replacing the letters in key.txt with their intended replacement, and eventally arrive at the final "inverse" key.
    Now, we should run recover_key() in decode.py to obtain the original key
