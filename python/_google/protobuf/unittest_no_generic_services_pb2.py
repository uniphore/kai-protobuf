# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/unittest_no_generic_services.proto
"""Generated protocol buffer code."""
from _google.protobuf.internal import builder as _builder
from _google.protobuf import descriptor as _descriptor
from _google.protobuf import descriptor_pool as _descriptor_pool
from _google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/protobuf/unittest_no_generic_services.proto\x12*protobuf_unittest.no_generic_services_test\"#\n\x0bTestMessage\x12\t\n\x01\x61\x18\x01 \x01(\x05*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02*\x13\n\x08TestEnum\x12\x07\n\x03\x46OO\x10\x01\x32\x86\x01\n\x0bTestService\x12w\n\x03\x46oo\x12\x37.protobuf_unittest.no_generic_services_test.TestMessage\x1a\x37.protobuf_unittest.no_generic_services_test.TestMessage:P\n\x0etest_extension\x12\x37.protobuf_unittest.no_generic_services_test.TestMessage\x18\xe8\x07 \x01(\x05')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.protobuf.unittest_no_generic_services_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  TestMessage.RegisterExtension(test_extension)

  DESCRIPTOR._options = None
  _TESTENUM._serialized_start=135
  _TESTENUM._serialized_end=154
  _TESTMESSAGE._serialized_start=98
  _TESTMESSAGE._serialized_end=133
  _TESTSERVICE._serialized_start=157
  _TESTSERVICE._serialized_end=291
# @@protoc_insertion_point(module_scope)
