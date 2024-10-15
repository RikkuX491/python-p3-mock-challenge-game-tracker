class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if (not hasattr(self, 'title')) and type(value) == str and len(value) > 0:
            self._title = value

    def results(self):
        return [result for result in Result.all if result.game is self]

    def players(self):
        return list(set([result.player for result in Result.all if result.game is self]))

    def average_score(self, player):
        score_list = [result.score for result in Result.all if (result.game is self) and (result.player is player)]
        return sum(score_list) / len(score_list)

class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if type(value) == str and 2 <= len(value) <= 16:
            self._username = value

    def results(self):
        return [result for result in Result.all if result.player is self]

    def games_played(self):
        return list(set([result.game for result in Result.all if result.player is self]))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        if self.played_game(game):
            results_for_game_played_by_player_list = [result for result in Result.all if (result.player is self) and (result.game is game)]
            return len(results_for_game_played_by_player_list)
        else:
            return 0

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if (not hasattr(self, 'score')) and type(value) == int and value >= 1 and value <= 5000:
            self._score = value

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, value):
        if type(value) == Player:
            self._player = value

    @property
    def game(self):
        return self._game
    

    @game.setter
    def game(self, value):
        if type(value) == Game:
            self._game = value