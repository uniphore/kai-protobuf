# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/test_messages_proto3.proto
"""Generated protocol buffer code."""
from _google.protobuf.internal import builder as _builder
from _google.protobuf import descriptor as _descriptor
from _google.protobuf import descriptor_pool as _descriptor_pool
from _google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from _google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from _google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from _google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from _google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from _google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from _google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/protobuf/test_messages_proto3.proto\x12\x1dprotobuf_test_messages.proto3\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xb1\x45\n\x12TestAllTypesProto3\x12\x16\n\x0eoptional_int32\x18\x01 \x01(\x05\x12\x16\n\x0eoptional_int64\x18\x02 \x01(\x03\x12\x17\n\x0foptional_uint32\x18\x03 \x01(\r\x12\x17\n\x0foptional_uint64\x18\x04 \x01(\x04\x12\x17\n\x0foptional_sint32\x18\x05 \x01(\x11\x12\x17\n\x0foptional_sint64\x18\x06 \x01(\x12\x12\x18\n\x10optional_fixed32\x18\x07 \x01(\x07\x12\x18\n\x10optional_fixed64\x18\x08 \x01(\x06\x12\x19\n\x11optional_sfixed32\x18\t \x01(\x0f\x12\x19\n\x11optional_sfixed64\x18\n \x01(\x10\x12\x16\n\x0eoptional_float\x18\x0b \x01(\x02\x12\x17\n\x0foptional_double\x18\x0c \x01(\x01\x12\x15\n\roptional_bool\x18\r \x01(\x08\x12\x17\n\x0foptional_string\x18\x0e \x01(\t\x12\x16\n\x0eoptional_bytes\x18\x0f \x01(\x0c\x12`\n\x17optional_nested_message\x18\x12 \x01(\x0b\x32?.protobuf_test_messages.proto3.TestAllTypesProto3.NestedMessage\x12O\n\x18optional_foreign_message\x18\x13 \x01(\x0b\x32-.protobuf_test_messages.proto3.ForeignMessage\x12Z\n\x14optional_nested_enum\x18\x15 \x01(\x0e\x32<.protobuf_test_messages.proto3.TestAllTypesProto3.NestedEnum\x12I\n\x15optional_foreign_enum\x18\x16 \x01(\x0e\x32*.protobuf_test_messages.proto3.ForeignEnum\x12\\\n\x15optional_aliased_enum\x18\x17 \x01(\x0e\x32=.protobuf_test_messages.proto3.TestAllTypesProto3.AliasedEnum\x12!\n\x15optional_string_piece\x18\x18 \x01(\tB\x02\x08\x02\x12\x19\n\roptional_cord\x18\x19 \x01(\tB\x02\x08\x01\x12L\n\x11recursive_message\x18\x1b \x01(\x0b\x32\x31.protobuf_test_messages.proto3.TestAllTypesProto3\x12\x16\n\x0erepeated_int32\x18\x1f \x03(\x05\x12\x16\n\x0erepeated_int64\x18  \x03(\x03\x12\x17\n\x0frepeated_uint32\x18! \x03(\r\x12\x17\n\x0frepeated_uint64\x18\" \x03(\x04\x12\x17\n\x0frepeated_sint32\x18# \x03(\x11\x12\x17\n\x0frepeated_sint64\x18$ \x03(\x12\x12\x18\n\x10repeated_fixed32\x18% \x03(\x07\x12\x18\n\x10repeated_fixed64\x18& \x03(\x06\x12\x19\n\x11repeated_sfixed32\x18\' \x03(\x0f\x12\x19\n\x11repeated_sfixed64\x18( \x03(\x10\x12\x16\n\x0erepeated_float\x18) \x03(\x02\x12\x17\n\x0frepeated_double\x18* \x03(\x01\x12\x15\n\rrepeated_bool\x18+ \x03(\x08\x12\x17\n\x0frepeated_string\x18, \x03(\t\x12\x16\n\x0erepeated_bytes\x18- \x03(\x0c\x12`\n\x17repeated_nested_message\x18\x30 \x03(\x0b\x32?.protobuf_test_messages.proto3.TestAllTypesProto3.NestedMessage\x12O\n\x18repeated_foreign_message\x18\x31 \x03(\x0b\x32-.protobuf_test_messages.proto3.ForeignMessage\x12Z\n\x14repeated_nested_enum\x18\x33 \x03(\x0e\x32<.protobuf_test_messages.proto3.TestAllTypesProto3.NestedEnum\x12I\n\x15repeated_foreign_enum\x18\x34 \x03(\x0e\x32*.protobuf_test_messages.proto3.ForeignEnum\x12!\n\x15repeated_string_piece\x18\x36 \x03(\tB\x02\x08\x02\x12\x19\n\rrepeated_cord\x18\x37 \x03(\tB\x02\x08\x01\x12\x18\n\x0cpacked_int32\x18K \x03(\x05\x42\x02\x10\x01\x12\x18\n\x0cpacked_int64\x18L \x03(\x03\x42\x02\x10\x01\x12\x19\n\rpacked_uint32\x18M \x03(\rB\x02\x10\x01\x12\x19\n\rpacked_uint64\x18N \x03(\x04\x42\x02\x10\x01\x12\x19\n\rpacked_sint32\x18O \x03(\x11\x42\x02\x10\x01\x12\x19\n\rpacked_sint64\x18P \x03(\x12\x42\x02\x10\x01\x12\x1a\n\x0epacked_fixed32\x18Q \x03(\x07\x42\x02\x10\x01\x12\x1a\n\x0epacked_fixed64\x18R \x03(\x06\x42\x02\x10\x01\x12\x1b\n\x0fpacked_sfixed32\x18S \x03(\x0f\x42\x02\x10\x01\x12\x1b\n\x0fpacked_sfixed64\x18T \x03(\x10\x42\x02\x10\x01\x12\x18\n\x0cpacked_float\x18U \x03(\x02\x42\x02\x10\x01\x12\x19\n\rpacked_double\x18V \x03(\x01\x42\x02\x10\x01\x12\x17\n\x0bpacked_bool\x18W \x03(\x08\x42\x02\x10\x01\x12\\\n\x12packed_nested_enum\x18X \x03(\x0e\x32<.protobuf_test_messages.proto3.TestAllTypesProto3.NestedEnumB\x02\x10\x01\x12\x1a\n\x0eunpacked_int32\x18Y \x03(\x05\x42\x02\x10\x00\x12\x1a\n\x0eunpacked_int64\x18Z \x03(\x03\x42\x02\x10\x00\x12\x1b\n\x0funpacked_uint32\x18[ \x03(\rB\x02\x10\x00\x12\x1b\n\x0funpacked_uint64\x18\\ \x03(\x04\x42\x02\x10\x00\x12\x1b\n\x0funpacked_sint32\x18] \x03(\x11\x42\x02\x10\x00\x12\x1b\n\x0funpacked_sint64\x18^ \x03(\x12\x42\x02\x10\x00\x12\x1c\n\x10unpacked_fixed32\x18_ \x03(\x07\x42\x02\x10\x00\x12\x1c\n\x10unpacked_fixed64\x18` \x03(\x06\x42\x02\x10\x00\x12\x1d\n\x11unpacked_sfixed32\x18\x61 \x03(\x0f\x42\x02\x10\x00\x12\x1d\n\x11unpacked_sfixed64\x18\x62 \x03(\x10\x42\x02\x10\x00\x12\x1a\n\x0eunpacked_float\x18\x63 \x03(\x02\x42\x02\x10\x00\x12\x1b\n\x0funpacked_double\x18\x64 \x03(\x01\x42\x02\x10\x00\x12\x19\n\runpacked_bool\x18\x65 \x03(\x08\x42\x02\x10\x00\x12^\n\x14unpacked_nested_enum\x18\x66 \x03(\x0e\x32<.protobuf_test_messages.proto3.TestAllTypesProto3.NestedEnumB\x02\x10\x00\x12]\n\x0fmap_int32_int32\x18\x38 \x03(\x0b\x32\x44.protobuf_test_messages.proto3.TestAllTypesProto3.MapInt32Int32Entry\x12]\n\x0fmap_int64_int64\x18\x39 \x03(\x0b\x32\x44.protobuf_test_messages.proto3.TestAllTypesProto3.MapInt64Int64Entry\x12\x61\n\x11map_uint32_uint32\x18: \x03(\x0b\x32\x46.protobuf_test_messages.proto3.TestAllTypesProto3.MapUint32Uint32Entry\x12\x61\n\x11map_uint64_uint64\x18; \x03(\x0b\x32\x46.protobuf_test_messages.proto3.TestAllTypesProto3.MapUint64Uint64Entry\x12\x61\n\x11map_sint32_sint32\x18< \x03(\x0b\x32\x46.protobuf_test_messages.proto3.TestAllTypesProto3.MapSint32Sint32Entry\x12\x61\n\x11map_sint64_sint64\x18= \x03(\x0b\x32\x46.protobuf_test_messages.proto3.TestAllTypesProto3.MapSint64Sint64Entry\x12\x65\n\x13map_fixed32_fixed32\x18> \x03(\x0b\x32H.protobuf_test_messages.proto3.TestAllTypesProto3.MapFixed32Fixed32Entry\x12\x65\n\x13map_fixed64_fixed64\x18? \x03(\x0b\x32H.protobuf_test_messages.proto3.TestAllTypesProto3.MapFixed64Fixed64Entry\x12i\n\x15map_sfixed32_sfixed32\x18@ \x03(\x0b\x32J.protobuf_test_messages.proto3.TestAllTypesProto3.MapSfixed32Sfixed32Entry\x12i\n\x15map_sfixed64_sfixed64\x18\x41 \x03(\x0b\x32J.protobuf_test_messages.proto3.TestAllTypesProto3.MapSfixed64Sfixed64Entry\x12]\n\x0fmap_int32_float\x18\x42 \x03(\x0b\x32\x44.protobuf_test_messages.proto3.TestAllTypesProto3.MapInt32FloatEntry\x12_\n\x10map_int32_double\x18\x43 \x03(\x0b\x32\x45.protobuf_test_messages.proto3.TestAllTypesProto3.MapInt32DoubleEntry\x12Y\n\rmap_bool_bool\x18\x44 \x03(\x0b\x32\x42.protobuf_test_messages.proto3.TestAllTypesProto3.MapBoolBoolEntry\x12\x61\n\x11map_string_string\x18\x45 \x03(\x0b\x32\x46.protobuf_test_messages.proto3.TestAllTypesProto3.MapStringStringEntry\x12_\n\x10map_string_bytes\x18\x46 \x03(\x0b\x32\x45.protobuf_test_messages.proto3.TestAllTypesProto3.MapStringBytesEntry\x12p\n\x19map_string_nested_message\x18G \x03(\x0b\x32M.protobuf_test_messages.proto3.TestAllTypesProto3.MapStringNestedMessageEntry\x12r\n\x1amap_string_foreign_message\x18H \x03(\x0b\x32N.protobuf_test_messages.proto3.TestAllTypesProto3.MapStringForeignMessageEntry\x12j\n\x16map_string_nested_enum\x18I \x03(\x0b\x32J.protobuf_test_messages.proto3.TestAllTypesProto3.MapStringNestedEnumEntry\x12l\n\x17map_string_foreign_enum\x18J \x03(\x0b\x32K.protobuf_test_messages.proto3.TestAllTypesProto3.MapStringForeignEnumEntry\x12\x16\n\x0coneof_uint32\x18o \x01(\rH\x00\x12_\n\x14oneof_nested_message\x18p \x01(\x0b\x32?.protobuf_test_messages.proto3.TestAllTypesProto3.NestedMessageH\x00\x12\x16\n\x0coneof_string\x18q \x01(\tH\x00\x12\x15\n\x0boneof_bytes\x18r \x01(\x0cH\x00\x12\x14\n\noneof_bool\x18s \x01(\x08H\x00\x12\x16\n\x0coneof_uint64\x18t \x01(\x04H\x00\x12\x15\n\x0boneof_float\x18u \x01(\x02H\x00\x12\x16\n\x0coneof_double\x18v \x01(\x01H\x00\x12R\n\noneof_enum\x18w \x01(\x0e\x32<.protobuf_test_messages.proto3.TestAllTypesProto3.NestedEnumH\x00\x12\x36\n\x10oneof_null_value\x18x \x01(\x0e\x32\x1a.google.protobuf.NullValueH\x00\x12:\n\x15optional_bool_wrapper\x18\xc9\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12<\n\x16optional_int32_wrapper\x18\xca\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12<\n\x16optional_int64_wrapper\x18\xcb\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12>\n\x17optional_uint32_wrapper\x18\xcc\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12>\n\x17optional_uint64_wrapper\x18\xcd\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12<\n\x16optional_float_wrapper\x18\xce\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12>\n\x17optional_double_wrapper\x18\xcf\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12>\n\x17optional_string_wrapper\x18\xd0\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12<\n\x16optional_bytes_wrapper\x18\xd1\x01 \x01(\x0b\x32\x1b.google.protobuf.BytesValue\x12:\n\x15repeated_bool_wrapper\x18\xd3\x01 \x03(\x0b\x32\x1a.google.protobuf.BoolValue\x12<\n\x16repeated_int32_wrapper\x18\xd4\x01 \x03(\x0b\x32\x1b.google.protobuf.Int32Value\x12<\n\x16repeated_int64_wrapper\x18\xd5\x01 \x03(\x0b\x32\x1b.google.protobuf.Int64Value\x12>\n\x17repeated_uint32_wrapper\x18\xd6\x01 \x03(\x0b\x32\x1c.google.protobuf.UInt32Value\x12>\n\x17repeated_uint64_wrapper\x18\xd7\x01 \x03(\x0b\x32\x1c.google.protobuf.UInt64Value\x12<\n\x16repeated_float_wrapper\x18\xd8\x01 \x03(\x0b\x32\x1b.google.protobuf.FloatValue\x12>\n\x17repeated_double_wrapper\x18\xd9\x01 \x03(\x0b\x32\x1c.google.protobuf.DoubleValue\x12>\n\x17repeated_string_wrapper\x18\xda\x01 \x03(\x0b\x32\x1c.google.protobuf.StringValue\x12<\n\x16repeated_bytes_wrapper\x18\xdb\x01 \x03(\x0b\x32\x1b.google.protobuf.BytesValue\x12\x35\n\x11optional_duration\x18\xad\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x37\n\x12optional_timestamp\x18\xae\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x13optional_field_mask\x18\xaf\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x31\n\x0foptional_struct\x18\xb0\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12+\n\x0coptional_any\x18\xb1\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12/\n\x0eoptional_value\x18\xb2\x02 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x38\n\x13optional_null_value\x18\xb3\x02 \x01(\x0e\x32\x1a.google.protobuf.NullValue\x12\x35\n\x11repeated_duration\x18\xb7\x02 \x03(\x0b\x32\x19.google.protobuf.Duration\x12\x37\n\x12repeated_timestamp\x18\xb8\x02 \x03(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x12repeated_fieldmask\x18\xb9\x02 \x03(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x31\n\x0frepeated_struct\x18\xc4\x02 \x03(\x0b\x32\x17.google.protobuf.Struct\x12+\n\x0crepeated_any\x18\xbb\x02 \x03(\x0b\x32\x14.google.protobuf.Any\x12/\n\x0erepeated_value\x18\xbc\x02 \x03(\x0b\x32\x16.google.protobuf.Value\x12\x38\n\x13repeated_list_value\x18\xbd\x02 \x03(\x0b\x32\x1a.google.protobuf.ListValue\x12\x13\n\nfieldname1\x18\x91\x03 \x01(\x05\x12\x14\n\x0b\x66ield_name2\x18\x92\x03 \x01(\x05\x12\x15\n\x0c_field_name3\x18\x93\x03 \x01(\x05\x12\x16\n\rfield__name4_\x18\x94\x03 \x01(\x05\x12\x14\n\x0b\x66ield0name5\x18\x95\x03 \x01(\x05\x12\x16\n\rfield_0_name6\x18\x96\x03 \x01(\x05\x12\x13\n\nfieldName7\x18\x97\x03 \x01(\x05\x12\x13\n\nFieldName8\x18\x98\x03 \x01(\x05\x12\x14\n\x0b\x66ield_Name9\x18\x99\x03 \x01(\x05\x12\x15\n\x0c\x46ield_Name10\x18\x9a\x03 \x01(\x05\x12\x15\n\x0c\x46IELD_NAME11\x18\x9b\x03 \x01(\x05\x12\x15\n\x0c\x46IELD_name12\x18\x9c\x03 \x01(\x05\x12\x17\n\x0e__field_name13\x18\x9d\x03 \x01(\x05\x12\x17\n\x0e__Field_name14\x18\x9e\x03 \x01(\x05\x12\x16\n\rfield__name15\x18\x9f\x03 \x01(\x05\x12\x16\n\rfield__Name16\x18\xa0\x03 \x01(\x05\x12\x17\n\x0e\x66ield_name17__\x18\xa1\x03 \x01(\x05\x12\x17\n\x0e\x46ield_name18__\x18\xa2\x03 \x01(\x05\x1a\x62\n\rNestedMessage\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\x46\n\x0b\x63orecursive\x18\x02 \x01(\x0b\x32\x31.protobuf_test_messages.proto3.TestAllTypesProto3\x1a\x34\n\x12MapInt32Int32Entry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x34\n\x12MapInt64Int64Entry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x36\n\x14MapUint32Uint32Entry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x36\n\x14MapUint64Uint64Entry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a\x36\n\x14MapSint32Sint32Entry\x12\x0b\n\x03key\x18\x01 \x01(\x11\x12\r\n\x05value\x18\x02 \x01(\x11:\x02\x38\x01\x1a\x36\n\x14MapSint64Sint64Entry\x12\x0b\n\x03key\x18\x01 \x01(\x12\x12\r\n\x05value\x18\x02 \x01(\x12:\x02\x38\x01\x1a\x38\n\x16MapFixed32Fixed32Entry\x12\x0b\n\x03key\x18\x01 \x01(\x07\x12\r\n\x05value\x18\x02 \x01(\x07:\x02\x38\x01\x1a\x38\n\x16MapFixed64Fixed64Entry\x12\x0b\n\x03key\x18\x01 \x01(\x06\x12\r\n\x05value\x18\x02 \x01(\x06:\x02\x38\x01\x1a:\n\x18MapSfixed32Sfixed32Entry\x12\x0b\n\x03key\x18\x01 \x01(\x0f\x12\r\n\x05value\x18\x02 \x01(\x0f:\x02\x38\x01\x1a:\n\x18MapSfixed64Sfixed64Entry\x12\x0b\n\x03key\x18\x01 \x01(\x10\x12\r\n\x05value\x18\x02 \x01(\x10:\x02\x38\x01\x1a\x34\n\x12MapInt32FloatEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x1a\x35\n\x13MapInt32DoubleEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a\x32\n\x10MapBoolBoolEntry\x12\x0b\n\x03key\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a\x36\n\x14MapStringStringEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x35\n\x13MapStringBytesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a~\n\x1bMapStringNestedMessageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0b\x32?.protobuf_test_messages.proto3.TestAllTypesProto3.NestedMessage:\x02\x38\x01\x1am\n\x1cMapStringForeignMessageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b\x32-.protobuf_test_messages.proto3.ForeignMessage:\x02\x38\x01\x1ax\n\x18MapStringNestedEnumEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12K\n\x05value\x18\x02 \x01(\x0e\x32<.protobuf_test_messages.proto3.TestAllTypesProto3.NestedEnum:\x02\x38\x01\x1ag\n\x19MapStringForeignEnumEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x39\n\x05value\x18\x02 \x01(\x0e\x32*.protobuf_test_messages.proto3.ForeignEnum:\x02\x38\x01\"9\n\nNestedEnum\x12\x07\n\x03\x46OO\x10\x00\x12\x07\n\x03\x42\x41R\x10\x01\x12\x07\n\x03\x42\x41Z\x10\x02\x12\x10\n\x03NEG\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\"Y\n\x0b\x41liasedEnum\x12\r\n\tALIAS_FOO\x10\x00\x12\r\n\tALIAS_BAR\x10\x01\x12\r\n\tALIAS_BAZ\x10\x02\x12\x07\n\x03MOO\x10\x02\x12\x07\n\x03moo\x10\x02\x12\x07\n\x03\x62\x41z\x10\x02\x1a\x02\x10\x01\x42\r\n\x0boneof_fieldJ\x06\x08\xf5\x03\x10\xff\x03\"\x1b\n\x0e\x46oreignMessage\x12\t\n\x01\x63\x18\x01 \x01(\x05\"\x16\n\x14NullHypothesisProto3\"/\n\x0e\x45numOnlyProto3\"\x1d\n\x04\x42ool\x12\n\n\x06kFalse\x10\x00\x12\t\n\x05kTrue\x10\x01*@\n\x0b\x46oreignEnum\x12\x0f\n\x0b\x46OREIGN_FOO\x10\x00\x12\x0f\n\x0b\x46OREIGN_BAR\x10\x01\x12\x0f\n\x0b\x46OREIGN_BAZ\x10\x02\x42\x38\n(com.google.protobuf_test_messages.proto3H\x01\xf8\x01\x01\xa2\x02\x06Proto3b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.protobuf.test_messages_proto3_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(com.google.protobuf_test_messages.proto3H\001\370\001\001\242\002\006Proto3'
  _TESTALLTYPESPROTO3_MAPINT32INT32ENTRY._options = None
  _TESTALLTYPESPROTO3_MAPINT32INT32ENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPINT64INT64ENTRY._options = None
  _TESTALLTYPESPROTO3_MAPINT64INT64ENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPUINT32UINT32ENTRY._options = None
  _TESTALLTYPESPROTO3_MAPUINT32UINT32ENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPUINT64UINT64ENTRY._options = None
  _TESTALLTYPESPROTO3_MAPUINT64UINT64ENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPSINT32SINT32ENTRY._options = None
  _TESTALLTYPESPROTO3_MAPSINT32SINT32ENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPSINT64SINT64ENTRY._options = None
  _TESTALLTYPESPROTO3_MAPSINT64SINT64ENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPFIXED32FIXED32ENTRY._options = None
  _TESTALLTYPESPROTO3_MAPFIXED32FIXED32ENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPFIXED64FIXED64ENTRY._options = None
  _TESTALLTYPESPROTO3_MAPFIXED64FIXED64ENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPSFIXED32SFIXED32ENTRY._options = None
  _TESTALLTYPESPROTO3_MAPSFIXED32SFIXED32ENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPSFIXED64SFIXED64ENTRY._options = None
  _TESTALLTYPESPROTO3_MAPSFIXED64SFIXED64ENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPINT32FLOATENTRY._options = None
  _TESTALLTYPESPROTO3_MAPINT32FLOATENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPINT32DOUBLEENTRY._options = None
  _TESTALLTYPESPROTO3_MAPINT32DOUBLEENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPBOOLBOOLENTRY._options = None
  _TESTALLTYPESPROTO3_MAPBOOLBOOLENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPSTRINGSTRINGENTRY._options = None
  _TESTALLTYPESPROTO3_MAPSTRINGSTRINGENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPSTRINGBYTESENTRY._options = None
  _TESTALLTYPESPROTO3_MAPSTRINGBYTESENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPSTRINGNESTEDMESSAGEENTRY._options = None
  _TESTALLTYPESPROTO3_MAPSTRINGNESTEDMESSAGEENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPSTRINGFOREIGNMESSAGEENTRY._options = None
  _TESTALLTYPESPROTO3_MAPSTRINGFOREIGNMESSAGEENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPSTRINGNESTEDENUMENTRY._options = None
  _TESTALLTYPESPROTO3_MAPSTRINGNESTEDENUMENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_MAPSTRINGFOREIGNENUMENTRY._options = None
  _TESTALLTYPESPROTO3_MAPSTRINGFOREIGNENUMENTRY._serialized_options = b'8\001'
  _TESTALLTYPESPROTO3_ALIASEDENUM._options = None
  _TESTALLTYPESPROTO3_ALIASEDENUM._serialized_options = b'\020\001'
  _TESTALLTYPESPROTO3.fields_by_name['optional_string_piece']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['optional_string_piece']._serialized_options = b'\010\002'
  _TESTALLTYPESPROTO3.fields_by_name['optional_cord']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['optional_cord']._serialized_options = b'\010\001'
  _TESTALLTYPESPROTO3.fields_by_name['repeated_string_piece']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['repeated_string_piece']._serialized_options = b'\010\002'
  _TESTALLTYPESPROTO3.fields_by_name['repeated_cord']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['repeated_cord']._serialized_options = b'\010\001'
  _TESTALLTYPESPROTO3.fields_by_name['packed_int32']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['packed_int32']._serialized_options = b'\020\001'
  _TESTALLTYPESPROTO3.fields_by_name['packed_int64']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['packed_int64']._serialized_options = b'\020\001'
  _TESTALLTYPESPROTO3.fields_by_name['packed_uint32']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['packed_uint32']._serialized_options = b'\020\001'
  _TESTALLTYPESPROTO3.fields_by_name['packed_uint64']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['packed_uint64']._serialized_options = b'\020\001'
  _TESTALLTYPESPROTO3.fields_by_name['packed_sint32']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['packed_sint32']._serialized_options = b'\020\001'
  _TESTALLTYPESPROTO3.fields_by_name['packed_sint64']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['packed_sint64']._serialized_options = b'\020\001'
  _TESTALLTYPESPROTO3.fields_by_name['packed_fixed32']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['packed_fixed32']._serialized_options = b'\020\001'
  _TESTALLTYPESPROTO3.fields_by_name['packed_fixed64']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['packed_fixed64']._serialized_options = b'\020\001'
  _TESTALLTYPESPROTO3.fields_by_name['packed_sfixed32']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['packed_sfixed32']._serialized_options = b'\020\001'
  _TESTALLTYPESPROTO3.fields_by_name['packed_sfixed64']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['packed_sfixed64']._serialized_options = b'\020\001'
  _TESTALLTYPESPROTO3.fields_by_name['packed_float']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['packed_float']._serialized_options = b'\020\001'
  _TESTALLTYPESPROTO3.fields_by_name['packed_double']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['packed_double']._serialized_options = b'\020\001'
  _TESTALLTYPESPROTO3.fields_by_name['packed_bool']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['packed_bool']._serialized_options = b'\020\001'
  _TESTALLTYPESPROTO3.fields_by_name['packed_nested_enum']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['packed_nested_enum']._serialized_options = b'\020\001'
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_int32']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_int32']._serialized_options = b'\020\000'
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_int64']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_int64']._serialized_options = b'\020\000'
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_uint32']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_uint32']._serialized_options = b'\020\000'
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_uint64']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_uint64']._serialized_options = b'\020\000'
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_sint32']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_sint32']._serialized_options = b'\020\000'
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_sint64']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_sint64']._serialized_options = b'\020\000'
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_fixed32']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_fixed32']._serialized_options = b'\020\000'
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_fixed64']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_fixed64']._serialized_options = b'\020\000'
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_sfixed32']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_sfixed32']._serialized_options = b'\020\000'
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_sfixed64']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_sfixed64']._serialized_options = b'\020\000'
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_float']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_float']._serialized_options = b'\020\000'
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_double']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_double']._serialized_options = b'\020\000'
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_bool']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_bool']._serialized_options = b'\020\000'
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_nested_enum']._options = None
  _TESTALLTYPESPROTO3.fields_by_name['unpacked_nested_enum']._serialized_options = b'\020\000'
  _FOREIGNENUM._serialized_start=9251
  _FOREIGNENUM._serialized_end=9315
  _TESTALLTYPESPROTO3._serialized_start=266
  _TESTALLTYPESPROTO3._serialized_end=9147
  _TESTALLTYPESPROTO3_NESTEDMESSAGE._serialized_start=7570
  _TESTALLTYPESPROTO3_NESTEDMESSAGE._serialized_end=7668
  _TESTALLTYPESPROTO3_MAPINT32INT32ENTRY._serialized_start=7670
  _TESTALLTYPESPROTO3_MAPINT32INT32ENTRY._serialized_end=7722
  _TESTALLTYPESPROTO3_MAPINT64INT64ENTRY._serialized_start=7724
  _TESTALLTYPESPROTO3_MAPINT64INT64ENTRY._serialized_end=7776
  _TESTALLTYPESPROTO3_MAPUINT32UINT32ENTRY._serialized_start=7778
  _TESTALLTYPESPROTO3_MAPUINT32UINT32ENTRY._serialized_end=7832
  _TESTALLTYPESPROTO3_MAPUINT64UINT64ENTRY._serialized_start=7834
  _TESTALLTYPESPROTO3_MAPUINT64UINT64ENTRY._serialized_end=7888
  _TESTALLTYPESPROTO3_MAPSINT32SINT32ENTRY._serialized_start=7890
  _TESTALLTYPESPROTO3_MAPSINT32SINT32ENTRY._serialized_end=7944
  _TESTALLTYPESPROTO3_MAPSINT64SINT64ENTRY._serialized_start=7946
  _TESTALLTYPESPROTO3_MAPSINT64SINT64ENTRY._serialized_end=8000
  _TESTALLTYPESPROTO3_MAPFIXED32FIXED32ENTRY._serialized_start=8002
  _TESTALLTYPESPROTO3_MAPFIXED32FIXED32ENTRY._serialized_end=8058
  _TESTALLTYPESPROTO3_MAPFIXED64FIXED64ENTRY._serialized_start=8060
  _TESTALLTYPESPROTO3_MAPFIXED64FIXED64ENTRY._serialized_end=8116
  _TESTALLTYPESPROTO3_MAPSFIXED32SFIXED32ENTRY._serialized_start=8118
  _TESTALLTYPESPROTO3_MAPSFIXED32SFIXED32ENTRY._serialized_end=8176
  _TESTALLTYPESPROTO3_MAPSFIXED64SFIXED64ENTRY._serialized_start=8178
  _TESTALLTYPESPROTO3_MAPSFIXED64SFIXED64ENTRY._serialized_end=8236
  _TESTALLTYPESPROTO3_MAPINT32FLOATENTRY._serialized_start=8238
  _TESTALLTYPESPROTO3_MAPINT32FLOATENTRY._serialized_end=8290
  _TESTALLTYPESPROTO3_MAPINT32DOUBLEENTRY._serialized_start=8292
  _TESTALLTYPESPROTO3_MAPINT32DOUBLEENTRY._serialized_end=8345
  _TESTALLTYPESPROTO3_MAPBOOLBOOLENTRY._serialized_start=8347
  _TESTALLTYPESPROTO3_MAPBOOLBOOLENTRY._serialized_end=8397
  _TESTALLTYPESPROTO3_MAPSTRINGSTRINGENTRY._serialized_start=8399
  _TESTALLTYPESPROTO3_MAPSTRINGSTRINGENTRY._serialized_end=8453
  _TESTALLTYPESPROTO3_MAPSTRINGBYTESENTRY._serialized_start=8455
  _TESTALLTYPESPROTO3_MAPSTRINGBYTESENTRY._serialized_end=8508
  _TESTALLTYPESPROTO3_MAPSTRINGNESTEDMESSAGEENTRY._serialized_start=8510
  _TESTALLTYPESPROTO3_MAPSTRINGNESTEDMESSAGEENTRY._serialized_end=8636
  _TESTALLTYPESPROTO3_MAPSTRINGFOREIGNMESSAGEENTRY._serialized_start=8638
  _TESTALLTYPESPROTO3_MAPSTRINGFOREIGNMESSAGEENTRY._serialized_end=8747
  _TESTALLTYPESPROTO3_MAPSTRINGNESTEDENUMENTRY._serialized_start=8749
  _TESTALLTYPESPROTO3_MAPSTRINGNESTEDENUMENTRY._serialized_end=8869
  _TESTALLTYPESPROTO3_MAPSTRINGFOREIGNENUMENTRY._serialized_start=8871
  _TESTALLTYPESPROTO3_MAPSTRINGFOREIGNENUMENTRY._serialized_end=8974
  _TESTALLTYPESPROTO3_NESTEDENUM._serialized_start=8976
  _TESTALLTYPESPROTO3_NESTEDENUM._serialized_end=9033
  _TESTALLTYPESPROTO3_ALIASEDENUM._serialized_start=9035
  _TESTALLTYPESPROTO3_ALIASEDENUM._serialized_end=9124
  _FOREIGNMESSAGE._serialized_start=9149
  _FOREIGNMESSAGE._serialized_end=9176
  _NULLHYPOTHESISPROTO3._serialized_start=9178
  _NULLHYPOTHESISPROTO3._serialized_end=9200
  _ENUMONLYPROTO3._serialized_start=9202
  _ENUMONLYPROTO3._serialized_end=9249
  _ENUMONLYPROTO3_BOOL._serialized_start=9220
  _ENUMONLYPROTO3_BOOL._serialized_end=9249
# @@protoc_insertion_point(module_scope)
