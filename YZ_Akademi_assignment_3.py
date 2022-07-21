import sys
ballEnergy = int(input("Enter The Energy of The Ball: "))

arr = list(map(int, input("Enter The Heights : ").split()))

ballEnergies = [ballEnergy]    

if 1<= ballEnergy <= 10^5:
    pass
else:    
    sys.exit("Ball Energy value is out of range ")


for height in arr:
    
    if (1<= height <= 10^5):
        pass
    else:
        sys.exit("Height value is out of range")



    if ballEnergy < height :
        newEnergy = ballEnergy - (height - ballEnergy)
        ballEnergies.append(newEnergy)
        ballEnergy = newEnergy
        #print("delta" , newEnergy-ballEnergy)   uncomment for delta     
        #print(newEnergy)                        uncomment for new energy of the ball


    elif ballEnergy > height:
        newEnergy = ballEnergy + (ballEnergy - height)
        ballEnergies.append(newEnergy)
        ballEnergy = newEnergy
        #print("delta" , newEnergy-ballEnergy)   uncomment for delta
        #print(newEnergy)                        uncomment for new energy of the ball
        
    else:
        ballEnergies.append(newEnergy)
        ballEnergy = newEnergy

print("minimum: ",min(ballEnergies))
