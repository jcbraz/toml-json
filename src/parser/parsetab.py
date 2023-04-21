
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOLEAN COMMA COMMENT DATE DOT EQUAL FLOAT INTEGER KEY LBRACKET LCURLY NEWLINE RBRACKET RCURLY STRING\n    document : items\n    \n    items : item items\n          | item\n    \n    item : KEY EQUAL value NEWLINE\n         | KEY EQUAL value\n         | KEY LBRACKET RBRACKET NEWLINE\n         | KEY LBRACKET RBRACKET\n         | NEWLINE\n    \n    value : STRING\n          | INTEGER\n          | FLOAT\n          | BOOLEAN\n          | DATE\n          | array\n          | inline_table\n    \n    array : LBRACKET values RBRACKET\n    \n    values : value COMMA values\n           | value\n    \n    inline_table : LCURLY pairs RCURLY\n    \n    pairs : KEY EQUAL value COMMA pairs\n          | KEY EQUAL value\n    '
    
_lr_action_items = {'KEY':([0,3,5,9,10,11,12,13,14,15,16,18,19,20,25,26,28,32,],[4,4,-8,-5,-9,-10,-11,-12,-13,-14,-15,24,-7,-4,-6,-16,-19,24,]),'NEWLINE':([0,3,5,9,10,11,12,13,14,15,16,19,20,25,26,28,],[5,5,-8,20,-9,-10,-11,-12,-13,-14,-15,25,-4,-6,-16,-19,]),'$end':([1,2,3,5,6,9,10,11,12,13,14,15,16,19,20,25,26,28,],[0,-1,-3,-8,-2,-5,-9,-10,-11,-12,-13,-14,-15,-7,-4,-6,-16,-19,]),'EQUAL':([4,24,],[7,29,]),'LBRACKET':([4,7,17,27,29,],[8,17,17,17,17,]),'STRING':([7,17,27,29,],[10,10,10,10,]),'INTEGER':([7,17,27,29,],[11,11,11,11,]),'FLOAT':([7,17,27,29,],[12,12,12,12,]),'BOOLEAN':([7,17,27,29,],[13,13,13,13,]),'DATE':([7,17,27,29,],[14,14,14,14,]),'LCURLY':([7,17,27,29,],[18,18,18,18,]),'RBRACKET':([8,10,11,12,13,14,15,16,21,22,26,28,30,],[19,-9,-10,-11,-12,-13,-14,-15,26,-18,-16,-19,-17,]),'COMMA':([10,11,12,13,14,15,16,22,26,28,31,],[-9,-10,-11,-12,-13,-14,-15,27,-16,-19,32,]),'RCURLY':([10,11,12,13,14,15,16,23,26,28,31,33,],[-9,-10,-11,-12,-13,-14,-15,28,-16,-19,-21,-20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'document':([0,],[1,]),'items':([0,3,],[2,6,]),'item':([0,3,],[3,3,]),'value':([7,17,27,29,],[9,22,22,31,]),'array':([7,17,27,29,],[15,15,15,15,]),'inline_table':([7,17,27,29,],[16,16,16,16,]),'values':([17,27,],[21,30,]),'pairs':([18,32,],[23,33,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> document","S'",1,None,None,None),
  ('document -> items','document',1,'p_document','_parser.py',16),
  ('items -> item items','items',2,'p_items','_parser.py',22),
  ('items -> item','items',1,'p_items','_parser.py',23),
  ('item -> KEY EQUAL value NEWLINE','item',4,'p_item','_parser.py',32),
  ('item -> KEY EQUAL value','item',3,'p_item','_parser.py',33),
  ('item -> KEY LBRACKET RBRACKET NEWLINE','item',4,'p_item','_parser.py',34),
  ('item -> KEY LBRACKET RBRACKET','item',3,'p_item','_parser.py',35),
  ('item -> NEWLINE','item',1,'p_item','_parser.py',36),
  ('value -> STRING','value',1,'p_value','_parser.py',47),
  ('value -> INTEGER','value',1,'p_value','_parser.py',48),
  ('value -> FLOAT','value',1,'p_value','_parser.py',49),
  ('value -> BOOLEAN','value',1,'p_value','_parser.py',50),
  ('value -> DATE','value',1,'p_value','_parser.py',51),
  ('value -> array','value',1,'p_value','_parser.py',52),
  ('value -> inline_table','value',1,'p_value','_parser.py',53),
  ('array -> LBRACKET values RBRACKET','array',3,'p_array','_parser.py',59),
  ('values -> value COMMA values','values',3,'p_values','_parser.py',65),
  ('values -> value','values',1,'p_values','_parser.py',66),
  ('inline_table -> LCURLY pairs RCURLY','inline_table',3,'p_inline_table','_parser.py',75),
  ('pairs -> KEY EQUAL value COMMA pairs','pairs',5,'p_pairs','_parser.py',81),
  ('pairs -> KEY EQUAL value','pairs',3,'p_pairs','_parser.py',82),
]
