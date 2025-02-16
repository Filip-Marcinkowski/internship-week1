class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path
        

# function checking if the file has word that user  is looking for
    def searching_word_in(self, word):
        # word that user is looking for
        print('-----------------------------')
        print(f'you are looking for {word}')
        print('-----------------------------')
        try:
            # opening the file
            with open(self.file_path) as file:
                # seting searching result to false
                found = False
                num = 0
                # checking line by line if word match to the words inside the file
                for line in file:
                    # removing extra signs from the line
                    line = line.rstrip()
                    num +=1
                    print('{}: {}'.format(num, line))
                    # check if input word match to the word in the line
                    if word in line:
                        print('the file includes {} word in line {}'.format(word, num))
                        found = True
                if found == False:
                    print(' there is no {} word in the file'.format(word))    
                        
        except FileNotFoundError:
            print("file {} doesn't exist".format(self.file_path))