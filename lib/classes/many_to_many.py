import ipdb

class Game:
    def __init__(self, title):
        self.title = title
        self.results_list = []
        self.players_list = []

    def results(self):
        return self.results_list

    def players(self):
        return self.players_list

    def average_score(self, player):
        score_list = [result.score for result in self.results_list if result.player is player]
        return sum(score_list) / len(score_list)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title_parameter):
        if (not hasattr(self, 'title')) and type(title_parameter) == str and len(title_parameter) > 0:
            self._title = title_parameter
        else:
            print("Error: Unable to set value!")

class Player:
    def __init__(self, username):
        self.username = username
        self.results_list = []
        self.games_list = []

    def results(self):
        return self.results_list

    def games_played(self):
        return self.games_list

    def played_game(self, game):
        if game in self.games_list:
            return True
        else:
            return False

    def num_times_played(self, game):
        result_list = [result for result in self.results_list if result.game is game]
        return len(result_list)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username_parameter):
        if isinstance(username_parameter, str) and 2 <= len(username_parameter) <= 16:
            self._username = username_parameter

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        self.player.results_list.append(self)
        
        if not (game in self.player.games_list):
            self.player.games_list.append(game)
        
        self.game.results_list.append(self)
        
        if not (player in self.game.players_list):
            self.game.players_list.append(player)

        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score_parameter):
        if (not hasattr(self, 'score')) and type(score_parameter) == int and 1 <= score_parameter <= 5000:
            self._score = score_parameter

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player_parameter):
        if type(player_parameter) == Player:
            self._player = player_parameter

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game_parameter):
        if isinstance(game_parameter, Game):
            self._game = game_parameter

# ipdb.set_trace()