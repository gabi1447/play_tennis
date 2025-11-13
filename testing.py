points = 'AAAAAAAAAAAABBABABABABAABBABBAAAABABABABBABBAAAAAAAAABABABBBABABABAAABBBAAABBABBBAAABBBAAABBBABAABABBABAABAABBBABBBBBBBABBAAABABABABABBBABBBAAAABBABBBAAABBABABABBAAAAABBBAABBBABBBBBAAABAAAAABAAAAAAABBA'
def run(points: str) -> str:
    """ 
    1 -> 15
    2 -> 30
    3 -> 40
    4 -> Gana el juego si hay dos puntos de ventaja
    5 -> Gana el juego siempre después de tener ventaja en un 40 iguales
    """
    
    MIN_POINTS_TO_WIN_TIE_BREAK = 7
    NUM_SETS_TO_WIN_MATCH = 2
    MIN_POINTS_TO_WIN_GAME = 4
    MAX_POINTS_TO_WIN_GAME = 5
    MIN_GAMES_TO_WIN_SET = 6
    MAX_GAMES_TO_WIN_SET = 7
    MIN_DIFFERENCE = 2
    
    # Identificadores de jugadores
    PLAYER_A_CHAR = "A"
    PLAYER_B_CHAR = "B"
    
    points_length = len(points)
    
    # Contador de puntos
    player_A_points = 0
    player_B_points = 0
    
    # Contador de juegos
    player_A_games = 0
    player_B_games = 0
    
    # Contador de sets
    player_A_sets = 0
    player_B_sets = 0 
    
    # Se actualiza cuando un jugador ha ganado un set
    match_score = ""
    
    # Usamos estas variables para saber cuando tenemos que entrar en las condiciones
    # que controlan el fin del set y el fin del juego
    game_winner = None
    set_winner = None
    
    point_position = 0
    for index in range(points_length):
        # Esta condición es necesaria para continuar la lógica del programa 
        # después de un set donde se produzca un tie-break
        if index != point_position:
            continue
        
        point = points[index]
        player_A_points += point == PLAYER_A_CHAR
        player_B_points += point == PLAYER_B_CHAR
        
        # Condiciones para comprobar si el juego se ha acabado y también volver a 40 iguales
        # si un jugador/a tiene ventaja y el otro jugador/a vuelve a anotar un punto.
        
        has_A_reached_min_points = player_A_points == MIN_POINTS_TO_WIN_GAME
        has_B_reached_min_points = player_B_points == MIN_POINTS_TO_WIN_GAME
        
        if has_A_reached_min_points and player_A_points >= player_B_points + MIN_DIFFERENCE:
            game_winner = PLAYER_A_CHAR
        elif has_B_reached_min_points and player_B_points >= player_A_points + MIN_DIFFERENCE:
            game_winner = PLAYER_B_CHAR
        elif player_A_points == MIN_POINTS_TO_WIN_GAME and player_B_points == MIN_POINTS_TO_WIN_GAME:
            player_A_points -= 1
            player_B_points -= 1
        elif player_A_points == MAX_POINTS_TO_WIN_GAME:
            game_winner = PLAYER_A_CHAR
        elif player_B_points == MAX_POINTS_TO_WIN_GAME:
            game_winner = PLAYER_B_CHAR
        
        if game_winner:
            player_A_games += game_winner == PLAYER_A_CHAR
            player_B_games += game_winner == PLAYER_B_CHAR
            
            game_winner = None
            player_A_points = 0
            player_B_points = 0
            
            # Si un jugador ha llegado a 6 juegos y tiene una ventaja de 2 con el rival
            # se suma un set y si el resultado del partido es 6-6 entonces se entra en
            # la condición para controlar la lógica del tie-break.
            
            has_A_reached_max_games = player_A_games == MIN_GAMES_TO_WIN_SET or player_A_games == MAX_GAMES_TO_WIN_SET
            has_B_reached_max_games = player_B_games == MIN_GAMES_TO_WIN_SET or player_B_games == MAX_GAMES_TO_WIN_SET
            
            if has_A_reached_max_games and player_A_games >= player_B_games + MIN_DIFFERENCE:
                set_winner = PLAYER_A_CHAR
            elif has_B_reached_max_games and player_B_games >= player_A_games + MIN_DIFFERENCE:
                set_winner = PLAYER_B_CHAR
            elif player_A_games == MIN_GAMES_TO_WIN_SET and player_B_games == MIN_GAMES_TO_WIN_SET:
                point_position += 1
                while True:
                    current_point = points[point_position]
                    player_A_points += current_point == PLAYER_A_CHAR
                    player_B_points += current_point == PLAYER_B_CHAR
                    
                    has_A_won_tiebreak = player_A_points >= MIN_POINTS_TO_WIN_TIE_BREAK and player_A_points >= player_B_points + MIN_DIFFERENCE
                    has_B_won_tiebreak = player_B_points >= MIN_POINTS_TO_WIN_TIE_BREAK and player_B_points >= player_A_points + MIN_DIFFERENCE
                    if has_A_won_tiebreak or has_B_won_tiebreak:
                        set_winner = "A" if has_A_won_tiebreak else "B"
                        player_A_games += set_winner == PLAYER_A_CHAR
                        player_B_games += set_winner == PLAYER_B_CHAR
                        player_A_points = 0
                        player_B_points = 0
                        break
                    point_position += 1
                    
            if set_winner:
                player_A_sets += set_winner == PLAYER_A_CHAR
                player_B_sets += set_winner == PLAYER_B_CHAR
                
                match_score += f"{player_A_games}-{player_B_games} "
                player_A_games = 0
                player_B_games = 0
                set_winner = None
                
                is_match_finished = player_A_sets == NUM_SETS_TO_WIN_MATCH or player_B_sets == NUM_SETS_TO_WIN_MATCH
                if is_match_finished:
                   break
        point_position += 1
        
    return match_score