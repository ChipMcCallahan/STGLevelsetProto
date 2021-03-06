# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stg_levelset.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stg_levelset.proto',
  package='stg_levelset_proto',
  syntax='proto3',
  serialized_options=b'\252\002\003STG',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12stg_levelset.proto\x12\x12stg_levelset_proto\"U\n\x08Levelset\x12\r\n\x05title\x18\x01 \x01(\t\x12)\n\x06levels\x18\x02 \x03(\x0b\x32\x19.stg_levelset_proto.Level\x12\x0f\n\x07\x61uthors\x18\x03 \x03(\t\"\xce\x01\n\x05Level\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07\x61uthors\x18\x02 \x03(\t\x12\x0e\n\x06size_x\x18\x03 \x01(\x05\x12\x0e\n\x06size_y\x18\x04 \x01(\x05\x12\x0e\n\x06size_z\x18\x05 \x01(\x05\x12/\n\x03map\x18\x08 \x03(\x0b\x32\".stg_levelset_proto.Level.MapEntry\x1a\x44\n\x08MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.stg_levelset_proto.Cell:\x02\x38\x01\"\x9a\x03\n\x04\x43\x65ll\x12,\n\x07terrain\x18\x01 \x01(\x0b\x32\x1b.stg_levelset_proto.Element\x12\x35\n\x10terrain_modifier\x18\x02 \x01(\x0b\x32\x1b.stg_levelset_proto.Element\x12+\n\x06pickup\x18\x03 \x01(\x0b\x32\x1b.stg_levelset_proto.Element\x12(\n\x03mob\x18\x04 \x01(\x0b\x32\x1b.stg_levelset_proto.Element\x12(\n\x03top\x18\x05 \x01(\x0b\x32\x1b.stg_levelset_proto.Element\x12*\n\x05north\x18\x06 \x01(\x0b\x32\x1b.stg_levelset_proto.Element\x12)\n\x04\x65\x61st\x18\x07 \x01(\x0b\x32\x1b.stg_levelset_proto.Element\x12*\n\x05south\x18\x08 \x01(\x0b\x32\x1b.stg_levelset_proto.Element\x12)\n\x04west\x18\t \x01(\x0b\x32\x1b.stg_levelset_proto.Element\"\xfa\x01\n\x07\x45lement\x12&\n\x02id\x18\x01 \x01(\x0e\x32\x1a.stg_levelset_proto.ElemId\x12\x0c\n\x04rule\x18\x02 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x03 \x01(\x05\x12(\n\x05\x63olor\x18\x04 \x01(\x0e\x32\x19.stg_levelset_proto.Color\x12*\n\x03\x64ir\x18\x05 \x01(\x0e\x32\x1d.stg_levelset_proto.Direction\x12\r\n\x05\x63ount\x18\x06 \x01(\x05\x12.\n\tinventory\x18\x07 \x03(\x0b\x32\x1b.stg_levelset_proto.Element\x12\x13\n\x0bstring_args\x18\x08 \x03(\t\"y\n\x05Input\x12.\n\x07primary\x18\x01 \x01(\x0e\x32\x1d.stg_levelset_proto.Direction\x12\x30\n\tsecondary\x18\x02 \x01(\x0e\x32\x1d.stg_levelset_proto.Direction\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\x05*\xe9\x04\n\x06\x45lemId\x12\x14\n\x10\x45LEMID_UNDEFINED\x10\x00\x12\t\n\x05SPACE\x10\x01\x12\t\n\x05\x46LOOR\x10\x02\x12\x08\n\x04WALL\x10\x03\x12\x08\n\x04\x45XIT\x10\x04\x12\t\n\x05WATER\x10\x05\x12\x08\n\x04\x46IRE\x10\x06\x12\x08\n\x04\x44IRT\x10\x07\x12\n\n\x06GRAVEL\x10\x08\x12\x07\n\x03ICE\x10\t\x12\t\n\x05\x46ORCE\x10\n\x12\n\n\x06\x43LONER\x10\x0b\x12\x08\n\x04HINT\x10\x0c\x12\x0e\n\nCHECKPOINT\x10\r\x12\t\n\x05THIEF\x10\x0e\x12\x0c\n\x08TELEPORT\x10\x0f\x12\x08\n\x04TRAP\x10\x10\x12\x08\n\x04\x44OOR\x10\x11\x12\x0f\n\x0bTOGGLE_WALL\x10\x12\x12\x0e\n\nPOPUP_WALL\x10\x13\x12\t\n\x05PANEL\x10\x64\x12\x10\n\x0cTOGGLE_PANEL\x10\x65\x12\x11\n\rONE_WAY_PANEL\x10\x66\x12\x0f\n\x0bPOPUP_PANEL\x10g\x12\n\n\x06\x43ORNER\x10h\x12\x0b\n\x06SOCKET\x10\xc8\x01\x12\x12\n\rTOGGLE_BUTTON\x10\xc9\x01\x12\x13\n\x0eHOLDONE_BUTTON\x10\xca\x01\x12\x13\n\x0eHOLDALL_BUTTON\x10\xcb\x01\x12\x11\n\x0cONEOF_BUTTON\x10\xcc\x01\x12\x10\n\x0b\x41REA_BUTTON\x10\xcd\x01\x12\t\n\x04\x43HIP\x10\xac\x02\x12\t\n\x04\x42OMB\x10\xad\x02\x12\r\n\x08\x46LIPPERS\x10\xae\x02\x12\x0c\n\x07SUCTION\x10\xaf\x02\x12\x0e\n\tFIREBOOTS\x10\xb0\x02\x12\x0b\n\x06SKATES\x10\xb1\x02\x12\x08\n\x03KEY\x10\xb2\x02\x12\x0b\n\x06PLAYER\x10\x90\x03\x12\x0f\n\nDIRT_BLOCK\x10\x91\x03\x12\x0c\n\x07MONSTER\x10\x92\x03\x12\t\n\x04TANK\x10\x93\x03\x12\x11\n\x0cMOB_FOLLOWER\x10\xf3\x03\x12\x0b\n\x06\x43\x41NOPY\x10\xf4\x03*A\n\tGamestate\x12\x17\n\x13GAMESTATE_UNDEFINED\x10\x00\x12\x08\n\x04PLAY\x10\x01\x12\x08\n\x04LOSE\x10\x02\x12\x07\n\x03WIN\x10\x03*t\n\x05\x43olor\x12\x13\n\x0f\x43OLOR_UNDEFINED\x10\x00\x12\x07\n\x03RED\x10\x01\x12\x08\n\x04\x42LUE\x10\x02\x12\t\n\x05GREEN\x10\x03\x12\n\n\x06YELLOW\x10\x04\x12\x08\n\x04\x43YAN\x10\x05\x12\x0b\n\x07MAGENTA\x10\x06\x12\n\n\x06ORANGE\x10\x07\x12\t\n\x05\x42ROWN\x10\x08*l\n\tDirection\x12\x17\n\x13\x44IRECTION_UNDEFINED\x10\x00\x12\x05\n\x01N\x10\x01\x12\x05\n\x01\x45\x10\x02\x12\x05\n\x01S\x10\x03\x12\x05\n\x01W\x10\x04\x12\x06\n\x02NE\x10\x05\x12\x06\n\x02SE\x10\x06\x12\x06\n\x02SW\x10\x07\x12\x06\n\x02NW\x10\x08\x12\n\n\x06RANDOM\x10\tB\x06\xaa\x02\x03STGb\x06proto3'
)

_ELEMID = _descriptor.EnumDescriptor(
  name='ElemId',
  full_name='stg_levelset_proto.ElemId',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ELEMID_UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPACE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLOOR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WALL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXIT', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WATER', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIRE', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIRT', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GRAVEL', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ICE', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FORCE', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLONER', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HINT', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHECKPOINT', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='THIEF', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TELEPORT', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRAP', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOOR', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOGGLE_WALL', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POPUP_WALL', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PANEL', index=20, number=100,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOGGLE_PANEL', index=21, number=101,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ONE_WAY_PANEL', index=22, number=102,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POPUP_PANEL', index=23, number=103,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CORNER', index=24, number=104,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SOCKET', index=25, number=200,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOGGLE_BUTTON', index=26, number=201,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HOLDONE_BUTTON', index=27, number=202,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HOLDALL_BUTTON', index=28, number=203,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ONEOF_BUTTON', index=29, number=204,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AREA_BUTTON', index=30, number=205,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHIP', index=31, number=300,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BOMB', index=32, number=301,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLIPPERS', index=33, number=302,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCTION', index=34, number=303,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIREBOOTS', index=35, number=304,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SKATES', index=36, number=305,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY', index=37, number=306,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLAYER', index=38, number=400,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIRT_BLOCK', index=39, number=401,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MONSTER', index=40, number=402,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TANK', index=41, number=403,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MOB_FOLLOWER', index=42, number=499,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANOPY', index=43, number=500,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1128,
  serialized_end=1745,
)
_sym_db.RegisterEnumDescriptor(_ELEMID)

ElemId = enum_type_wrapper.EnumTypeWrapper(_ELEMID)
_GAMESTATE = _descriptor.EnumDescriptor(
  name='Gamestate',
  full_name='stg_levelset_proto.Gamestate',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GAMESTATE_UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLAY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOSE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WIN', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1747,
  serialized_end=1812,
)
_sym_db.RegisterEnumDescriptor(_GAMESTATE)

Gamestate = enum_type_wrapper.EnumTypeWrapper(_GAMESTATE)
_COLOR = _descriptor.EnumDescriptor(
  name='Color',
  full_name='stg_levelset_proto.Color',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COLOR_UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BLUE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GREEN', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='YELLOW', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CYAN', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MAGENTA', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORANGE', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BROWN', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1814,
  serialized_end=1930,
)
_sym_db.RegisterEnumDescriptor(_COLOR)

Color = enum_type_wrapper.EnumTypeWrapper(_COLOR)
_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='stg_levelset_proto.Direction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIRECTION_UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='N', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='E', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='S', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='W', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SE', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SW', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NW', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RANDOM', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1932,
  serialized_end=2040,
)
_sym_db.RegisterEnumDescriptor(_DIRECTION)

Direction = enum_type_wrapper.EnumTypeWrapper(_DIRECTION)
ELEMID_UNDEFINED = 0
SPACE = 1
FLOOR = 2
WALL = 3
EXIT = 4
WATER = 5
FIRE = 6
DIRT = 7
GRAVEL = 8
ICE = 9
FORCE = 10
CLONER = 11
HINT = 12
CHECKPOINT = 13
THIEF = 14
TELEPORT = 15
TRAP = 16
DOOR = 17
TOGGLE_WALL = 18
POPUP_WALL = 19
PANEL = 100
TOGGLE_PANEL = 101
ONE_WAY_PANEL = 102
POPUP_PANEL = 103
CORNER = 104
SOCKET = 200
TOGGLE_BUTTON = 201
HOLDONE_BUTTON = 202
HOLDALL_BUTTON = 203
ONEOF_BUTTON = 204
AREA_BUTTON = 205
CHIP = 300
BOMB = 301
FLIPPERS = 302
SUCTION = 303
FIREBOOTS = 304
SKATES = 305
KEY = 306
PLAYER = 400
DIRT_BLOCK = 401
MONSTER = 402
TANK = 403
MOB_FOLLOWER = 499
CANOPY = 500
GAMESTATE_UNDEFINED = 0
PLAY = 1
LOSE = 2
WIN = 3
COLOR_UNDEFINED = 0
RED = 1
BLUE = 2
GREEN = 3
YELLOW = 4
CYAN = 5
MAGENTA = 6
ORANGE = 7
BROWN = 8
DIRECTION_UNDEFINED = 0
N = 1
E = 2
S = 3
W = 4
NE = 5
SE = 6
SW = 7
NW = 8
RANDOM = 9



_LEVELSET = _descriptor.Descriptor(
  name='Levelset',
  full_name='stg_levelset_proto.Levelset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='stg_levelset_proto.Levelset.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='levels', full_name='stg_levelset_proto.Levelset.levels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authors', full_name='stg_levelset_proto.Levelset.authors', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=127,
)


_LEVEL_MAPENTRY = _descriptor.Descriptor(
  name='MapEntry',
  full_name='stg_levelset_proto.Level.MapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='stg_levelset_proto.Level.MapEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='stg_levelset_proto.Level.MapEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=268,
  serialized_end=336,
)

_LEVEL = _descriptor.Descriptor(
  name='Level',
  full_name='stg_levelset_proto.Level',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='stg_levelset_proto.Level.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authors', full_name='stg_levelset_proto.Level.authors', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size_x', full_name='stg_levelset_proto.Level.size_x', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size_y', full_name='stg_levelset_proto.Level.size_y', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size_z', full_name='stg_levelset_proto.Level.size_z', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='map', full_name='stg_levelset_proto.Level.map', index=5,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LEVEL_MAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=336,
)


_CELL = _descriptor.Descriptor(
  name='Cell',
  full_name='stg_levelset_proto.Cell',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='terrain', full_name='stg_levelset_proto.Cell.terrain', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='terrain_modifier', full_name='stg_levelset_proto.Cell.terrain_modifier', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pickup', full_name='stg_levelset_proto.Cell.pickup', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mob', full_name='stg_levelset_proto.Cell.mob', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='top', full_name='stg_levelset_proto.Cell.top', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='north', full_name='stg_levelset_proto.Cell.north', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='east', full_name='stg_levelset_proto.Cell.east', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='south', full_name='stg_levelset_proto.Cell.south', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='west', full_name='stg_levelset_proto.Cell.west', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=749,
)


_ELEMENT = _descriptor.Descriptor(
  name='Element',
  full_name='stg_levelset_proto.Element',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='stg_levelset_proto.Element.id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rule', full_name='stg_levelset_proto.Element.rule', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel', full_name='stg_levelset_proto.Element.channel', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color', full_name='stg_levelset_proto.Element.color', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dir', full_name='stg_levelset_proto.Element.dir', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count', full_name='stg_levelset_proto.Element.count', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inventory', full_name='stg_levelset_proto.Element.inventory', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_args', full_name='stg_levelset_proto.Element.string_args', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=752,
  serialized_end=1002,
)


_INPUT = _descriptor.Descriptor(
  name='Input',
  full_name='stg_levelset_proto.Input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='primary', full_name='stg_levelset_proto.Input.primary', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secondary', full_name='stg_levelset_proto.Input.secondary', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='stg_levelset_proto.Input.action', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1004,
  serialized_end=1125,
)

_LEVELSET.fields_by_name['levels'].message_type = _LEVEL
_LEVEL_MAPENTRY.fields_by_name['value'].message_type = _CELL
_LEVEL_MAPENTRY.containing_type = _LEVEL
_LEVEL.fields_by_name['map'].message_type = _LEVEL_MAPENTRY
_CELL.fields_by_name['terrain'].message_type = _ELEMENT
_CELL.fields_by_name['terrain_modifier'].message_type = _ELEMENT
_CELL.fields_by_name['pickup'].message_type = _ELEMENT
_CELL.fields_by_name['mob'].message_type = _ELEMENT
_CELL.fields_by_name['top'].message_type = _ELEMENT
_CELL.fields_by_name['north'].message_type = _ELEMENT
_CELL.fields_by_name['east'].message_type = _ELEMENT
_CELL.fields_by_name['south'].message_type = _ELEMENT
_CELL.fields_by_name['west'].message_type = _ELEMENT
_ELEMENT.fields_by_name['id'].enum_type = _ELEMID
_ELEMENT.fields_by_name['color'].enum_type = _COLOR
_ELEMENT.fields_by_name['dir'].enum_type = _DIRECTION
_ELEMENT.fields_by_name['inventory'].message_type = _ELEMENT
_INPUT.fields_by_name['primary'].enum_type = _DIRECTION
_INPUT.fields_by_name['secondary'].enum_type = _DIRECTION
DESCRIPTOR.message_types_by_name['Levelset'] = _LEVELSET
DESCRIPTOR.message_types_by_name['Level'] = _LEVEL
DESCRIPTOR.message_types_by_name['Cell'] = _CELL
DESCRIPTOR.message_types_by_name['Element'] = _ELEMENT
DESCRIPTOR.message_types_by_name['Input'] = _INPUT
DESCRIPTOR.enum_types_by_name['ElemId'] = _ELEMID
DESCRIPTOR.enum_types_by_name['Gamestate'] = _GAMESTATE
DESCRIPTOR.enum_types_by_name['Color'] = _COLOR
DESCRIPTOR.enum_types_by_name['Direction'] = _DIRECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Levelset = _reflection.GeneratedProtocolMessageType('Levelset', (_message.Message,), {
  'DESCRIPTOR' : _LEVELSET,
  '__module__' : 'stg_levelset_pb2'
  # @@protoc_insertion_point(class_scope:stg_levelset_proto.Levelset)
  })
_sym_db.RegisterMessage(Levelset)

Level = _reflection.GeneratedProtocolMessageType('Level', (_message.Message,), {

  'MapEntry' : _reflection.GeneratedProtocolMessageType('MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _LEVEL_MAPENTRY,
    '__module__' : 'stg_levelset_pb2'
    # @@protoc_insertion_point(class_scope:stg_levelset_proto.Level.MapEntry)
    })
  ,
  'DESCRIPTOR' : _LEVEL,
  '__module__' : 'stg_levelset_pb2'
  # @@protoc_insertion_point(class_scope:stg_levelset_proto.Level)
  })
_sym_db.RegisterMessage(Level)
_sym_db.RegisterMessage(Level.MapEntry)

Cell = _reflection.GeneratedProtocolMessageType('Cell', (_message.Message,), {
  'DESCRIPTOR' : _CELL,
  '__module__' : 'stg_levelset_pb2'
  # @@protoc_insertion_point(class_scope:stg_levelset_proto.Cell)
  })
_sym_db.RegisterMessage(Cell)

Element = _reflection.GeneratedProtocolMessageType('Element', (_message.Message,), {
  'DESCRIPTOR' : _ELEMENT,
  '__module__' : 'stg_levelset_pb2'
  # @@protoc_insertion_point(class_scope:stg_levelset_proto.Element)
  })
_sym_db.RegisterMessage(Element)

Input = _reflection.GeneratedProtocolMessageType('Input', (_message.Message,), {
  'DESCRIPTOR' : _INPUT,
  '__module__' : 'stg_levelset_pb2'
  # @@protoc_insertion_point(class_scope:stg_levelset_proto.Input)
  })
_sym_db.RegisterMessage(Input)


DESCRIPTOR._options = None
_LEVEL_MAPENTRY._options = None
# @@protoc_insertion_point(module_scope)
