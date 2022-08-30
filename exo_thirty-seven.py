def set_board(dimension,alphabet, player_turn, move_to_play=None, list_of_lists=[]):
    dash= False
    number_of_lines =0
    board_letters= alphabet[:dimension]
    if player_turn ==1:
        symbol= 'x'
        player_turn = 2
    else:
        symbol= 'o'
        player_turn =1


    if len(list_of_lists) ==0:
            for i in range(0,dimension):
                list_of_lists.append([])
                for j in range(0,dimension):
                    list_of_lists[i].append(' ')

    if move_to_play: 
        list_of_lists[move_to_play['row']][move_to_play['column']] = symbol

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
    player_turn=1

    while True:
        dimension= input('Insert a digit between 3 and 26 for your grid dimension(ex:8 for 8*8 grid): ')
        if dimension.isalpha and len(dimension) < 3:
            dimension = int(dimension)
            if 3 <= dimension <= 26:
                break

    #dimension,list_of_lists,alphabet = set_board(dimension)
    list_of_lists, player_turn= set_board(dimension,alphabet,player_turn)

    allowed_move= dict()

    while not winner:
        if tile_already_checked:
            print('Move not allowed : Tile already checked')
            tile_already_checked=0

        input(f'Player {player_turn} to play')
        player_move= input('Type a coordinate pair(ex:b3) : ')
        player_move = list(player_move)

        if len(player_move) != 2:
            continue
        else:
            for char in player_move:
                if len(char) ==1 and char.isalpha():
                    if alphabet.index(char) < dimension and not allowed_move['column']:
                        allowed_move['column']= alphabet.index(char)

                if len(char) ==1 and char.isdecimal() and int(char) < dimension:
                    if not allowed_move['row']:
                        allowed_move['row']= int(char)

        if allowed_move['row'] and allowed_move['column']:
            if not list_of_lists[allowed_move['row']][allowed_move['column']]:
                list_of_lists,player_turn = set_board(dimension,alphabet,player_turn,move_to_play=allowed_move)
                winner = check_win(list_of_lists,dimension)
            else:
                tile_already_checked=1
