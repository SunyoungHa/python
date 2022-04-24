from name import *

def counter(fname):
    num_words = 0
    num_lines = 0
    num_charc = 0
    upperCount = 0
    lowerCount = 0
    digit = 0
    sentence = 0
    space=0


    with open(fname, 'r') as f:

        for line in f:
            num_lines += 1
            num_charc += len(line)
            num_words += len(line.split())
            space += line.count(' ')
            sentence += line.count('.')
            print("line{}: {}".format(num_lines, line.strip('\n')))

            for case in line:
                if (case.isupper()):
                    upperCount += 1
                elif (case.islower()):
                    lowerCount += 1
            for num in line:
                if num.isdigit():
                    digit += 1
    return num_lines, num_words, upperCount,lowerCount,num_charc,space,digit,sentence


if __name__ == '__main__':
    fname = 'test.txt'
    try:
        name()
        num_lines, num_words, upperCount,lowerCount,num_charc,space,digit,sentence = counter(fname)
        print("Number of lines in text file: ", num_lines)
        print("Number of words in text file: ", num_words)
        print("Number of upper case characters : ", upperCount)
        print("Number of lower case Characters : ", lowerCount)
        print('Number of characters in text file: ', num_charc)
        print('Number of spaces in text file: ', space)
        print('Number of spaces in digit: ', digit)
        print('Number of spaces in sentence: ', sentence)

    except IOError:
        print ("Error: can't open file ", fname)

#
#
#
# from name import *
#
#
# def readFile ():
#     line = ''
#
#     try:
#         file= open('test.txt','r')
#
#     except IOError:
#         print ("Error: can't open file")
#     else:
#         num_words = 0
#         num_lines = 0
#         num_charc = 0
#         num_spaces = 0
#
#
#
#         # for i in text:
#         #     if i.islower():
#         #         count += 1
#         for l in line:
#             numberOfLines += 1
#             print("Line{}: {}".format(numberOfLines, l.strip('\n')))
#                 # numberOfChars += len(l)
#                 # words += len(line.split())
#
#
#
#
#
#         #
#         # line = file.readline()
#         #
#         # numberOfLines = 0
#         # numberOfChars = 0
#         # words = 0
#         # while line !='':
#         #     print("line{}: {}".format(numberOfLines,line.strip('\n')))
#         #     line = file.readline()
#         #     numberOfLines +=1
#         #     numberOfChars += len(line)
#         #     words += len(line.split())
#
#
#
#
#
#         file.close()
#
#     print('Total number of line: ',numberOfLines)
#     print('Total number of words: ',words)
#     print('Total number of Character: ',numberOfChars)
#     print('Total number of islower: ',count)
#
#
# name()
# readFile()