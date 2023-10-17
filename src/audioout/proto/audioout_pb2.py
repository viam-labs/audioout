# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: audioout.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x61udioout.proto\x12\x1cviamlabs.service.audioout.v1\x1a\x1cgoogle/api/annotations.proto\"\xaf\x01\n\x0bPlayRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tfile_path\x18\x02 \x01(\tR\x08\x66ilePath\x12\x1d\n\nloop_count\x18\x03 \x01(\x05R\tloopCount\x12\x1d\n\nmaxtime_ms\x18\x04 \x01(\x05R\tmaxtimeMs\x12\x1b\n\tfadein_ms\x18\x05 \x01(\x05R\x08\x66\x61\x64\x65inMs\x12\x14\n\x05\x62lock\x18\x06 \x01(\x08R\x05\x62lock\"\"\n\x0cPlayResponse\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\"!\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"\"\n\x0cStopResponse\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text2\xb3\x02\n\x0f\x41udiooutService\x12\x8e\x01\n\x04Play\x12).viamlabs.service.audioout.v1.PlayRequest\x1a*.viamlabs.service.audioout.v1.PlayResponse\"/\x82\xd3\xe4\x93\x02)\"\'/acme/api/v1/service/speech/{name}/play\x12\x8e\x01\n\x04Stop\x12).viamlabs.service.audioout.v1.StopRequest\x1a*.viamlabs.service.audioout.v1.StopResponse\"/\x82\xd3\xe4\x93\x02)\"\'/acme/api/v1/service/speech/{name}/stopb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'audioout_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AUDIOOUTSERVICE.methods_by_name['Play']._options = None
  _AUDIOOUTSERVICE.methods_by_name['Play']._serialized_options = b'\202\323\344\223\002)\"\'/acme/api/v1/service/speech/{name}/play'
  _AUDIOOUTSERVICE.methods_by_name['Stop']._options = None
  _AUDIOOUTSERVICE.methods_by_name['Stop']._serialized_options = b'\202\323\344\223\002)\"\'/acme/api/v1/service/speech/{name}/stop'
  _PLAYREQUEST._serialized_start=79
  _PLAYREQUEST._serialized_end=254
  _PLAYRESPONSE._serialized_start=256
  _PLAYRESPONSE._serialized_end=290
  _STOPREQUEST._serialized_start=292
  _STOPREQUEST._serialized_end=325
  _STOPRESPONSE._serialized_start=327
  _STOPRESPONSE._serialized_end=361
  _AUDIOOUTSERVICE._serialized_start=364
  _AUDIOOUTSERVICE._serialized_end=671
# @@protoc_insertion_point(module_scope)
