# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tip.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tip.proto',
  package='Tip',
  syntax='proto2',
  serialized_pb=_b('\n\ttip.proto\x12\x03Tip\"P\n\tReviewTip\x12\x0e\n\x06tipUrl\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x10\n\x08polarity\x18\x03 \x01(\x05\x12\x13\n\x0breviewCount\x18\x04 \x01(\x03\x42\'\n com.google.android.finsky.protosB\x03Tip')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REVIEWTIP = _descriptor.Descriptor(
  name='ReviewTip',
  full_name='Tip.ReviewTip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tipUrl', full_name='Tip.ReviewTip.tipUrl', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='Tip.ReviewTip.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='polarity', full_name='Tip.ReviewTip.polarity', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reviewCount', full_name='Tip.ReviewTip.reviewCount', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=98,
)

DESCRIPTOR.message_types_by_name['ReviewTip'] = _REVIEWTIP

ReviewTip = _reflection.GeneratedProtocolMessageType('ReviewTip', (_message.Message,), dict(
  DESCRIPTOR = _REVIEWTIP,
  __module__ = 'tip_pb2'
  # @@protoc_insertion_point(class_scope:Tip.ReviewTip)
  ))
_sym_db.RegisterMessage(ReviewTip)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n com.google.android.finsky.protosB\003Tip'))
# @@protoc_insertion_point(module_scope)