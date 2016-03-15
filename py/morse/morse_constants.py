import csv

class MorseConstants:
    DICT_FILE_NAME = 'morse-dict.csv'

    MULTIPLIER_POINT = 1
    MULTIPLIER_DASH = 3
    MULTIPLIER_SYMBOL_PAUSE = 1
    MULTIPLIER_LETTER_PAUSE = 3
    MULTIPLIER_WORD_PAUSE = 6
    
    DICT = {}

    def __init__(self):
        reader = csv.reader(open(self.DICT_FILE_NAME, 'r'))
        self.DICT = {}
        for row in reader:
            if len(row) < 2:
                continue
            k = row[0]
            v = row[1]
            self.DICT[k] = v
        print self.DICT

    def main():
        print '111'
        print DICT

if __name__ == "__main__":
     main()
