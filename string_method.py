#string_method.py 

str = "Hello, My little baby"
print(str.upper()) #  대문자 반환
print(str.lower()) # 소문자 반환
print(str.title())
print()
print(str.count('b')) # 문자열내 'b'문자의 갯수 반환
print(str.startswith('h')) # 문자열의 시작문자가 'h'인지 여부 반환
print(str.endswith('y')) # 문자열의 끝문자가 'y'인지 여부 반환
print()
print(str.split()) # 문자열을 공백을 기준으로 분리해서 리스트로 반환
print(str.split(',')) # 문자열을 ','을 기준으로 분리해서 리스트로 반환
print(str.zfill(30)) # 문자열을 30으로 기준으로 남는 자리만큼 zero로 채우
