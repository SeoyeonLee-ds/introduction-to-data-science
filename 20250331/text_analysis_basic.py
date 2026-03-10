s = "This movie was terrible! The acting was poor and the story was boring."
#print s
print("s =",s)
#print 글자수
print("글자수 =", len(s))
#print 단어들의 리스트
words = s.split()
print("단어들의의 리스트 =", words)
#print 단어 수
print("단어 수 =",len(words))
#print 평균 단어 길이
print("평균 단어 길이 =", sum(len(word) for word in words)/len(words))
#불용어 정의
stop_words = ['was', 'and', 'the']
#불용어를 제외한 단어들을 filtered_s에 저장
filtered_s = [word for word in words if word.lower() not in stop_words]
#print filtered_s
print("불용어가 제거된 s = ", ' '.join(filtered_s))