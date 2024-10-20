def play_game():
    game = TicTacToeMDP()
    vi = ValueIteration(game)
    vi.value_iteration()
 
    current_player = 1  # Start with player 1
    while True:
        if current_player == 1:
            action = get_player_move(game)
        else:
            # AI's turn
            state = game.board_to_state()  # You need to implement board_to_state() in TicTacToeMDP
            action = vi.get_optimal_action(state)
        game.update_state(action, current_player)
     
        if game.is_winner(current_player):
            print(f"Player {current_player} wins!")
            break
        elif not game.get_possible_actions():
            print("It's a draw!")
            break
     
        # Switch turns
        current_player = -current_player

play_game()
