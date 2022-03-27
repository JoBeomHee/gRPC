# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncalc.proto\x12\x04\x63\x61lc\"$\n\nAddRequest\x12\n\n\x02n1\x18\x01 \x01(\x05\x12\n\n\x02n2\x18\x02 \x01(\x05\"\x16\n\x08\x41\x64\x64Reply\x12\n\n\x02n1\x18\x01 \x01(\x05\"*\n\x10SubstractRequest\x12\n\n\x02n1\x18\x01 \x01(\x05\x12\n\n\x02n2\x18\x02 \x01(\x05\"\x1c\n\x0eSubstractReply\x12\n\n\x02n1\x18\x01 \x01(\x05\")\n\x0fMultiplyRequest\x12\n\n\x02n1\x18\x01 \x01(\x05\x12\n\n\x02n2\x18\x02 \x01(\x05\"\x1b\n\rMeuliplyReply\x12\n\n\x02n1\x18\x01 \x01(\x05\"\'\n\rDivideRequest\x12\n\n\x02n1\x18\x01 \x01(\x05\x12\n\n\x02n2\x18\x02 \x01(\x05\"\x19\n\x0b\x44ivideReply\x12\n\n\x02\x66\x31\x18\x01 \x01(\x02\x32\xe2\x01\n\nCalculator\x12)\n\x03\x41\x64\x64\x12\x10.calc.AddRequest\x1a\x0e.calc.AddReply\"\x00\x12;\n\tSubstract\x12\x16.calc.SubstractRequest\x1a\x14.calc.SubstractReply\"\x00\x12\x38\n\x08Multiply\x12\x15.calc.MultiplyRequest\x1a\x13.calc.MeuliplyReply\"\x00\x12\x32\n\x06\x44ivide\x12\x13.calc.DivideRequest\x1a\x11.calc.DivideReply\"\x00\x62\x06proto3')



_ADDREQUEST = DESCRIPTOR.message_types_by_name['AddRequest']
_ADDREPLY = DESCRIPTOR.message_types_by_name['AddReply']
_SUBSTRACTREQUEST = DESCRIPTOR.message_types_by_name['SubstractRequest']
_SUBSTRACTREPLY = DESCRIPTOR.message_types_by_name['SubstractReply']
_MULTIPLYREQUEST = DESCRIPTOR.message_types_by_name['MultiplyRequest']
_MEULIPLYREPLY = DESCRIPTOR.message_types_by_name['MeuliplyReply']
_DIVIDEREQUEST = DESCRIPTOR.message_types_by_name['DivideRequest']
_DIVIDEREPLY = DESCRIPTOR.message_types_by_name['DivideReply']
AddRequest = _reflection.GeneratedProtocolMessageType('AddRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDREQUEST,
  '__module__' : 'calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.AddRequest)
  })
_sym_db.RegisterMessage(AddRequest)

AddReply = _reflection.GeneratedProtocolMessageType('AddReply', (_message.Message,), {
  'DESCRIPTOR' : _ADDREPLY,
  '__module__' : 'calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.AddReply)
  })
_sym_db.RegisterMessage(AddReply)

SubstractRequest = _reflection.GeneratedProtocolMessageType('SubstractRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSTRACTREQUEST,
  '__module__' : 'calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.SubstractRequest)
  })
_sym_db.RegisterMessage(SubstractRequest)

SubstractReply = _reflection.GeneratedProtocolMessageType('SubstractReply', (_message.Message,), {
  'DESCRIPTOR' : _SUBSTRACTREPLY,
  '__module__' : 'calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.SubstractReply)
  })
_sym_db.RegisterMessage(SubstractReply)

MultiplyRequest = _reflection.GeneratedProtocolMessageType('MultiplyRequest', (_message.Message,), {
  'DESCRIPTOR' : _MULTIPLYREQUEST,
  '__module__' : 'calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.MultiplyRequest)
  })
_sym_db.RegisterMessage(MultiplyRequest)

MeuliplyReply = _reflection.GeneratedProtocolMessageType('MeuliplyReply', (_message.Message,), {
  'DESCRIPTOR' : _MEULIPLYREPLY,
  '__module__' : 'calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.MeuliplyReply)
  })
_sym_db.RegisterMessage(MeuliplyReply)

DivideRequest = _reflection.GeneratedProtocolMessageType('DivideRequest', (_message.Message,), {
  'DESCRIPTOR' : _DIVIDEREQUEST,
  '__module__' : 'calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.DivideRequest)
  })
_sym_db.RegisterMessage(DivideRequest)

DivideReply = _reflection.GeneratedProtocolMessageType('DivideReply', (_message.Message,), {
  'DESCRIPTOR' : _DIVIDEREPLY,
  '__module__' : 'calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.DivideReply)
  })
_sym_db.RegisterMessage(DivideReply)

_CALCULATOR = DESCRIPTOR.services_by_name['Calculator']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDREQUEST._serialized_start=20
  _ADDREQUEST._serialized_end=56
  _ADDREPLY._serialized_start=58
  _ADDREPLY._serialized_end=80
  _SUBSTRACTREQUEST._serialized_start=82
  _SUBSTRACTREQUEST._serialized_end=124
  _SUBSTRACTREPLY._serialized_start=126
  _SUBSTRACTREPLY._serialized_end=154
  _MULTIPLYREQUEST._serialized_start=156
  _MULTIPLYREQUEST._serialized_end=197
  _MEULIPLYREPLY._serialized_start=199
  _MEULIPLYREPLY._serialized_end=226
  _DIVIDEREQUEST._serialized_start=228
  _DIVIDEREQUEST._serialized_end=267
  _DIVIDEREPLY._serialized_start=269
  _DIVIDEREPLY._serialized_end=294
  _CALCULATOR._serialized_start=297
  _CALCULATOR._serialized_end=523
# @@protoc_insertion_point(module_scope)
