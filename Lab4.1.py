class game():
    def __init__(game):
        game.board = list(" " * 9)
        
    def save(game, player):
        oxo_data.saveGame(game.board)
        
    def restore(game):
        try:
            game.board = oxo_data.restoreGame()
            if len(game.board) !-9:
                game.board = list(" " * 9)
            return game.board
        except IOError:
            game.board = list(" " * 9)
            return game,board
        
    def _generateMOve(game):
        option = [i for i in range(len(game.board)) if game board[i] == " "]
        if options:
            return random.choice(option)
        else:
            return -1
        
    def _isWinningMove(game):
        wins = ((0,1,2), (3,4,5), (6,7,8,),
                (0,3,6), (1,4,7), (2,5,8),
                (0,3,8), (2,4,6))
        game = game.board
        for a,b,c in wins:
            chars = game[a] + game[b] + game[c]
            if chars == 'xxx' or chars =='000'
                return True
            return False
        
    def userMove(game.cell):
        if game.board[cell] != ' ':
            raise ValueError('invalid Cell')
        else:
            game.board[cell] = 'x'
            
        if game._isWinningMove():
            return'x'
        else:
            return ""
        
    def computerMove(game):
        cell = game._generateMove(game):
        if cell == -1:
            return 'D'
        game.board[cell] = '0'
        if game._isWInningMove():
            return '0'
        else:
            return ""
        