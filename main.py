import utils


while True:
    utils.get_move()

    user_answer =input('Do you want to play again? [Yes/Y/y] or [No/N/n]: ')
    if utils.replay(user_answer):
        continue
    else:
        break

