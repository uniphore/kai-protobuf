# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _google/protobuf/internal/more_extensions_dynamic.proto
"""Generated protocol buffer code."""
from _google.protobuf.internal import builder as _builder
from _google.protobuf import descriptor as _descriptor
from _google.protobuf import descriptor_pool as _descriptor_pool
from _google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from _google.protobuf.internal import more_extensions_pb2 as __google_dot_protobuf_dot_internal_dot_more__extensions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7_google/protobuf/internal/more_extensions_dynamic.proto\x12\x18google.protobuf.internal\x1a/_google/protobuf/internal/more_extensions.proto\"\x1f\n\x12\x44ynamicMessageType\x12\t\n\x01\x61\x18\x01 \x01(\x05:J\n\x17\x64ynamic_int32_extension\x12).google.protobuf.internal.ExtendedMessage\x18\x64 \x01(\x05:z\n\x19\x64ynamic_message_extension\x12).google.protobuf.internal.ExtendedMessage\x18\x65 \x01(\x0b\x32,.google.protobuf.internal.DynamicMessageType:\x83\x01\n\"repeated_dynamic_message_extension\x12).google.protobuf.internal.ExtendedMessage\x18\x66 \x03(\x0b\x32,.google.protobuf.internal.DynamicMessageType')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, '_google.protobuf.internal.more_extensions_dynamic_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  __google_dot_protobuf_dot_internal_dot_more__extensions__pb2.ExtendedMessage.RegisterExtension(dynamic_int32_extension)
  __google_dot_protobuf_dot_internal_dot_more__extensions__pb2.ExtendedMessage.RegisterExtension(dynamic_message_extension)
  __google_dot_protobuf_dot_internal_dot_more__extensions__pb2.ExtendedMessage.RegisterExtension(repeated_dynamic_message_extension)

  DESCRIPTOR._options = None
  _DYNAMICMESSAGETYPE._serialized_start=134
  _DYNAMICMESSAGETYPE._serialized_end=165
# @@protoc_insertion_point(module_scope)
