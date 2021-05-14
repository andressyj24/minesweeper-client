import requests
from pydantic import BaseModel

game_service_url = 'https://mine-sweeper-game.herokuapp.com/'


class NewGameRequest(BaseModel):
    rows: int
    columns: int
    timer: int
    difficulty: str


class UpdateGameRequest(BaseModel):
    game_id: str
    row: int
    column: int
    action: str


def create_new_game(new_game_request: NewGameRequest):
    data = {'rows': new_game_request.rows, 'columns': new_game_request.columns, 'timer': new_game_request.timer,
            'difficulty': new_game_request.difficulty}
    create_game_url = f'{game_service_url}api/games'
    return requests.post(create_game_url, data)


def get_game(game_id):
    get_game_url = f'https://mine-sweeper-game.herokuapp.com/api/games/{game_id}'
    return requests.get(get_game_url)


def update_cell(update_cell_request: UpdateGameRequest):
    data = {'row': update_cell_request.row, 'columns': update_cell_request.column, 'action': 'FLAG'}
    update_game_url = f'https://mine-sweeper-game.herokuapp.com/api/games/{update_cell_request.game_id}/boards'
    return requests.patch(update_game_url, data)


if __name__ == '__main__':
    create_new_game(NewGameRequest(5, 7, 5, 'MEDIUM'))
