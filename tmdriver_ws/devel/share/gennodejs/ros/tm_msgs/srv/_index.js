
"use strict";

let SendScript = require('./SendScript.js')
let AskItem = require('./AskItem.js')
let SetIO = require('./SetIO.js')
let Ask_img = require('./Ask_img.js')
let robot_state = require('./robot_state.js')
let AskSta = require('./AskSta.js')
let robot_motion = require('./robot_motion.js')
let defect_detect = require('./defect_detect.js')
let SetPositions = require('./SetPositions.js')
let WriteItem = require('./WriteItem.js')
let ConnectTM = require('./ConnectTM.js')
let SetEvent = require('./SetEvent.js')
let Ask_img_AD = require('./Ask_img_AD.js')

module.exports = {
  SendScript: SendScript,
  AskItem: AskItem,
  SetIO: SetIO,
  Ask_img: Ask_img,
  robot_state: robot_state,
  AskSta: AskSta,
  robot_motion: robot_motion,
  defect_detect: defect_detect,
  SetPositions: SetPositions,
  WriteItem: WriteItem,
  ConnectTM: ConnectTM,
  SetEvent: SetEvent,
  Ask_img_AD: Ask_img_AD,
};
