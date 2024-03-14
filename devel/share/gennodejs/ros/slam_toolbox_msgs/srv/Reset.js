// Auto-generated. Do not edit!

// (in-package slam_toolbox_msgs.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class ResetRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.pause_new_measurements = null;
    }
    else {
      if (initObj.hasOwnProperty('pause_new_measurements')) {
        this.pause_new_measurements = initObj.pause_new_measurements
      }
      else {
        this.pause_new_measurements = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ResetRequest
    // Serialize message field [pause_new_measurements]
    bufferOffset = _serializer.bool(obj.pause_new_measurements, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ResetRequest
    let len;
    let data = new ResetRequest(null);
    // Deserialize message field [pause_new_measurements]
    data.pause_new_measurements = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'slam_toolbox_msgs/ResetRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b8fd9baf49824dc9215dabe1b6b58b4a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Set this to 'true' to pause new measurements immediately after reset.
    # Note: This is a set behaviour and not a toggle behaviour, contrary to Pause.srv service.
    bool pause_new_measurements
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ResetRequest(null);
    if (msg.pause_new_measurements !== undefined) {
      resolved.pause_new_measurements = msg.pause_new_measurements;
    }
    else {
      resolved.pause_new_measurements = false
    }

    return resolved;
    }
};

class ResetResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.result = null;
    }
    else {
      if (initObj.hasOwnProperty('result')) {
        this.result = initObj.result
      }
      else {
        this.result = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ResetResponse
    // Serialize message field [result]
    bufferOffset = _serializer.uint8(obj.result, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ResetResponse
    let len;
    let data = new ResetResponse(null);
    // Deserialize message field [result]
    data.result = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'slam_toolbox_msgs/ResetResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '077d96dcedff8bde88bb113787d3fb93';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Result code defintions
    uint8 RESULT_SUCCESS=0
    
    uint8 result
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ResetResponse(null);
    if (msg.result !== undefined) {
      resolved.result = msg.result;
    }
    else {
      resolved.result = 0
    }

    return resolved;
    }
};

// Constants for message
ResetResponse.Constants = {
  RESULT_SUCCESS: 0,
}

module.exports = {
  Request: ResetRequest,
  Response: ResetResponse,
  md5sum() { return 'd183d6d1f6b03b1483ab508f22fac253'; },
  datatype() { return 'slam_toolbox_msgs/Reset'; }
};
