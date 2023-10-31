import os
from typing import ClassVar, Mapping, Sequence, Any, Dict, Optional, Tuple, Final, List, cast
from typing_extensions import Self

from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName, Vector3
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

from audioout_python import Audioout
from viam.logging import getLogger

import pygame
from pygame import mixer

LOGGER = getLogger(__name__)

class audioout_pygame(Audioout, Reconfigurable):
    
    MODEL: ClassVar[Model] = Model(ModelFamily("viam-labs", "audioout"), "pygame")

    bitsize: int
    buffer: int
    channels: int
    frequency: int
    volume: float

    # Constructor
    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        my_class = cls(config.name)
        my_class.reconfigure(config, dependencies)
        return my_class

    @classmethod
    def validate(cls, config: ComponentConfig):
        return []

    # Handles attribute reconfiguration
    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        self.bitsize = int(config.attributes.fields["bitsize"].number_value or -16)
        self.buffer = int(config.attributes.fields["buffer"].number_value or 1024)
        self.channels = int(config.attributes.fields["channels"].number_value or 2)
        self.frequency = int(config.attributes.fields["frequency"].number_value or 44100)
        self.volume = config.attributes.fields["default_volume"].number_value or 1.0

        if mixer.pre_init() is None:
            mixer.init(self.frequency, self.bitsize, self.channels, self.buffer)

        # clear any playing channels
        mixer.stop()

        # release resources
        mixer.quit()
        return

    async def play(self, file_path: str, loop_count: int, maxtime_ms: int, fadein_ms: int, block: bool) -> str:
        LOGGER.info("Will play audio, blocking: " + str(block))
        if mixer.pre_init() is None:
            mixer.init(self.frequency, self.bitsize, self.channels, self.buffer)
            mixer.music.set_volume(self.volume)

        try:
            if os.path.isfile(file_path):
                mixer.music.load(file_path) 
                mixer.music.play(loop_count, maxtime_ms, fadein_ms)

                if block:
                    while mixer.music.get_busy():
                        pygame.time.Clock().tick()
                        
                LOGGER.info("Played audio...")
            else:
                raise ValueError("Specified file path not found")
        except RuntimeError as e:
            raise ValueError("Play failure: " + str(e))
        return file_path

    async def stop(self) -> str:
        try:
            mixer.music.stop()
        except RuntimeError:
            raise ValueError("Stop failure")
        return "OK"
