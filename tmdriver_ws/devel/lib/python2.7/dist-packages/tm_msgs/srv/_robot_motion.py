# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from tm_msgs/robot_motionRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class robot_motionRequest(genpy.Message):
  _md5sum = "e5d56d3ead9f6aa43a72bdca77e7dce7"
  _type = "tm_msgs/robot_motionRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """string goal_format # 'JPP' or 'CPP' (Joint angle or Cartesian), 'plan' for excute certain plan 
string motion_type # 'PTP' or 'line' , if goal_format is 'plan', motion_type will be the file path of plan 
float64[] goal
float64 velocity_scaling_factor # Set a scaling factor for optionally reducing the maximum joint velocity. Allowed values are in (0,1]
bool constraints
string plan_name # file name of plan
int32 plan_index
bool move_to_plan_first_pose
"""
  __slots__ = ['goal_format','motion_type','goal','velocity_scaling_factor','constraints','plan_name','plan_index','move_to_plan_first_pose']
  _slot_types = ['string','string','float64[]','float64','bool','string','int32','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       goal_format,motion_type,goal,velocity_scaling_factor,constraints,plan_name,plan_index,move_to_plan_first_pose

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(robot_motionRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.goal_format is None:
        self.goal_format = ''
      if self.motion_type is None:
        self.motion_type = ''
      if self.goal is None:
        self.goal = []
      if self.velocity_scaling_factor is None:
        self.velocity_scaling_factor = 0.
      if self.constraints is None:
        self.constraints = False
      if self.plan_name is None:
        self.plan_name = ''
      if self.plan_index is None:
        self.plan_index = 0
      if self.move_to_plan_first_pose is None:
        self.move_to_plan_first_pose = False
    else:
      self.goal_format = ''
      self.motion_type = ''
      self.goal = []
      self.velocity_scaling_factor = 0.
      self.constraints = False
      self.plan_name = ''
      self.plan_index = 0
      self.move_to_plan_first_pose = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.goal_format
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.motion_type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.goal)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.goal))
      _x = self
      buff.write(_get_struct_dB().pack(_x.velocity_scaling_factor, _x.constraints))
      _x = self.plan_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_iB().pack(_x.plan_index, _x.move_to_plan_first_pose))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal_format = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.goal_format = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.motion_type = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.motion_type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.goal = s.unpack(str[start:end])
      _x = self
      start = end
      end += 9
      (_x.velocity_scaling_factor, _x.constraints,) = _get_struct_dB().unpack(str[start:end])
      self.constraints = bool(self.constraints)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.plan_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.plan_name = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.plan_index, _x.move_to_plan_first_pose,) = _get_struct_iB().unpack(str[start:end])
      self.move_to_plan_first_pose = bool(self.move_to_plan_first_pose)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.goal_format
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.motion_type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.goal)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.goal.tostring())
      _x = self
      buff.write(_get_struct_dB().pack(_x.velocity_scaling_factor, _x.constraints))
      _x = self.plan_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_iB().pack(_x.plan_index, _x.move_to_plan_first_pose))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal_format = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.goal_format = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.motion_type = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.motion_type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.goal = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 9
      (_x.velocity_scaling_factor, _x.constraints,) = _get_struct_dB().unpack(str[start:end])
      self.constraints = bool(self.constraints)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.plan_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.plan_name = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.plan_index, _x.move_to_plan_first_pose,) = _get_struct_iB().unpack(str[start:end])
      self.move_to_plan_first_pose = bool(self.move_to_plan_first_pose)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_dB = None
def _get_struct_dB():
    global _struct_dB
    if _struct_dB is None:
        _struct_dB = struct.Struct("<dB")
    return _struct_dB
_struct_iB = None
def _get_struct_iB():
    global _struct_iB
    if _struct_iB is None:
        _struct_iB = struct.Struct("<iB")
    return _struct_iB
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from tm_msgs/robot_motionResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class robot_motionResponse(genpy.Message):
  _md5sum = "6f6da3883749771fac40d6deb24a8c02"
  _type = "tm_msgs/robot_motionResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool ok

"""
  __slots__ = ['ok']
  _slot_types = ['bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ok

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(robot_motionResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.ok is None:
        self.ok = False
    else:
      self.ok = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.ok
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.ok,) = _get_struct_B().unpack(str[start:end])
      self.ok = bool(self.ok)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.ok
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.ok,) = _get_struct_B().unpack(str[start:end])
      self.ok = bool(self.ok)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
class robot_motion(object):
  _type          = 'tm_msgs/robot_motion'
  _md5sum = '8e3073766aab12c61a8c47f8c01da720'
  _request_class  = robot_motionRequest
  _response_class = robot_motionResponse
