from itertools import permutations

palavra = input('Insira a string que deseja permutar...\n\n\n')

print('\n\n\n\n')

def scrambles(word):
    return [''.join(permutation) for permutation in permutations(word)]

def permutations(word):

    if len(word) == 1:
        # the word is one letter long, so this is the base case; there is only one permutation
        return [word]

    # recursively get all permutations of the word after its first letter
    subword_perms = permutations(word[1:])

    # insert the first letter at all possible positions in each of the possible permutations of the rest of the letters
    first_letter = word[0]
    perms = []
    for subword_perm in subword_perms:
        for i in range(len(subword_perm)+1):
            perm = subword_perm[:i] + first_letter + subword_perm[i:]

            # test to make sure permutation wasn't already found (which is possible if some letters are duplicated within the word)
            if perm not in perms:
                perms.append(perm)
    return perms

print(scrambles(palavra))
print('\n\n\n\n\n')
print(permutations(palavra))