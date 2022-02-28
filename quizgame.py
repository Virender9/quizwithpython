Asking = input("Do you Want To Play Game? ")
# print(Asking)
if Asking != "yes":
    quit()

score = 0
print("OK lets Play!")

answer = input("What Is short form of random access memory? ")
if answer.lower() == "ram":
    print("Correct")
    score += 1
else:
    print("Incorrect Answer")
    score -= 1

answer = input("What is 1MB equals to in KB? ")
if answer.lower() == "1024kb":
    print("Correct Answer")
    score +=1
else:
    print("Incorrect Answer")
    score -=1

answer = input("What is your relationship with your mom? ")
if answer.lower() == "son":
    print("Correct Answer")
    score +=1
else:
    print("Incorrect Answer")
    score -= 1
    

print("You have Achieved " + str(score) +" points")


