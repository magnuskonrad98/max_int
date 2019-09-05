name = input("Velkomin/n í spurningakeppni Maggarans! Skrifaðu nafnið þitt: ")

score = 0

print("Hvað er 1+1?")
print("a: 1")
print("b: 2")
print("c: 3")
print("d: 4")
answer = input("Skrifaðu þitt svar (a,b,c or d): ")

if answer == "b":
    score += 1
    print("Vel gert sjomlakóngur! Stigin þín eru:", score, "/1")
else:
    print("Gaddem! Stigin þín eru: ", score, "/1")

print("Hvað er besti maturinn?")
print("a: pizza")
print("b: hamborgari")
print("c: nautasteik")
print("d: pulla")
answer = input("Skrifaðu þitt svar (a,b,c or d): ")

if answer == "a":
    score += 1
    print("Vel gert sjomlakóngur! Stigin þín eru:", score, "/2")
else:
    print("Gaddem! Stigin þín eru: ", score, "/2")

