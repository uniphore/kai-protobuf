# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _google/protobuf/internal/missing_enum_values.proto
"""Generated protocol buffer code."""
from _google.protobuf.internal import builder as _builder
from _google.protobuf import descriptor as _descriptor
from _google.protobuf import descriptor_pool as _descriptor_pool
from _google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3_google/protobuf/internal/missing_enum_values.proto\x12\x1fgoogle.protobuf.python.internal\"\xc1\x02\n\x0eTestEnumValues\x12X\n\x14optional_nested_enum\x18\x01 \x01(\x0e\x32:.google.protobuf.python.internal.TestEnumValues.NestedEnum\x12X\n\x14repeated_nested_enum\x18\x02 \x03(\x0e\x32:.google.protobuf.python.internal.TestEnumValues.NestedEnum\x12Z\n\x12packed_nested_enum\x18\x03 \x03(\x0e\x32:.google.protobuf.python.internal.TestEnumValues.NestedEnumB\x02\x10\x01\"\x1f\n\nNestedEnum\x12\x08\n\x04ZERO\x10\x00\x12\x07\n\x03ONE\x10\x01\"\xd3\x02\n\x15TestMissingEnumValues\x12_\n\x14optional_nested_enum\x18\x01 \x01(\x0e\x32\x41.google.protobuf.python.internal.TestMissingEnumValues.NestedEnum\x12_\n\x14repeated_nested_enum\x18\x02 \x03(\x0e\x32\x41.google.protobuf.python.internal.TestMissingEnumValues.NestedEnum\x12\x61\n\x12packed_nested_enum\x18\x03 \x03(\x0e\x32\x41.google.protobuf.python.internal.TestMissingEnumValues.NestedEnumB\x02\x10\x01\"\x15\n\nNestedEnum\x12\x07\n\x03TWO\x10\x02\"\x1b\n\nJustString\x12\r\n\x05\x64ummy\x18\x01 \x02(\t')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, '_google.protobuf.internal.missing_enum_values_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TESTENUMVALUES.fields_by_name['packed_nested_enum']._options = None
  _TESTENUMVALUES.fields_by_name['packed_nested_enum']._serialized_options = b'\020\001'
  _TESTMISSINGENUMVALUES.fields_by_name['packed_nested_enum']._options = None
  _TESTMISSINGENUMVALUES.fields_by_name['packed_nested_enum']._serialized_options = b'\020\001'
  _TESTENUMVALUES._serialized_start=89
  _TESTENUMVALUES._serialized_end=410
  _TESTENUMVALUES_NESTEDENUM._serialized_start=379
  _TESTENUMVALUES_NESTEDENUM._serialized_end=410
  _TESTMISSINGENUMVALUES._serialized_start=413
  _TESTMISSINGENUMVALUES._serialized_end=752
  _TESTMISSINGENUMVALUES_NESTEDENUM._serialized_start=731
  _TESTMISSINGENUMVALUES_NESTEDENUM._serialized_end=752
  _JUSTSTRING._serialized_start=754
  _JUSTSTRING._serialized_end=781
# @@protoc_insertion_point(module_scope)
