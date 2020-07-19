'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #establishing our base case here
    #if the length of our word is less than 2 then return 0 because there are no more letters in our word that can contain the "th". This will also break our loop once we reduce our word all the way down
    if len(word) < 2:
        return False
    else:
        # if the first 2 letters of our word contain the letters we need call our count function and adding 1 meaning we found 1 case of our "th"
        if word[:2] == 'th':
            return count_th(word[1:]) + 1
        else:
            #if the first 2 letters didnt contain our "th" continue searching after the 2nd letter and repeat the process
            return count_th(word[1:])



our_word = "Tthesis"

print(count_th(our_word))