# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: content_filters.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='content_filters.proto',
  package='ContentFilters',
  syntax='proto2',
  serialized_pb=_b('\n\x15\x63ontent_filters.proto\x12\x0e\x43ontentFilters\x1a\x0c\x63ommon.proto\"\xb6\x01\n\x1d\x43ontentFilterSettingsResponse\x12\x30\n\x0b\x66ilterRange\x18\x01 \x03(\x0b\x32\x1b.ContentFilters.FilterRange\x12\x14\n\x0ctutorialText\x18\x02 \x01(\t\x12(\n\x11tutorialImageFife\x18\x03 \x01(\x0b\x32\r.Common.Image\x12\x11\n\tinfoTitle\x18\x04 \x01(\t\x12\x10\n\x08infoText\x18\x05 \x01(\t\"\xcf\x02\n\x0b\x46ilterRange\x12\x14\n\x0c\x64ocumentType\x18\x01 \x03(\x05\x12\x13\n\x0b\x61uthorityId\x18\x02 \x01(\x05\x12\x32\n\x0c\x66ilterChoice\x18\x03 \x03(\x0b\x32\x1c.ContentFilters.FilterChoice\x12\r\n\x05label\x18\x04 \x01(\t\x12\x1f\n\x08iconFife\x18\x05 \x01(\x0b\x32\r.Common.Image\x12\x1c\n\x14selectionDialogLabel\x18\x06 \x01(\t\x12\x1f\n\x17\x63onfirmationDialogTitle\x18\x07 \x01(\t\x12!\n\x19\x63onfirmationDialogContent\x18\x08 \x01(\t\x12\x1f\n\x17representChoiceAsToggle\x18\t \x01(\x08\x12\x16\n\x0e\x61ppPackageName\x18\n \x01(\t\x12\x16\n\x0eminVersionCode\x18\x0b \x01(\x05\"\x8e\x01\n\x0c\x46ilterChoice\x12\r\n\x05level\x18\x01 \x01(\x05\x12 \n\timageFife\x18\x02 \x01(\x0b\x32\r.Common.Image\x12\r\n\x05label\x18\x03 \x01(\t\x12\x16\n\x0e\x64\x66\x65HeaderValue\x18\x04 \x01(\t\x12\x10\n\x08selected\x18\x05 \x01(\x08\x12\x14\n\x0clabelSummary\x18\x06 \x01(\tB2\n com.google.android.finsky.protosB\x0e\x43ontentFilters')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CONTENTFILTERSETTINGSRESPONSE = _descriptor.Descriptor(
  name='ContentFilterSettingsResponse',
  full_name='ContentFilters.ContentFilterSettingsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filterRange', full_name='ContentFilters.ContentFilterSettingsResponse.filterRange', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tutorialText', full_name='ContentFilters.ContentFilterSettingsResponse.tutorialText', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tutorialImageFife', full_name='ContentFilters.ContentFilterSettingsResponse.tutorialImageFife', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='infoTitle', full_name='ContentFilters.ContentFilterSettingsResponse.infoTitle', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='infoText', full_name='ContentFilters.ContentFilterSettingsResponse.infoText', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=56,
  serialized_end=238,
)


_FILTERRANGE = _descriptor.Descriptor(
  name='FilterRange',
  full_name='ContentFilters.FilterRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='documentType', full_name='ContentFilters.FilterRange.documentType', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authorityId', full_name='ContentFilters.FilterRange.authorityId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filterChoice', full_name='ContentFilters.FilterRange.filterChoice', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='ContentFilters.FilterRange.label', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iconFife', full_name='ContentFilters.FilterRange.iconFife', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='selectionDialogLabel', full_name='ContentFilters.FilterRange.selectionDialogLabel', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confirmationDialogTitle', full_name='ContentFilters.FilterRange.confirmationDialogTitle', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confirmationDialogContent', full_name='ContentFilters.FilterRange.confirmationDialogContent', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='representChoiceAsToggle', full_name='ContentFilters.FilterRange.representChoiceAsToggle', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appPackageName', full_name='ContentFilters.FilterRange.appPackageName', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minVersionCode', full_name='ContentFilters.FilterRange.minVersionCode', index=10,
      number=11, type=5, cpp_type=1, label=1,
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
  serialized_start=241,
  serialized_end=576,
)


_FILTERCHOICE = _descriptor.Descriptor(
  name='FilterChoice',
  full_name='ContentFilters.FilterChoice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='ContentFilters.FilterChoice.level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageFife', full_name='ContentFilters.FilterChoice.imageFife', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='ContentFilters.FilterChoice.label', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dfeHeaderValue', full_name='ContentFilters.FilterChoice.dfeHeaderValue', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='selected', full_name='ContentFilters.FilterChoice.selected', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labelSummary', full_name='ContentFilters.FilterChoice.labelSummary', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=579,
  serialized_end=721,
)

_CONTENTFILTERSETTINGSRESPONSE.fields_by_name['filterRange'].message_type = _FILTERRANGE
_CONTENTFILTERSETTINGSRESPONSE.fields_by_name['tutorialImageFife'].message_type = common__pb2._IMAGE
_FILTERRANGE.fields_by_name['filterChoice'].message_type = _FILTERCHOICE
_FILTERRANGE.fields_by_name['iconFife'].message_type = common__pb2._IMAGE
_FILTERCHOICE.fields_by_name['imageFife'].message_type = common__pb2._IMAGE
DESCRIPTOR.message_types_by_name['ContentFilterSettingsResponse'] = _CONTENTFILTERSETTINGSRESPONSE
DESCRIPTOR.message_types_by_name['FilterRange'] = _FILTERRANGE
DESCRIPTOR.message_types_by_name['FilterChoice'] = _FILTERCHOICE

ContentFilterSettingsResponse = _reflection.GeneratedProtocolMessageType('ContentFilterSettingsResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONTENTFILTERSETTINGSRESPONSE,
  __module__ = 'content_filters_pb2'
  # @@protoc_insertion_point(class_scope:ContentFilters.ContentFilterSettingsResponse)
  ))
_sym_db.RegisterMessage(ContentFilterSettingsResponse)

FilterRange = _reflection.GeneratedProtocolMessageType('FilterRange', (_message.Message,), dict(
  DESCRIPTOR = _FILTERRANGE,
  __module__ = 'content_filters_pb2'
  # @@protoc_insertion_point(class_scope:ContentFilters.FilterRange)
  ))
_sym_db.RegisterMessage(FilterRange)

FilterChoice = _reflection.GeneratedProtocolMessageType('FilterChoice', (_message.Message,), dict(
  DESCRIPTOR = _FILTERCHOICE,
  __module__ = 'content_filters_pb2'
  # @@protoc_insertion_point(class_scope:ContentFilters.FilterChoice)
  ))
_sym_db.RegisterMessage(FilterChoice)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n com.google.android.finsky.protosB\016ContentFilters'))
# @@protoc_insertion_point(module_scope)