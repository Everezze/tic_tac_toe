def set_board(dimension,alphabet, player_turn, move_to_play=None, list_of_lists=[]):
    dash= False
    number_of_lines =0
    board_letters= alphabet[:dimension]
    symbol=''

    # Initialization and keep track of which player is about to play
    if player_turn ==1:
        symbol= 'x'
        player_turn = 2
    elif player_turn ==2:
        symbol= 'o'
        player_turn =1
    else:
        player_turn =1 


    if len(list_of_lists) ==0:
            for i in range(0,dimension):
                list_of_lists.append([])
                for j in range(0,dimension):
                    list_of_lists[i].append(' ')

    if move_to_play: 
        list_of_lists[move_to_play['row']][move_to_play['column']] = symbol

    print(list_of_lists)

    for letter in board_letters:
        if letter =='a':
          print(f'    {letter} ',end='')
          continue
        print(f'  {letter} ',end='')
    print('\n'+'   ---'+' ---'* (dimension-1))

    while number_of_lines < dimension:
        if dash:
            print('\n'+'   ---'+' ---'* (dimension-1))
            dash=False
            number_of_lines +=1

        else:
            print(f'{number_of_lines +1} |',end='')
            for tile in list_of_lists[number_of_lines]:
                #print('|'+ '   |'*dimension)
                print(f' {tile} |',end='')
            dash=True

    return (list_of_lists, player_turn)

#user_input= int(input('Insert a single digit for your grid dimension: '))
#set_board(user_input)


def get_move():

    tile_already_checked=0
    alphabet='abcdefghijklmnopqrstuvwxyz'
    winner= False
    player_turn=0

    while True:
        dimension= input('Insert a digit between 3 and 26 for your grid dimension(ex:8 for an 8*8 grid): ')
        if dimension.isalpha and len(dimension) < 3:
            dimension = int(dimension)
            if 3 <= dimension <= 26:
                break

    #dimension,list_of_lists,alphabet = set_board(dimension)
    list_of_lists, player_turn= set_board(dimension,alphabet,player_turn)

    allowed_move= dict()

    while not winner:

        for key in allowed_move.keys():
            allowed_move[key]=' '

        if tile_already_checked:
            print('Move not allowed : Tile already played')
            tile_already_checked=0

        print(f'Player {player_turn} to play')
        player_move= input('Type a coordinate pair(ex:b3) : ')
        player_move = list(player_move)

        if len(player_move) != 2:
            continue
        else:
            for char in player_move:
                if len(char) ==1 and char.isalpha():
                    if alphabet.index(char) <= dimension :
                        allowed_move['column']= alphabet.index(char)

                if len(char) ==1 and char.isdecimal() and 0<int(char) <= dimension:
                    allowed_move['row']= int(char)-1
        print(allowed_move)
        print(list_of_lists[allowed_move['row']][allowed_move['column']])

        if allowed_move['row'] != ' ' and allowed_move['column'] != ' ':
            print(allowed_move)
            print(list_of_lists[allowed_move['row']][allowed_move['column']])
            if list_of_lists[allowed_move['row']][allowed_move['column']] == ' ':
                list_of_lists,player_turn = set_board(dimension,alphabet,player_turn,move_to_play=allowed_move)
                winner = check_win(list_of_lists,dimension)
            else:
                tile_already_checked=1

    if winner == 'draw':
        print(f'It\'s a tie game')
    else:
        print(f'Player {winner} have won!')



def check_win(list_of_lists, dimension):

    dimension -=1
    x=0
    column=0
        
    #CHECKING FOR ROWS
    for list in list_of_lists:
        if all(move=='x' for move in list):
            return 'x'
        elif all(move=='o' for move in list):
            return 'o'

    #CHECKING FOR COLUMNS 
    while column <= dimension and x != dimension :

        if list_of_lists[dimension-x][column] == list_of_lists[dimension-x-1][column] and list_of_lists[dimension-x][column] !=' ':
                x+=1
                #tile_checked +=1
        else:
            x=0
            column+=1

    if x==dimension:
        return list_of_lists[dimension-x][column]  

    x=0
    column=0


    #CHECKING FOR THE DIAGONALS
    while x != dimension :
        if list_of_lists[dimension-x][x] == list_of_lists[dimension-x-1][x+1] and  list_of_lists[dimension-x][x] !=' ':
            x+=1
        else:
            break

    if x == dimension:
        #print(f'player {list_of_lists[dimension-x][x]} won!')
        return list_of_lists[dimension-x][x]
        #break

    x=0

    while x != dimension :
        if list_of_lists[dimension-x][-1-x] == list_of_lists[dimension-x-1][-1-(x+1)] and list_of_lists[dimension-x][-1-x] !=' ':
            x+=1
        else:
            break

    if x == dimension:
        #print(f'player {list_of_lists[dimension-x][-1-x]} won!')
        return list_of_lists[dimension-x][x-1-x]
        #break

    #x=0


    for row in list_of_lists:
        if all(char != ' ' for char in row):
            continue
        else:
            return False
    
    return 'draw'



def replay(answer):
    answer = answer.lower()
    if answer == 'yes' or answer == 'y':
        return True
    elif answer == 'no' or answer == 'n':
        return False
    
