# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _google/protobuf/internal/import_test_package/outer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from _google.protobuf.internal.import_test_package import inner_pb2 as __google_dot_protobuf_dot_internal_dot_import__test__package_dot_inner__pb2
try:
  __google_dot_protobuf_dot_internal_dot_import__test__package_dot_import__public__pb2 = __google_dot_protobuf_dot_internal_dot_import__test__package_dot_inner__pb2.__google_dot_protobuf_dot_internal_dot_import__test__package_dot_import__public__pb2
except AttributeError:
  __google_dot_protobuf_dot_internal_dot_import__test__package_dot_import__public__pb2 = __google_dot_protobuf_dot_internal_dot_import__test__package_dot_inner__pb2._google.protobuf.internal.import_test_package.import_public_pb2
try:
  __google_dot_protobuf_dot_internal_dot_import__test__package_dot_import__public__nested__pb2 = __google_dot_protobuf_dot_internal_dot_import__test__package_dot_inner__pb2.__google_dot_protobuf_dot_internal_dot_import__test__package_dot_import__public__nested__pb2
except AttributeError:
  __google_dot_protobuf_dot_internal_dot_import__test__package_dot_import__public__nested__pb2 = __google_dot_protobuf_dot_internal_dot_import__test__package_dot_inner__pb2._google.protobuf.internal.import_test_package.import_public_nested_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9_google/protobuf/internal/import_test_package/outer.proto\x12\x33google.protobuf.python.internal.import_test_package\x1a\x39_google/protobuf/internal/import_test_package/inner.proto\"\xc0\x01\n\x05Outer\x12I\n\x05inner\x18\x01 \x01(\x0b\x32:.google.protobuf.python.internal.import_test_package.Inner\x12l\n\x14import_public_nested\x18\x02 \x01(\x0b\x32N.google.protobuf.python.internal.import_test_package.ImportPublicNestedMessage')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, '_google.protobuf.internal.import_test_package.outer_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _OUTER._serialized_start=174
  _OUTER._serialized_end=366
# @@protoc_insertion_point(module_scope)