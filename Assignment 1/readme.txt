Attached programs: keygen.py, encode.py, decode.py
Also attached (sample text files): key.txt, message.txt, ciphertext.txt, output.txt

Process:
  1.To GENERATE A KEY, run keygen.py (with 'm'/size as a command line argument). This will generate an mxm matrix and store it in ‘key.txt’.
    example: python keygen.py 7

  2.To ENCRYPT A MESSAGE, run encode.py (with 2 arguments: <message_file>, <key_file>)
    example: python encode.py message.txt key.txt

        The message is encrypted in the following manner:
            For each character in the message.txt, we get its ascii value using ord(). The ascii values of [a to z] in python, range from 97 to 122. Hence we do ord(ch) - 97. This makes a —> 0, b —> 1 and so on. We keep storing these values in a row matrix.
            Thereafter, we read the key from key.txt and store it in a square matrix.
            Multiplying the arrays happens as follows:
                According to the size of the key, we pad the message array so that multiplying these two arrays (matrices) is possible.
                We split the padded message array into multiple arrays of size that is equal to the dimension size of the key. Then, we multiply the individual pieces of the message with the key and keep appending to a ciphertext array.
            This ciphertext array is our encrypted message, and is in the Z26 space. It is stored in ciphertext.txt

  3.To DECRYPT A CIPHERTEXT, run decode.py (with 2 arguments: <ciphertext_file>, <key_file>)
    example: python decode.py ciphertext.txt key.txt

        The ciphertext is decrypted in the following manner:
            We read the ciphertext and key from ciphertext.txt and key.txt respectively and store them in individual arrays/matrices.
            The idea behind decrypting is to multiply the ciphertext with the inverse of the key.
            The inverse of the key is calculated as follows:
                We calculate the determinant of the original key, and calculate its modular multiplicative inverse under Z26.
                At the same time, we also find the adjoint matrix of the key.
                The inverse of the key is calculated by multiplying [the adjoint matrix] with [the modular inverse of the original determinant].
            This inverse matrix has the same dimensions as the original key.
            Since we padded the message during encryption, the size of ciphertext is divisible by the dimension size of the inverse matrix. So, we multiply these two matrices in a similar manner (by breaking the ciphertext into arrays of size 'm')
            The output is our decrypted message, and again is in the Z26 space. We convert it back into alphabets by adding 97 (ascii value of 'a') and using chr().
            We store that string in output.txt and should be the same as the original message, along with some padding.
            If the decrypted message is not the same, please try generating another key.
