points = 'AAAAAAAAAAAABBABABABABAABBABBAAAABABABABBABBAAAAAAAAABABABBBABABABAAABBBAAABBABBBAAABBBAAABBBABAABABBABAABAABBBABBBBBBBABBAAABABABABABBBABBBAAAABBABBBAAABBABABABBAAAAABBBAABBBABBBBBAAABAAAAABAAAAAAABBA'
def run(points: str) -> str:
    """ 
    15 -> 1
    30 -> 2
    40 -> 3
    puede ganar el punto si hay como mínimo dos puntos de ventaja/ -> 4
    si un jugador llega a 4 y el otro tiene 3, entonces es ventaja -> 4
    Ganas el punto -> 5
    """
    
    # Identificadores de jugadores
    PLAYER_A_CHAR = "A"
    PLAYER_B_CHAR = "B"
    
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
    
    game_winner = None
    set_winner = None
    
    point_position = 0
    for point in points:
        # Sumar puntos al contador de jugadores
        player_A_points += point == PLAYER_A_CHAR
        player_B_points += point == PLAYER_B_CHAR
        
        # Después de cada punto ganado, comprobar si el juego se ha terminado 
        # El ganador del juego tiene que tener 2 puntos de ventaja ✅
        # hay que tener en cuenta cuando un jugador pierde la ventaja, volver a deuce ✅
        # El ganador llega a 5 puntos es que ha ganado el juego ✅
        
        if player_A_points == 4 and player_A_points >= player_B_points + 2:
            game_winner = PLAYER_A_CHAR
        elif player_B_points == 4 and player_B_points >= player_A_points + 2:
            game_winner = PLAYER_B_CHAR
        elif player_A_points == 4 and player_B_points == 4:
            player_A_points -= 1
            player_B_points -= 1
        elif player_A_points == 5:
            game_winner = PLAYER_A_CHAR
        elif player_B_points == 5:
            game_winner = PLAYER_B_CHAR
        
        if game_winner:
            player_A_games += game_winner == PLAYER_A_CHAR
            player_B_games += game_winner == PLAYER_B_CHAR
            player_A_points = 0
            player_B_points = 0
            # Reseteamos la variable game_winner
            game_winner = None
            
            # Si un jugador ha llegado a 6 juegos y tiene una ventaja de 2 con el rival
            # se suma un set y se añade el resultado del set a la variable match_score ✅
            # Resetear los juegos cuando un set se ha ganado ✅
            # comprobar la funcionalidad del tie break
            
            if (player_A_games == 6 or player_A_games == 7) and player_A_games >= player_B_games + 2:
                set_winner = PLAYER_A_CHAR
            elif (player_B_games == 6 or player_B_games == 7) and player_B_games >= player_A_games + 2:
                set_winner = PLAYER_B_CHAR
            elif player_A_games == 6 and player_B_games == 6:
                point_position += 1
                while True:
                    current_point = points[point_position]
                    player_A_points += current_point == PLAYER_A_CHAR
                    player_B_points += current_point == PLAYER_B_CHAR
                    
                    has_A_won_tiebreak = player_A_points >= 7 and player_A_points >= player_B_points + 2
                    has_B_won_tiebreak = player_B_points >= 7 and player_B_points >= player_A_points + 2
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
                set_winner = None
                match_score += f"{player_A_games}-{player_B_games} "
                player_A_games = 0
                player_B_games = 0
                if player_A_sets == 2 or player_B_sets == 2:
                   break
        point_position += 1
    return match_score

run(points)