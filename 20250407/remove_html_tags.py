import re
html = input("HTML 문장을 입력하시오 :")
result = re.sub('<[^>]+>', '', html)
print(result)