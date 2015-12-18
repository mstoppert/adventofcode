import hashlib

input = "ckczppom"

def starts_with_x_zeroes(zeroes, hash):

    starts_with_x_zeroes = True

    for x in range(0, zeroes):
        if hash[x] != "0":
            starts_with_x_zeroes = False
            break

    return starts_with_x_zeroes

counter = 0
hash = ""
hash_found = False

#zeroes = 5 # first star
zeroes = 6 # second star

while(not hash_found):
    counter += 1
    hash = hashlib.md5(input + str(counter)).hexdigest()
    hash_found = starts_with_x_zeroes(zeroes, hash)

print counter, hash
