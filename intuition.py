score=0
print("Welome To The Intuition Test!")
print("Answer The Following Questions: Trust Your Gut. Don't Over Think! \n")
q1=int(input("1. Guess a number between 1-10: "))
if q1==7:
    print("Correct Answer!\n")
    score+=1
else:
    print("Wrong answer! It was 7\n")
q2=(input("2. What is behind the door? (cat/dog): ")).lower()
if q2=="cat":
    print("Correct Answer!\n")
    score+=1
else:
    print("Wrong answer! It was cat\n")
q3=(input("3.Choose a color (Red/blue). ")).lower()
if q3=="blue":
    print("Correct Answer!\n")
    score+=1
else:
    print("Wrong answer! It was blue\n")
q4=int(input("4. Pick a number (1-5): "))
if q4==3:
    print("Correct Answer!\n")
    score+=1
else:
    print("Wrong answer! It was 3\n")
q5=(input("5. Day or Night?: ")).lower()
if q5=="night":
    print("Correct Answer!\n")
    score+=1
else:
    print("Wrong answer! It was night\n")
q6=(input("6. Tea/Coffee?: ")).lower()
if q6=="tea":
    print("Correct Answer!\n")
    score+=1
else:
    print("Wrong answer! It was tea\n")
q7=(input("7. Summer or Winter?: ")).lower()
if q7=="winter":
    print("Correct Answer!\n")
    score+=1
else:
    print("Wrong answer! It was winter\n")
q8=(input("8. Choose(Sun/Moon): ")).lower()
if q8=="moon":
  print("Correct Answer!\n")
  score+=1
else:
    print("Wrong answer! It was moon\n")
q9=(input("9. Even or Odd?: ")).lower()
if q9=="even":
    print("Correct Answer!\n")
    score+=1
else:
    print("Wrong answer! It was even\n")
q10=(input("10. Left or Right?: ")).lower()
if q10=="left":
    print("Correct Answer!\n")
    score+=1
else:
    print("Wrong answer! It was left\n")
print("\nYour score:",score,"/10")
if score>=8:
    print("Excellent Intuition!")
elif score>=5:
    print("Good Intuition!")
else:
    print("Need Improvement!")