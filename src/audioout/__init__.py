"""
This file registers the model with the Python SDK.
"""

from viam.resource.registry import Registry, ResourceCreatorRegistration

from audioout_python import Audioout
from .audioout_pygame import audioout_pygame

Registry.register_resource_creator(Audioout.SUBTYPE, audioout_pygame.MODEL, ResourceCreatorRegistration(audioout_pygame.new))
