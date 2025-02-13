
import os
import requests
import argparse
import datetime

# function fetching data to file
def fetch_data_from_api(url, file_path):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            with open(file_path , 'w') as file:
                for item in data: 
                    file.write('{}\n'.format(item))
            print('data fetched and saved to {}'.format(file_path))
        else:
            print('failed to fetch data: status code {}'.format(r.status_code))
    except:
        print('error')


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
def searching_word_in(word, file_path):
    # word that user is looking for
    

    print(word)
    try:
         # opening the file
        with open(file_path) as file:
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
        print("file {} doesn't exist".format(file_path))


def main():

    # implementation of argparse module
    parser = argparse.ArgumentParser(description='file operations with arguments')

    # arguments
    parser.add_argument('file', help='path to the file')
    parser.add_argument('--word', type=str,default=None)
    parser.add_argument('--fetch', action='store_true')
    parser.add_argument('--url', type=str, default=None)

    args = parser.parse_args()

    
    

    # Call the function to fetch data from api to file
    if args.fetch and args.url:
        fetch_data_from_api(args.url, args.file)

    # implementation of datetime module -  display date
    print('Today {} - data save to file {}\n'.format(datetime.date.today() ,args.file))

    # Read the file and display its content
    read_local_file(args.file) 

    # Call the function to search for a word in the file
    if args.word:
        searching_word_in(args.word, args.file)


if __name__ == '__main__':
    main()


