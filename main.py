import argparse
import datetime
from file_manager import FileManager
from api_client import APIClient


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
        api_client = APIClient(args.url, args.file)
        api_client.fetch_data_from_api()

    # implementation of datetime module -  display date
    print('Today {} - data save to file {}\n'.format(datetime.date.today() ,args.file))

    
    # Call the function to search for a word in the file
    if args.word:
        file_manager = FileManager(args.file)
        file_manager.searching_word_in(args.word)


if __name__ == '__main__':
    main()


