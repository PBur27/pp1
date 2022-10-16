cm = int(input("height in centimeters = ?  "))
print("I am {0} cm tall, i.e. {1} feet and {2} inches.".format(cm,cm//30.48,(cm%30.48)//2.54))