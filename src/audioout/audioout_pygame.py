import os
from typing import ClassVar, Mapping, Sequence, Any, Dict, Optional, Tuple, Final, List, cast
from typing_extensions import Self

from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName, Vector3
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

from .api import Audioout
from viam.logging import getLogger

import time
import asyncio
import pygame
from pygame import mixer

LOGGER = getLogger(__name__)
mixer.init(buffer=1024)

class audioout_pygame(Audioout, Reconfigurable):
    
    MODEL: ClassVar[Model] = Model(ModelFamily("viam-labs", "audioout"), "pygame")
    
    mic_device_name: str

    # Constructor
    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        my_class = cls(config.name)
        my_class.reconfigure(config, dependencies)
        return my_class

    # Handles attribute reconfiguration
    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        self.mic_device_name = config.attributes.fields["mic_device_name"].string_value or ""
        return

    async def play(self, file_path: str, loop_count: int, maxtime_ms: int, fadein_ms: int) -> str:
        try:
            if os.path.isfile(file_path):
                mixer.music.load(file_path) 
                mixer.music.play(loop_count, maxtime_ms, fadein_ms)

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