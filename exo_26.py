def check_win(list_of_lists, dimension):

    dimension -=1
    x=0
    column=0
    #diagonal=0
    #tile_checked=1

    #while True:

    #if x ==dimension then all are crossed meaning player won, check for 0 case
    #if x == dimension:
        #print(f'player {list_of_lists[dimension-x][column]} won!')
        #break
        #column+=1
        #x=0

    #if column == dimension:
        #break

    #if diagonal == dimension:
        #print(f'player {list_of_lists[dimension-x][column]} won!')
        #break
        

    while column != dimension :

        while list_of_lists[dimension-x][column] == list_of_lists[dimension-x-1][column]:
            if list_of_lists[dimension-x][column] !=0:
                if x == dimension:
                    print(f'player {list_of_lists[dimension-x][column]} won!')
                    break
            x+=1
                #tile_checked +=1
        x=0
        column+=1

    #CHECKING FOR THE DIAGONALS
    while list_of_lists[dimension-x][x] == list_of_lists[dimension-x-1][x+1]:
        if list_of_lists[dimension-x][x] !=0:
            if x == dimension:
                print(f'player {list_of_lists[dimension-x][x]} won!')
                break
        x+=1

    x=0

    while list_of_lists[dimension-x][-1-x] == list_of_lists[dimension-x-1][-1+(x+1)]:
        if list_of_lists[dimension-x][-1-x] !=0:
            if x == dimension:
                print(f'player {list_of_lists[dimension-x][-1-x]} won!')
                break
        x+=1

    x=0
