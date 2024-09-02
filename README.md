# Capture the Flag Challenge 

## Overview 
This repository contains the source code and documentation for a multi-stage Capture the Flag (CTF) challenge designed to test and improve participants' skills in cryptography, steganography, and cybersecurity problem-solving.

## Challenge Stages

### Stage 1: Rail-Fence Cipher Encryption
Participants are required to decrypt an encrypted hyperlink using the Rail-Fence Cipher. The encryption process is implemented in `stage_1_encrypt.py`.
hts/cf1wrpescmtp:/t5.odrs.o
The decrypted hyperlink will point to this blog post: 
```bash
https://ctf51.wordpress.com/
``` 

### Stage 2: Cryptographic Questions
Traverse the blog posts in a seqeuntial manner to find out the secret password. 
This stage includes a series of cryptographic puzzles:
1. **Caesar Cipher**: Decrypt a ciphertext with a key of 13.
2. **Steganography**: Answer questions related to steganography.
3. **Password Construction**: Concatenate answers from blog post clues to form a password, then hash it using MD5.

### Stage 3: Steganography
Participants must use the password obtained in Stage 2 to unlock an image. This image has a hidden message embedded using steganography. The encoding process is outlined in `imghide.py`, and the image participants must decode is `sutd_logo-enc.png`.

## Final Flag
The final flag, hidden within the image, is `fcs23{dylanhongjingsarangazaddhruv}`.

## How to Run the Scripts
1. **Stage 1**: Use `stage_1_encrypt.py` to understand the Rail-Fence encryption method.
2. **Stage 2**: Refer to `https://ctf51.wordpress.com/` for the cryptographic puzzles and use `CTF_Final Draft` to validate the answers.
3. **Stage 3**: Participants should decode `sutd_logo-enc.png` after obtaining the password from Stage 2.
All answers are provided in the document `CTF_Final Draft`. 
