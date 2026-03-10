def process(w):
    output =''
    for ch in w:
        if ch.isalpha():
            output += ch
    return output.lower()

#get filename
file_name = input("입력 파일 이름:")
#open file
file = open(file_name, "r")
#create empty set
words = set()
#iter for all lines in file
for line in file:
    #get words from each line
    linewords = line.split()
    for word in linewords:
        words.add(process(word))
print("사용된 단어의 개수 = ", len(words))
print(words)