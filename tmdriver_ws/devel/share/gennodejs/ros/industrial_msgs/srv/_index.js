
"use strict";

let StopMotion = require('./StopMotion.js')
let GetRobotInfo = require('./GetRobotInfo.js')
let SetRemoteLoggerLevel = require('./SetRemoteLoggerLevel.js')
let StartMotion = require('./StartMotion.js')
let CmdJointTrajectory = require('./CmdJointTrajectory.js')
let SetDrivePower = require('./SetDrivePower.js')

module.exports = {
  StopMotion: StopMotion,
  GetRobotInfo: GetRobotInfo,
  SetRemoteLoggerLevel: SetRemoteLoggerLevel,
  StartMotion: StartMotion,
  CmdJointTrajectory: CmdJointTrajectory,
  SetDrivePower: SetDrivePower,
};
