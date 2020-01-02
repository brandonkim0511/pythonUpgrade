# A , B, C


def HanoiMove(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print ("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    HanoiMove(n-1, from_rod, aux_rod, to_rod)
    print ("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    HanoiMove(n-1, aux_rod, to_rod, from_rod)

# Driver code
n = 2
HanoiMove(n, 'Nayeon', 'Tzuyu', 'Sana')
# A, C, B are the name of rods

# Contributed By Harshit Agrawal
