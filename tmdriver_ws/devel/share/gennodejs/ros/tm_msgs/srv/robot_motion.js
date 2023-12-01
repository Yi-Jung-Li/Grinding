// Auto-generated. Do not edit!

// (in-package tm_msgs.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class robot_motionRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.goal_format = null;
      this.motion_type = null;
      this.goal = null;
      this.velocity_scaling_factor = null;
      this.constraints = null;
      this.plan_name = null;
      this.plan_index = null;
      this.move_to_plan_first_pose = null;
    }
    else {
      if (initObj.hasOwnProperty('goal_format')) {
        this.goal_format = initObj.goal_format
      }
      else {
        this.goal_format = '';
      }
      if (initObj.hasOwnProperty('motion_type')) {
        this.motion_type = initObj.motion_type
      }
      else {
        this.motion_type = '';
      }
      if (initObj.hasOwnProperty('goal')) {
        this.goal = initObj.goal
      }
      else {
        this.goal = [];
      }
      if (initObj.hasOwnProperty('velocity_scaling_factor')) {
        this.velocity_scaling_factor = initObj.velocity_scaling_factor
      }
      else {
        this.velocity_scaling_factor = 0.0;
      }
      if (initObj.hasOwnProperty('constraints')) {
        this.constraints = initObj.constraints
      }
      else {
        this.constraints = false;
      }
      if (initObj.hasOwnProperty('plan_name')) {
        this.plan_name = initObj.plan_name
      }
      else {
        this.plan_name = '';
      }
      if (initObj.hasOwnProperty('plan_index')) {
        this.plan_index = initObj.plan_index
      }
      else {
        this.plan_index = 0;
      }
      if (initObj.hasOwnProperty('move_to_plan_first_pose')) {
        this.move_to_plan_first_pose = initObj.move_to_plan_first_pose
      }
      else {
        this.move_to_plan_first_pose = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type robot_motionRequest
    // Serialize message field [goal_format]
    bufferOffset = _serializer.string(obj.goal_format, buffer, bufferOffset);
    // Serialize message field [motion_type]
    bufferOffset = _serializer.string(obj.motion_type, buffer, bufferOffset);
    // Serialize message field [goal]
    bufferOffset = _arraySerializer.float64(obj.goal, buffer, bufferOffset, null);
    // Serialize message field [velocity_scaling_factor]
    bufferOffset = _serializer.float64(obj.velocity_scaling_factor, buffer, bufferOffset);
    // Serialize message field [constraints]
    bufferOffset = _serializer.bool(obj.constraints, buffer, bufferOffset);
    // Serialize message field [plan_name]
    bufferOffset = _serializer.string(obj.plan_name, buffer, bufferOffset);
    // Serialize message field [plan_index]
    bufferOffset = _serializer.int32(obj.plan_index, buffer, bufferOffset);
    // Serialize message field [move_to_plan_first_pose]
    bufferOffset = _serializer.bool(obj.move_to_plan_first_pose, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type robot_motionRequest
    let len;
    let data = new robot_motionRequest(null);
    // Deserialize message field [goal_format]
    data.goal_format = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [motion_type]
    data.motion_type = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [goal]
    data.goal = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [velocity_scaling_factor]
    data.velocity_scaling_factor = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [constraints]
    data.constraints = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [plan_name]
    data.plan_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [plan_index]
    data.plan_index = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [move_to_plan_first_pose]
    data.move_to_plan_first_pose = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.goal_format.length;
    length += object.motion_type.length;
    length += 8 * object.goal.length;
    length += object.plan_name.length;
    return length + 30;
  }

  static datatype() {
    // Returns string type for a service object
    return 'tm_msgs/robot_motionRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e5d56d3ead9f6aa43a72bdca77e7dce7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string goal_format # 'JPP' or 'CPP' (Joint angle or Cartesian), 'plan' for excute certain plan 
    string motion_type # 'PTP' or 'line' , if goal_format is 'plan', motion_type will be the file path of plan 
    float64[] goal
    float64 velocity_scaling_factor # Set a scaling factor for optionally reducing the maximum joint velocity. Allowed values are in (0,1]
    bool constraints
    string plan_name # file name of plan
    int32 plan_index
    bool move_to_plan_first_pose
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new robot_motionRequest(null);
    if (msg.goal_format !== undefined) {
      resolved.goal_format = msg.goal_format;
    }
    else {
      resolved.goal_format = ''
    }

    if (msg.motion_type !== undefined) {
      resolved.motion_type = msg.motion_type;
    }
    else {
      resolved.motion_type = ''
    }

    if (msg.goal !== undefined) {
      resolved.goal = msg.goal;
    }
    else {
      resolved.goal = []
    }

    if (msg.velocity_scaling_factor !== undefined) {
      resolved.velocity_scaling_factor = msg.velocity_scaling_factor;
    }
    else {
      resolved.velocity_scaling_factor = 0.0
    }

    if (msg.constraints !== undefined) {
      resolved.constraints = msg.constraints;
    }
    else {
      resolved.constraints = false
    }

    if (msg.plan_name !== undefined) {
      resolved.plan_name = msg.plan_name;
    }
    else {
      resolved.plan_name = ''
    }

    if (msg.plan_index !== undefined) {
      resolved.plan_index = msg.plan_index;
    }
    else {
      resolved.plan_index = 0
    }

    if (msg.move_to_plan_first_pose !== undefined) {
      resolved.move_to_plan_first_pose = msg.move_to_plan_first_pose;
    }
    else {
      resolved.move_to_plan_first_pose = false
    }

    return resolved;
    }
};

class robot_motionResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ok = null;
    }
    else {
      if (initObj.hasOwnProperty('ok')) {
        this.ok = initObj.ok
      }
      else {
        this.ok = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type robot_motionResponse
    // Serialize message field [ok]
    bufferOffset = _serializer.bool(obj.ok, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type robot_motionResponse
    let len;
    let data = new robot_motionResponse(null);
    // Deserialize message field [ok]
    data.ok = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'tm_msgs/robot_motionResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6f6da3883749771fac40d6deb24a8c02';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool ok
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new robot_motionResponse(null);
    if (msg.ok !== undefined) {
      resolved.ok = msg.ok;
    }
    else {
      resolved.ok = false
    }

    return resolved;
    }
};

module.exports = {
  Request: robot_motionRequest,
  Response: robot_motionResponse,
  md5sum() { return '8e3073766aab12c61a8c47f8c01da720'; },
  datatype() { return 'tm_msgs/robot_motion'; }
};
