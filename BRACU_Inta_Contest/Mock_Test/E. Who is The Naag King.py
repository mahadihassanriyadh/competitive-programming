L, S = input().split()
L = int(L)  # the number of Ladders and
S = int(S)  # the number ofSnake in the board
LArray = []
SArray = []
for x in range(L):
    LArray.append(input())

for x in range(S):
    SArray.append(input())
gotWinner = False
jabir_position = 0
muktadir_position = 0
jabir_bhai = True

while not gotWinner:
    v = int(input())
    if jabir_bhai:
        if jabir_position >= 100:
            print("Jaber Tuhin is the winner.")
            gotWinner = True
            break

        if jabir_position > 0:
            jabir_position += v

            for i in range(L):
                a, b = LArray[i].split()
                a = int(a)
                b = int(b)
                if jabir_position == a:
                    jabir_position = b
            for i in range(S):
                a, b = SArray[i].split()
                a = int(a)
                b = int(b)
                if jabir_position == a:
                    jabir_position = b
            if jabir_position == 100:
                print("Jaber Tuhin is the winner.")
                gotWinner = True
                break
            elif jabir_position > 100:
                jabir_position = jabir_position - v

            print("j", jabir_position)
            jabir_bhai = False
        elif jabir_position == 0:
            if v == 1:
                jabir_position = 1
                jabir_bhai = False
            else:
                jabir_bhai = False

    elif not jabir_bhai:
        if muktadir_position >= 100:
            print("Mukhter Hossain is the winner.")
            gotWinner = True
            break

        if muktadir_position > 0:
            muktadir_position += v

            for i in range(L):
                a, b = LArray[i].split()
                a = int(a)
                b = int(b)
                if muktadir_position == a:
                    muktadir_position = b
            for i in range(S):
                a, b = SArray[i].split()
                a = int(a)
                b = int(b)
                if muktadir_position == a:
                    muktadir_position = b
            if muktadir_position == 100:
                print("Mukhter Hossain is the winner.")
                gotWinner = True
                break
            elif muktadir_position > 100:
                muktadir_position = muktadir_position - v

            jabir_bhai = True
        elif muktadir_position == 0:
            if v == 1:
                muktadir_position = 1
                jabir_bhai = True
            else:
                jabir_bhai = True
