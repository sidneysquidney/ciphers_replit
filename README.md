# Caesar, Substitution, and Vinegere Cipher

A small terminal based application to both encode and decode ciphers. 

Caesar - displace each letter in the text by a number (the key). 'hello' becomes 'khoor' with key 3.

Substitution - each letter of the alphabet is substituted for another letter of the alphabet. "don't tell mum" would become "uqh't tkee vyv" if the key was 'lczukgodnamevhqswbityrjpxf'.

Vinegere - The key is a word eg 'cat'. The index of each letter's place in the alphabet is taken: c = 3, a = 1, t = 20; the text is sequentially displaced that number of times. 'attack' will become 'ctmccd'.

Please be patient with this program especially with large inputs. Although saying that, it also works most accurately with larger texts, especially in the case of the vinegere and substitution cipher. It may also take a number of tries. It is not full proof.

I think the most impressive elements of the project are decrypting the Vinegere and Substitution without a key. You have to use a combination of frequency attacks, Index of Coincidence, and hillclimb algorithm.

To manipulate .txt files hard code your variables into cipher_master.py, to run as a small terminal app run cipher_master2.py. You can run at: 
https://replit.com/@sidneysquidney/Caesar-Substitution-and-Vinegere-Cipher#.replit
