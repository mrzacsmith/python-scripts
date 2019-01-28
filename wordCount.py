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
        line = line.lower()
        line = line.strip()
        # print(line)

        if line.find("yes") != -1:
            countYes += 1
        if line.find("no") != -1:
            countNo += 1

    # display results
    print("Yes : ", countYes)
    print("No  : ", countNo)

main()