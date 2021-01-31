import argparse as ap
import hashlib

parser = ap.ArgumentParser(description="A simple password cracker")

parser.add_argument('hashfile', help="Text file containing hash to be cracked.")

parser.add_argument('wordlist', help="path to the desired wordlist")

args = parser.parse_args()

def crackpassword(hash, wordlist):
    hashfile = open(hash, "r") # ! open hash file

    hash = hashfile.read(1000) # ! get hash and save as variable
    print(f"found {hash} hash")

    hashfile.close()

    wordlist = open(wordlist, "r") # ! open wordlist 

    count = 0

    for line in wordlist: # ! Iterate through wordlist convert to hash and compare to desired hash
        count += 1

        hashedline = hashlib.md5(line.encode())
        actualhash = hashedline.hexdigest()

        if str(actualhash) == hash:
            print(f'password is {line}')

    wordlist.close()

if __name__ == '__main__':
    print(crackpassword(args.hashfile, args.wordlist))