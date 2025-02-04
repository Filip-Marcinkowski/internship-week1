
file_path = 'week_1\data.txt'

# function counting file lines

def read_local_file(path):
    try:
        # opening the file
        with open(path) as file:
            #lines number set to 0
            num = 0
            # checking every line and adding line number to it
            for line in file:
                num +=1
                # displaying line with number
                print('{}: {}'.format(num, line.rstrip()))

        print('this file has {} lines'.format(num))
    except:
        print("file {} doesn't exist".format(path))

read_local_file(file_path)

# //////////////////////////////////////////////
print('--------------------------------------')

# function checking if the file has word that user  is looking for
def searching_word_in(path):
    # word that user is looking for
    word = input('what word are you looking for?')

    print(word)
    try:
         # opening the file
        with open(path) as file:
            # seting searching result to false
            found = False
            # checking line by line if word match to the words inside the file
            for line in file:
                # removing extra signs from the line
                line = line.rstrip()
                # check if input word match to the word in the line
                if line == word:
                    print('the file includes {} word'.format(word))
                    found = True
            if found == False:
                print(' there is no {} word in the file'.format(word))    
                    
    except:
        print("file {} doesn't exist".format(path))


searching_word_in(file_path)