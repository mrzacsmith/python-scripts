__author__ = 'silverback'

# file that you want to use for word count
fileName = 'yesno.txt'


def main():
    # read file
    file = open(fileName, 'r')
    lines = file.readlines()
    file.close()

    # find the word pattern
    countYes = 0
    countNo = 0


    for line in lines:

        # ensure all words are the same case, and strip out extra space between lines
        # line = line.lower()
        line = line.strip().lower()
        # print(line)

        if line.find("yes") != -1 and len(line) == 3: # limit the character length to match the word length
            countYes += 1
        if line.find("no") != -1 and len(line) == 2:
            countNo += 1

    # display results
    print("Yes : ", countYes)
    print("No  : ", countNo)

main()