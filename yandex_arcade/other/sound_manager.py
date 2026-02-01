import arcade
import os
from typing import Optional
from ..tools.observer import Event


class BackgroundMusic:
    def __init__(self):
        self.music_player: Optional[arcade.sound.media.Player] = None
        self.current_music: Optional[arcade.Sound] = None
        self.volume: float = 0.25
        
        self.music_started = Event[str]()
        self.music_stopped = Event[None]() 
        self.volume_changed = Event[float]()
    
    def load_and_play(self, music_path: str, loop: bool = True):
        self.stop()
        self.current_music = arcade.load_sound(music_path, streaming=True)
        self.music_player = self.current_music.play(
            volume=self.volume,
            loop=loop
        )
        self.music_started.invoke(music_path)

    def play_sound_effect(self, sound_path: str, volume: float = 0.3):
        sound = arcade.load_sound(sound_path, streaming=False)
        arcade.play_sound(sound, volume=volume)
    
    def stop(self):
        if self.music_player:
            self.music_player.pause()
            self.music_stopped.invoke()
            self.music_player = None
            self.music_started = Event[str]()
            self.music_stopped = Event[None]()
            self.volume_changed = Event[float]()
    
    def pause(self):
        if self.music_player:
            self.music_player.pause()
    
    def resume(self):
        if self.music_player:
            self.music_player.play()

    def is_playing(self) -> bool:
        return self.music_player is not None and self.music_player.playing


background_music = BackgroundMusic()