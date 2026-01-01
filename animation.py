'''# https://ezgif.com/sprite-cutter/
import math
from pathlib import Path

from attrs import define, field

from sprite import Sprite, SPRITES_FOLDER
from observer import Event, OnEventSubscriber
from vector import Vector2Int


@define
class Animation:
    @classmethod
    def load(cls, folder: str = "walk", frames_count: int = 4, period: float = 0.5):
        folder = Path(folder)
        full_folder = SPRITES_FOLDER / folder
        assert full_folder.exists() and full_folder.is_dir()

        frames = list[Sprite]()
        for index in range(frames_count):
            filename = folder / f"walk{str(index+1)}.png"
            frames.append(Sprite.load_raw_image(filename, Vector2Int.zero()))

        return cls(frames, period, loop=True)

    _frames: list[Sprite]
    _period: float
    _progress: float = field(init=False, default=0)
    _loop: bool = True
    _has_ended: Event[None] = field(init=False, factory=Event)

    @property
    def has_ended(self) -> OnEventSubscriber[None]:
        return self._has_ended.subscriber

    @property
    def current_frame(self) -> Sprite:
        assert self._progress < self._period
        return self._frames[self._current_frame_index]

    @property
    def _current_frame_index(self) -> int:
        return math.floor(self._progress / self._period * len(self._frames))

    def update(self, dt: float) -> None:
        self._progress += dt
        if self._progress <= self._period:
            return
        if self._loop and self._progress >= self._period:
            self._progress = 0
        self._progress = self._period 
        #self._has_ended.invoke()

    def play(self) -> None:
        self._is_playing = True

    def pause(self) -> None:
        self._is_playing = False

    def reset(self) -> None:
        self._progress = 0'''


import math
from pathlib import Path

import arcade
from attrs import define, field

from sprite import Sprite, SPRITES_FOLDER
from observer import Event, OnEventSubscriber
from vector import Vector2Int


@define
class Animation:
    @classmethod
    def load(cls, folder: str = "walk", frames_count: int = 4, period: float = 0.3):
        folder = Path(folder)
        full_folder = SPRITES_FOLDER / folder
        assert full_folder.exists() and full_folder.is_dir()

        frames = list[Sprite]()
        for index in range(frames_count):
            filename = folder / f"walk{str(index+1)}.png"
            frames.append(Sprite.load_raw_image(filename, Vector2Int.zero()))

        return cls(frames, period)

    _frames: list[Sprite]
    _period: float
    _progress: float = field(init=False, default=0)

    @property
    def current_frame(self) -> Sprite:
        return self._frames[self._current_frame_index]

    @property
    def _current_frame_index(self) -> int:
        if not self._frames:
            return 0
        return math.floor(self._progress / self._period * len(self._frames)) % len(self._frames)

    def update(self, dt: float) -> None:
        self._progress += dt
        if self._progress >= self._period * len(self._frames):
            self._progress = 0

    def reset(self) -> None:
        self._progress = 0









# https://ezgif.com/sprite-cutter/

@define
class RocketAnimation:
    @classmethod
    def load(cls, folder: str = 'rocket_explode', frames_count: int = 7, period: float = 1, pivot: Vector2Int = Vector2Int.zero()):
        folder = Path(folder)
        full_folder = SPRITES_FOLDER / folder
        assert full_folder.exists() and full_folder.is_dir()

        frames = list[Sprite]()
        for index in range(frames_count):
            filename = folder / f"explode{str(index + 1)}.png"
            frames.append(Sprite.load_raw_image(filename, pivot))

        return cls(frames, period)

    _frames: list[Sprite]
    _period: float
    _progress: float = field(init=False, default=0)

    _has_ended: Event[None] = field(init=False, factory=Event)

    @property
    def has_ended(self) -> OnEventSubscriber[None]:
        return self._has_ended.subscriber

    @property
    def current_frame(self) -> Sprite:
        return self._frames[self._current_frame_index]

    @property
    def _current_frame_index(self) -> int:
        return math.floor(self._progress / self._period * len(self._frames))

    def update(self, dt: float) -> None:
        self._progress += dt
        if self._progress <= self._period:
            return

        self._progress = self._period
        self._has_ended.invoke()

@define
class ExplosionEffect:
    position: Vector2Int
    animation: object  # ← теперь может быть любая анимация
    _is_finished: bool = field(default=False, init=False)

    @classmethod
    def create_at(cls, pos: Vector2Int, anim_class, **anim_kwargs) -> "ExplosionEffect":

        anim = anim_class.load(**anim_kwargs)
        return cls(position=pos, animation=anim)

    def update(self, dt: float) -> None:
        if self._is_finished:
            return
        self.animation.update(dt)
        if self.animation._progress >= self.animation._period:
            self._is_finished = True

    def is_finished(self) -> bool:
        return self._is_finished

    def get_texture(self) -> arcade.Texture:
        return self.animation.current_frame.get()

    def get_position(self) -> Vector2Int:
        return self.position