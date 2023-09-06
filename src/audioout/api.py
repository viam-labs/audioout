"""
This file outlines the general structure for the API around a custom, modularized service.

It defines the abstract class definition that all concrete implementations must follow,
the gRPC service that will handle calls to the service,
and the gRPC client that will be able to make calls to this service.

In this example, the ``Audioout`` abstract class defines what functionality is required for all Audioout services.
It extends ``ServiceBase``, as all service types must.
It also defines its specific ``SUBTYPE``, which is used internally to keep track of supported types.

The ``AudiooutRPCService`` implements the gRPC service for the Audioout service. This will allow other robots and clients to make
requests of the Audioout service. It extends both from ``AudiooutServiceBase`` and ``RPCServiceBase``.
The former is the gRPC service as defined by the proto, and the latter is the class that all gRPC services must inherit from.

Finally, the ``AudiooutClient`` is the gRPC client for a Audioout service. It inherits from AudiooutService since it implements
 all the same functions. The implementations are simply gRPC calls to some remote Audioout service.

To see how this custom modular service is registered, see the __init__.py file.
To see the custom implementation of this service, see the audioout_pygame.py file.
"""

import abc
from typing import Final, Sequence

from grpclib.client import Channel
from grpclib.server import Stream

from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.resource.types import RESOURCE_TYPE_SERVICE, Subtype
from viam.services.service_base import ServiceBase

from ..proto.audioout_grpc import AudiooutServiceBase, AudiooutServiceStub

# update the below with actual methods for your API!
from ..proto.audioout_pb2 import PlayRequest, PlayResponse, StopRequest, StopResponse


class Audioout(ServiceBase):

    SUBTYPE: Final = Subtype("viam-labs", RESOURCE_TYPE_SERVICE, "audioout")

    @abc.abstractmethod
    async def play(self, file_path: str, loop_count: int, maxtime_ms: int, fadein_ms: int) -> str:
        ...
    async def stop(self) -> str:
        ...

class AudiooutRPCService(AudiooutServiceBase, ResourceRPCServiceBase):

    RESOURCE_TYPE = Audioout

    async def Play(self, stream: Stream[PlayRequest, PlayResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        service = self.get_resource(name)
        resp = await service.play(request.file_path, request.loop_count, request.maxtime_ms, request.fadein_ms, request.block)
        await stream.send_message(PlayResponse(text=resp))

    async def Stop(self, stream: Stream[StopRequest, StopResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        service = self.get_resource(name)
        resp = await service.stop()
        await stream.send_message(StopResponse(text=resp))

class AudiooutClient(Audioout):

    def __init__(self, name: str, channel: Channel) -> None:
        self.channel = channel
        self.client = AudiooutServiceStub(channel)
        super().__init__(name)

    async def play(self, file_path: str = "", loop_count: int = 0, maxtime_ms: int = 0, fadein_ms: int = 0, block: bool = False) -> str:
        request = PlayRequest(name=self.name, file_path=file_path, loop_count=loop_count, maxtime_ms=maxtime_ms, fadein_ms=fadein_ms, block=block)
        response: PlayResponse = await self.client.Play(request)
        return response.text
    
    async def stop(self) -> str:
        request = StopRequest(name=self.name)
        response: StopResponse = await self.client.Stop(request)
        return response.text