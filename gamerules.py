from physics import SPAWN_POSITION
from vector import Vector2
from player import Player
import arcade

class GameRules:
    @staticmethod
    def check_level_completion(player: Player, exit_position: Vector2, exit_radius: float = 20.0) -> bool:
        distance = (player.position - exit_position).length
        return distance < exit_radius
    
    @staticmethod
    def exit_game() -> None:
        arcade.close_window()
    
    @staticmethod
    def restart_level(player: Player, spawn_position: Vector2 = SPAWN_POSITION) -> None:
        player.physics.position = spawn_position
        player.physics.velocity = Vector2.zero()

    def complete_level(game_app, level_num: int) -> None:
        game_app.save_system.complete_level(level_num)
        next_level = level_num + 1
        game_app.save_system.unlock_level(next_level)
        game_app.switch_to_state("level", level_num=next_level)

    def complete_level_and_return_to_menu(game_app, level_num: int) -> None:
        game_app.save_system.complete_level(level_num)
        game_app.switch_to_state("main_menu")

#GameRules.complete_level_and_return_to_menu(self.game_app, self.level_num)