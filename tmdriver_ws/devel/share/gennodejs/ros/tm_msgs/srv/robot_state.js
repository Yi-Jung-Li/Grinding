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

class robot_stateRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.state = null;
    }
    else {
      if (initObj.hasOwnProperty('state')) {
        this.state = initObj.state
      }
      else {
        this.state = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type robot_stateRequest
    // Serialize message field [state]
    bufferOffset = _serializer.int8(obj.state, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type robot_stateRequest
    let len;
    let data = new robot_stateRequest(null);
    // Deserialize message field [state]
    data.state = _deserializer.int8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'tm_msgs/robot_stateRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a33bed68685ae53bd39b0a9242210752';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 state
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new robot_stateRequest(null);
    if (msg.state !== undefined) {
      resolved.state = msg.state;
    }
    else {
      resolved.state = 0
    }

    return resolved;
    }
};

class robot_stateResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.joint_state = null;
      this.end_effect = null;
    }
    else {
      if (initObj.hasOwnProperty('joint_state')) {
        this.joint_state = initObj.joint_state
      }
      else {
        this.joint_state = [];
      }
      if (initObj.hasOwnProperty('end_effect')) {
        this.end_effect = initObj.end_effect
      }
      else {
        this.end_effect = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type robot_stateResponse
    // Serialize message field [joint_state]
    bufferOffset = _arraySerializer.float64(obj.joint_state, buffer, bufferOffset, null);
    // Serialize message field [end_effect]
    bufferOffset = _arraySerializer.float64(obj.end_effect, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type robot_stateResponse
    let len;
    let data = new robot_stateResponse(null);
    // Deserialize message field [joint_state]
    data.joint_state = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [end_effect]
    data.end_effect = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.joint_state.length;
    length += 8 * object.end_effect.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'tm_msgs/robot_stateResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4802ef3f32ba280daab2fbfb5f167fd4';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[] joint_state
    float64[] end_effect 
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new robot_stateResponse(null);
    if (msg.joint_state !== undefined) {
      resolved.joint_state = msg.joint_state;
    }
    else {
      resolved.joint_state = []
    }

    if (msg.end_effect !== undefined) {
      resolved.end_effect = msg.end_effect;
    }
    else {
      resolved.end_effect = []
    }

    return resolved;
    }
};

module.exports = {
  Request: robot_stateRequest,
  Response: robot_stateResponse,
  md5sum() { return '8179a08027057ba6ad3ae82542746bab'; },
  datatype() { return 'tm_msgs/robot_state'; }
};
