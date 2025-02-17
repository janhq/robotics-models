# Robot Joint Configuration: g1_dual_arm

## Joints

| Index | Name | Type | Parent | Child | Angle Limits | Force Limits |
|---|---|---|---|---|---|---|
| 0 | waist_roll_joint | fixed | waist_yaw_link | waist_roll_link | [-0.52, 0.52] | [-50.0, 50.0] |
| 1 | waist_pitch_joint | fixed | waist_roll_link | torso_link | [-0.52, 0.52] | [-50.0, 50.0] |
| 2 | logo_joint | fixed | torso_link | logo_link | [] | [] |
| 3 | head_joint | fixed | torso_link | head_link | [] | [] |
| 4 | waist_support_joint | fixed | torso_link | waist_support_link | [] | [] |
| 5 | imu_in_torso_joint | fixed | torso_link | imu_in_torso | [] | [] |
| 6 | d435_joint | fixed | torso_link | d435_link | [] | [] |
| 7 | mid360_joint | fixed | torso_link | mid360_link | [] | [] |
| 8 | left_shoulder_pitch_joint | revolute | torso_link | left_shoulder_pitch_link | [-3.0892, 2.6704] | [-25.0, 25.0] |
| 9 | left_shoulder_roll_joint | revolute | left_shoulder_pitch_link | left_shoulder_roll_link | [-1.5882, 2.2515] | [-25.0, 25.0] |
| 10 | left_shoulder_yaw_joint | revolute | left_shoulder_roll_link | left_shoulder_yaw_link | [-2.618, 2.618] | [-25.0, 25.0] |
| 11 | left_elbow_joint | revolute | left_shoulder_yaw_link | left_elbow_link | [-1.0472, 2.0944] | [-25.0, 25.0] |
| 12 | left_wrist_roll_joint | revolute | left_elbow_link | left_wrist_roll_link | [-1.972222054, 1.972222054] | [-25.0, 25.0] |
| 13 | left_wrist_pitch_joint | revolute | left_wrist_roll_link | left_wrist_pitch_link | [-1.614429558, 1.614429558] | [-5.0, 5.0] |
| 14 | left_wrist_yaw_joint | revolute | left_wrist_pitch_link | left_wrist_yaw_link | [-1.614429558, 1.614429558] | [-5.0, 5.0] |
| 15 | left_hand_palm_joint | fixed | left_wrist_yaw_link | left_rubber_hand | [] | [] |
| 16 | right_shoulder_pitch_joint | revolute | torso_link | right_shoulder_pitch_link | [-3.0892, 2.6704] | [-25.0, 25.0] |
| 17 | right_shoulder_roll_joint | revolute | right_shoulder_pitch_link | right_shoulder_roll_link | [-2.2515, 1.5882] | [-25.0, 25.0] |
| 18 | right_shoulder_yaw_joint | revolute | right_shoulder_roll_link | right_shoulder_yaw_link | [-2.618, 2.618] | [-25.0, 25.0] |
| 19 | right_elbow_joint | revolute | right_shoulder_yaw_link | right_elbow_link | [-1.0472, 2.0944] | [-25.0, 25.0] |
| 20 | right_wrist_roll_joint | revolute | right_elbow_link | right_wrist_roll_link | [-1.972222054, 1.972222054] | [-25.0, 25.0] |
| 21 | right_wrist_pitch_joint | revolute | right_wrist_roll_link | right_wrist_pitch_link | [-1.614429558, 1.614429558] | [-5.0, 5.0] |
| 22 | right_wrist_yaw_joint | revolute | right_wrist_pitch_link | right_wrist_yaw_link | [-1.614429558, 1.614429558] | [-5.0, 5.0] |
| 23 | right_hand_palm_joint | fixed | right_wrist_yaw_link | right_rubber_hand | [] | [] |
