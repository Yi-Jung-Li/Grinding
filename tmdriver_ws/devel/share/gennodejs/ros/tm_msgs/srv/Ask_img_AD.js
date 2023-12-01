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

class Ask_img_ADRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.file_path = null;
    }
    else {
      if (initObj.hasOwnProperty('file_path')) {
        this.file_path = initObj.file_path
      }
      else {
        this.file_path = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Ask_img_ADRequest
    // Serialize message field [file_path]
    bufferOffset = _serializer.string(obj.file_path, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Ask_img_ADRequest
    let len;
    let data = new Ask_img_ADRequest(null);
    // Deserialize message field [file_path]
    data.file_path = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.file_path.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'tm_msgs/Ask_img_ADRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a1f82596372c52a517e1fe32d1e998e8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string file_path
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Ask_img_ADRequest(null);
    if (msg.file_path !== undefined) {
      resolved.file_path = msg.file_path;
    }
    else {
      resolved.file_path = ''
    }

    return resolved;
    }
};

class Ask_img_ADResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.anomaly_score = null;
    }
    else {
      if (initObj.hasOwnProperty('anomaly_score')) {
        this.anomaly_score = initObj.anomaly_score
      }
      else {
        this.anomaly_score = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Ask_img_ADResponse
    // Serialize message field [anomaly_score]
    bufferOffset = _arraySerializer.float64(obj.anomaly_score, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Ask_img_ADResponse
    let len;
    let data = new Ask_img_ADResponse(null);
    // Deserialize message field [anomaly_score]
    data.anomaly_score = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.anomaly_score.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'tm_msgs/Ask_img_ADResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '96f23771245c7ee86e43cfe9e20d6900';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[] anomaly_score 
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Ask_img_ADResponse(null);
    if (msg.anomaly_score !== undefined) {
      resolved.anomaly_score = msg.anomaly_score;
    }
    else {
      resolved.anomaly_score = []
    }

    return resolved;
    }
};

module.exports = {
  Request: Ask_img_ADRequest,
  Response: Ask_img_ADResponse,
  md5sum() { return '718c3a88dd0f5e8414a94bc17ba46265'; },
  datatype() { return 'tm_msgs/Ask_img_AD'; }
};
