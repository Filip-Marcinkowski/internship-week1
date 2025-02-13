
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
    except FileNotFoundError:
        print("file {} doesn't exist".format(path))



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
                    
    except FileNotFoundError:
        print("file {} doesn't exist".format(path))


def main():

    file_path = 'week_1\data.txt'

    # Call the function to display the content of the file
    read_local_file(file_path)
    # Call the function to search for a word in the file
    searching_word_in(file_path)

if __name__ == '__main__':
    main()
    
# week1

