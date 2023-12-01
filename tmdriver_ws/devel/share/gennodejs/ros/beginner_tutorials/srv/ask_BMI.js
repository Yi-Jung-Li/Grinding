// Auto-generated. Do not edit!

// (in-package beginner_tutorials.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class ask_BMIRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.height = null;
      this.weight = null;
    }
    else {
      if (initObj.hasOwnProperty('height')) {
        this.height = initObj.height
      }
      else {
        this.height = 0.0;
      }
      if (initObj.hasOwnProperty('weight')) {
        this.weight = initObj.weight
      }
      else {
        this.weight = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ask_BMIRequest
    // Serialize message field [height]
    bufferOffset = _serializer.float32(obj.height, buffer, bufferOffset);
    // Serialize message field [weight]
    bufferOffset = _serializer.float32(obj.weight, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ask_BMIRequest
    let len;
    let data = new ask_BMIRequest(null);
    // Deserialize message field [height]
    data.height = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [weight]
    data.weight = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'beginner_tutorials/ask_BMIRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c714d1effcb9d7045df53d374d18e3d7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 height
    float32 weight
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ask_BMIRequest(null);
    if (msg.height !== undefined) {
      resolved.height = msg.height;
    }
    else {
      resolved.height = 0.0
    }

    if (msg.weight !== undefined) {
      resolved.weight = msg.weight;
    }
    else {
      resolved.weight = 0.0
    }

    return resolved;
    }
};

class ask_BMIResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.BMI = null;
    }
    else {
      if (initObj.hasOwnProperty('BMI')) {
        this.BMI = initObj.BMI
      }
      else {
        this.BMI = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ask_BMIResponse
    // Serialize message field [BMI]
    bufferOffset = _serializer.float32(obj.BMI, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ask_BMIResponse
    let len;
    let data = new ask_BMIResponse(null);
    // Deserialize message field [BMI]
    data.BMI = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'beginner_tutorials/ask_BMIResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd24e9092ad345fe90a3db3d59e270dc5';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 BMI
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ask_BMIResponse(null);
    if (msg.BMI !== undefined) {
      resolved.BMI = msg.BMI;
    }
    else {
      resolved.BMI = 0.0
    }

    return resolved;
    }
};

module.exports = {
  Request: ask_BMIRequest,
  Response: ask_BMIResponse,
  md5sum() { return '3de0e12df6c14255537cca18d991ce8d'; },
  datatype() { return 'beginner_tutorials/ask_BMI'; }
};
