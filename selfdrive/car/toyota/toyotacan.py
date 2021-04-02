def create_steer_command(packer, steer, steer_req, raw_cnt):
  """Creates a CAN message for the Toyota Steer Command."""

  values = {
    "STEER_REQUEST": steer_req,
    "STEER_TORQUE_CMD": steer,
    "COUNTER": raw_cnt,
    "SET_ME_1": 1,
  }
  return packer.make_can_msg("STEERING_LKA", 0, values)


def create_lta_steer_command(packer, steer, steer_req, raw_cnt):
  """Creates a CAN message for the Toyota LTA Steer Command."""

  values = {
    "COUNTER": raw_cnt + 128,
    "SETME_X1": 1,
    "SETME_X3": 3,
    "PERCENTAGE": 100,
    "SETME_X64": 0x64,
    "ANGLE": 0,
    "STEER_ANGLE_CMD": steer,
    "STEER_REQUEST": steer_req,
    "STEER_REQUEST_2": steer_req,
    "BIT": 0,
  }
  return packer.make_can_msg("STEERING_LTA", 0, values)


def create_accel_command(packer, accel, pcm_cancel, standstill_req, lead, acc_type):
  # TODO: find the exact canceling bit that does not create a chime
  values = {
    "ACCEL_CMD": accel,
    "ACC_TYPE": acc_type,
    "DISTANCE": 0,
    "MINI_CAR": lead,
    "PERMIT_BRAKING": 1,
    "RELEASE_STANDSTILL": not standstill_req,
    "CANCEL_REQ": pcm_cancel,
    "ALLOW_LONG_PRESS": 1,
  }
  return packer.make_can_msg("ACC_CONTROL", 0, values)


def create_acc_cancel_command(packer):
  values = {
    "GAS_RELEASED": 0,
    "CRUISE_ACTIVE": 0,
    "STANDSTILL_ON": 0,
    "ACCEL_NET": 0,
    "CRUISE_STATE": 0,
    "CANCEL_REQ": 1,
  }
  return packer.make_can_msg("PCM_CRUISE", 0, values)


def create_fcw_command(packer, fcw):
  values = {
    "PCS_INDICATOR": 1,
    "FCW": fcw,
    "SET_ME_X20": 0x20,
    "SET_ME_X10": 0x10,
    "PCS_OFF": 1,
    "PCS_SENSITIVITY": 0,
  }
  return packer.make_can_msg("ACC_HUD", 0, values)


def create_ui_command(packer, steer, chime, left_line, right_line, left_lane_depart, right_lane_depart, enabled):
  values = {
    "TWO_BEEPS": chime,
    "LDA_ALERT": steer,
    "RIGHT_LINE": 3 if right_lane_depart else 2 if enabled else 1 if right_line else 0,
    "LEFT_LINE": 3 if left_lane_depart else 2 if enabled else 1 if left_line else 0,
    "BARRIERS" : 0 if enabled else 1,

    # static signals
    "SET_ME_X02": 2,
    "SET_ME_X01": 1,
    "LKAS_STATUS": 1,
    "REPEATED_BEEPS": 0,
    "LANE_SWAY_FLD": 7,
    "LANE_SWAY_BUZZER": 0,
    "LANE_SWAY_WARNING": 0,
    "LDA_FRONT_CAMERA_BLOCKED": 0,
    "TAKE_CONTROL": 0,
    "LANE_SWAY_SENSITIVITY": 2,
    "LANE_SWAY_TOGGLE": 1,
    "LDA_ON_MESSAGE": 0,
    "LDA_SPEED_TOO_LOW": 0,
    "LDA_SA_TOGGLE": 1,
    "LDA_SENSITIVITY": 2,
    "LDA_UNAVAILABLE": 0,
    "LDA_MALFUNCTION": 0,
    "LDA_UNAVAILABLE_QUIET": 0,
    "ADJUSTING_CAMERA": 0,
    "LDW_EXIST": 1,
  }
  return packer.make_can_msg("LKAS_HUD", 0, values)

def create_ui_command_off(packer):
  return create_ui_command_off_new(packer)

def create_ui_command_off_new(packer):
  # new one? trying to?
  values = {
    "TWO_BEEPS": 0,
    "LDA_ALERT": 0,
    "RIGHT_LINE": 0,
    "LEFT_LINE": 0,
    "BARRIERS" : 0,

    # static signals
    "SET_ME_X02": 2,
    "SET_ME_X01": 0,
    "LKAS_STATUS": 0,
    "REPEATED_BEEPS": 0,
    "LANE_SWAY_FLD": 7,
    "LANE_SWAY_BUZZER": 0,
    "LANE_SWAY_WARNING": 0,
    "LDA_FRONT_CAMERA_BLOCKED": 0,
    "TAKE_CONTROL": 0,
    "LANE_SWAY_SENSITIVITY": 2,
    "LANE_SWAY_TOGGLE": 1,
    "LDA_ON_MESSAGE": 0,
    "LDA_SPEED_TOO_LOW": 0,
    "LDA_SA_TOGGLE": 0,
    "LDA_SENSITIVITY": 2,
    "LDA_UNAVAILABLE": 0,
    "LDA_MALFUNCTION": 0,
    "LDA_UNAVAILABLE_QUIET": 0,
    "ADJUSTING_CAMERA": 0,
    "LDW_EXIST": 0,
  }
  return packer.make_can_msg("LKAS_HUD", 0, values)
  pass

def create_ui_command_off_spektor(packer):
  # spektor's original ui command off
  values = {
    "RIGHT_LINE": 0,
    "LEFT_LINE": 0,
    "BARRIERS" : 0,
    "SET_ME_X0C": 0x0a,
    "SET_ME_X2C": 0x34,
    "SET_ME_X38": 0x00,
    "SET_ME_X02": 0x12,
    "SET_ME_X01": 0,
    "SET_ME_X01_2": 1,
    "REPEATED_BEEPS": 0,
    "TWO_BEEPS": 0,
    "LDA_ALERT": 0,
  }
  return packer.make_can_msg("LKAS_HUD", 0, values)
