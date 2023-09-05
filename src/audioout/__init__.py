"""
This file registers the model with the Python SDK.
"""

from viam.resource.registry import Registry, ResourceCreatorRegistration, ResourceRegistration

from .api import AudiooutClient, AudiooutRPCService, Audioout
from .audioout_pygame import audioout_pygame

Registry.register_subtype(ResourceRegistration(Audioout, AudiooutRPCService, lambda name, channel: AudiooutClient(name, channel)))

Registry.register_resource_creator(Audioout.SUBTYPE, audioout_pygame.MODEL, ResourceCreatorRegistration(audioout_pygame.new))
