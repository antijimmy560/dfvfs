# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='pyvfs/proto/transmission.proto',
  package='transmission',
  serialized_pb='\n\x1epyvfs/proto/transmission.proto\x12\x0ctransmission\"\x94\x01\n\x08PathSpec\x12&\n\x06parent\x18\x01 \x01(\x0b\x32\x16.transmission.PathSpec\x12\x16\n\x0etype_indicator\x18\x02 \x02(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x12\n\nidentifier\x18\x04 \x01(\t\x12\r\n\x05inode\x18\x05 \x01(\x04\x12\x13\n\x0bstore_index\x18\x06 \x01(\x04')




_PATHSPEC = descriptor.Descriptor(
  name='PathSpec',
  full_name='transmission.PathSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='parent', full_name='transmission.PathSpec.parent', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type_indicator', full_name='transmission.PathSpec.type_indicator', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='location', full_name='transmission.PathSpec.location', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='identifier', full_name='transmission.PathSpec.identifier', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='inode', full_name='transmission.PathSpec.inode', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='store_index', full_name='transmission.PathSpec.store_index', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=49,
  serialized_end=197,
)

_PATHSPEC.fields_by_name['parent'].message_type = _PATHSPEC
DESCRIPTOR.message_types_by_name['PathSpec'] = _PATHSPEC

class PathSpec(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PATHSPEC
  
  # @@protoc_insertion_point(class_scope:transmission.PathSpec)

# @@protoc_insertion_point(module_scope)
