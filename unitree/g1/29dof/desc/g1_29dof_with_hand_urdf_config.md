# Robot Joint Configuration: g1_29dof_with_hand

## Joints

| Index | Name | Type | Parent | Child | Angle Limits | Force Limits |
|---|---|---|---|---|---|---|
| 0 | pelvis_contour_joint | fixed | pelvis | pelvis_contour_link | [] | [] |
| 1 | left_hip_pitch_joint | revolute | pelvis | left_hip_pitch_link | [-2.5307, 2.8798] | [-88.0, 88.0] |
| 2 | left_hip_roll_joint | revolute | left_hip_pitch_link | left_hip_roll_link | [-0.5236, 2.9671] | [-88.0, 88.0] |
| 3 | left_hip_yaw_joint | revolute | left_hip_roll_link | left_hip_yaw_link | [-2.7576, 2.7576] | [-88.0, 88.0] |
| 4 | left_knee_joint | revolute | left_hip_yaw_link | left_knee_link | [-0.087267, 2.8798] | [-139.0, 139.0] |
| 5 | left_ankle_pitch_joint | revolute | left_knee_link | left_ankle_pitch_link | [-0.87267, 0.5236] | [-50.0, 50.0] |
| 6 | left_ankle_roll_joint | revolute | left_ankle_pitch_link | left_ankle_roll_link | [-0.2618, 0.2618] | [-50.0, 50.0] |
| 7 | right_hip_pitch_joint | revolute | pelvis | right_hip_pitch_link | [-2.5307, 2.8798] | [-88.0, 88.0] |
| 8 | right_hip_roll_joint | revolute | right_hip_pitch_link | right_hip_roll_link | [-2.9671, 0.5236] | [-88.0, 88.0] |
| 9 | right_hip_yaw_joint | revolute | right_hip_roll_link | right_hip_yaw_link | [-2.7576, 2.7576] | [-88.0, 88.0] |
| 10 | right_knee_joint | revolute | right_hip_yaw_link | right_knee_link | [-0.087267, 2.8798] | [-139.0, 139.0] |
| 11 | right_ankle_pitch_joint | revolute | right_knee_link | right_ankle_pitch_link | [-0.87267, 0.5236] | [-50.0, 50.0] |
| 12 | right_ankle_roll_joint | revolute | right_ankle_pitch_link | right_ankle_roll_link | [-0.2618, 0.2618] | [-50.0, 50.0] |
| 13 | waist_yaw_joint | revolute | pelvis | waist_yaw_link | [-2.618, 2.618] | [-88.0, 88.0] |
| 14 | waist_roll_joint | revolute | waist_yaw_link | waist_roll_link | [-0.52, 0.52] | [-50.0, 50.0] |
| 15 | waist_pitch_joint | revolute | waist_roll_link | torso_link | [-0.52, 0.52] | [-50.0, 50.0] |
| 16 | logo_joint | fixed | torso_link | logo_link | [] | [] |
| 17 | head_joint | fixed | torso_link | head_link | [] | [] |
| 18 | waist_support_joint | fixed | torso_link | waist_support_link | [] | [] |
| 19 | imu_in_torso_joint | fixed | torso_link | imu_in_torso | [] | [] |
| 20 | imu_in_pelvis_joint | fixed | pelvis | imu_in_pelvis | [] | [] |
| 21 | d435_joint | fixed | torso_link | d435_link | [] | [] |
| 22 | mid360_joint | fixed | torso_link | mid360_link | [] | [] |
| 23 | left_shoulder_pitch_joint | revolute | torso_link | left_shoulder_pitch_link | [-3.0892, 2.6704] | [-25.0, 25.0] |
| 24 | left_shoulder_roll_joint | revolute | left_shoulder_pitch_link | left_shoulder_roll_link | [-1.5882, 2.2515] | [-25.0, 25.0] |
| 25 | left_shoulder_yaw_joint | revolute | left_shoulder_roll_link | left_shoulder_yaw_link | [-2.618, 2.618] | [-25.0, 25.0] |
| 26 | left_elbow_joint | revolute | left_shoulder_yaw_link | left_elbow_link | [-1.0472, 2.0944] | [-25.0, 25.0] |
| 27 | left_wrist_roll_joint | revolute | left_elbow_link | left_wrist_roll_link | [-1.972222054, 1.972222054] | [-25.0, 25.0] |
| 28 | left_wrist_pitch_joint | revolute | left_wrist_roll_link | left_wrist_pitch_link | [-1.614429558, 1.614429558] | [-5.0, 5.0] |
| 29 | left_wrist_yaw_joint | revolute | left_wrist_pitch_link | left_wrist_yaw_link | [-1.614429558, 1.614429558] | [-5.0, 5.0] |
| 30 | left_hand_palm_joint | fixed | left_wrist_yaw_link | left_hand_palm_link | [] | [] |
| 31 | left_hand_thumb_0_joint | revolute | left_hand_palm_link | left_hand_thumb_0_link | [-1.04719755, 1.04719755] | [-2.45, 2.45] |
| 32 | left_hand_thumb_1_joint | revolute | left_hand_thumb_0_link | left_hand_thumb_1_link | [-0.72431163, 1.04719755] | [-1.4, 1.4] |
| 33 | left_hand_thumb_2_joint | revolute | left_hand_thumb_1_link | left_hand_thumb_2_link | [0.0, 1.74532925] | [-1.4, 1.4] |
| 34 | left_hand_middle_0_joint | revolute | left_hand_palm_link | left_hand_middle_0_link | [-1.57079632, 0.0] | [-1.4, 1.4] |
| 35 | left_hand_middle_1_joint | revolute | left_hand_middle_0_link | left_hand_middle_1_link | [-1.74532925, 0.0] | [-1.4, 1.4] |
| 36 | left_hand_index_0_joint | revolute | left_hand_palm_link | left_hand_index_0_link | [-1.57079632, 0.0] | [-1.4, 1.4] |
| 37 | left_hand_index_1_joint | revolute | left_hand_index_0_link | left_hand_index_1_link | [-1.74532925, 0.0] | [-1.4, 1.4] |
| 38 | right_shoulder_pitch_joint | revolute | torso_link | right_shoulder_pitch_link | [-3.0892, 2.6704] | [-25.0, 25.0] |
| 39 | right_shoulder_roll_joint | revolute | right_shoulder_pitch_link | right_shoulder_roll_link | [-2.2515, 1.5882] | [-25.0, 25.0] |
| 40 | right_shoulder_yaw_joint | revolute | right_shoulder_roll_link | right_shoulder_yaw_link | [-2.618, 2.618] | [-25.0, 25.0] |
| 41 | right_elbow_joint | revolute | right_shoulder_yaw_link | right_elbow_link | [-1.0472, 2.0944] | [-25.0, 25.0] |
| 42 | right_wrist_roll_joint | revolute | right_elbow_link | right_wrist_roll_link | [-1.972222054, 1.972222054] | [-25.0, 25.0] |
| 43 | right_wrist_pitch_joint | revolute | right_wrist_roll_link | right_wrist_pitch_link | [-1.614429558, 1.614429558] | [-5.0, 5.0] |
| 44 | right_wrist_yaw_joint | revolute | right_wrist_pitch_link | right_wrist_yaw_link | [-1.614429558, 1.614429558] | [-5.0, 5.0] |
| 45 | right_hand_palm_joint | fixed | right_wrist_yaw_link | right_hand_palm_link | [] | [] |
| 46 | right_hand_thumb_0_joint | revolute | right_hand_palm_link | right_hand_thumb_0_link | [-1.04719755, 1.04719755] | [-2.45, 2.45] |
| 47 | right_hand_thumb_1_joint | revolute | right_hand_thumb_0_link | right_hand_thumb_1_link | [-1.04719755, 0.72431163] | [-1.4, 1.4] |
| 48 | right_hand_thumb_2_joint | revolute | right_hand_thumb_1_link | right_hand_thumb_2_link | [-1.74532925, 0.0] | [-1.4, 1.4] |
| 49 | right_hand_middle_0_joint | revolute | right_hand_palm_link | right_hand_middle_0_link | [0.0, 1.57079632] | [-1.4, 1.4] |
| 50 | right_hand_middle_1_joint | revolute | right_hand_middle_0_link | right_hand_middle_1_link | [0.0, 1.74532925] | [-1.4, 1.4] |
| 51 | right_hand_index_0_joint | revolute | right_hand_palm_link | right_hand_index_0_link | [0.0, 1.57079632] | [-1.4, 1.4] |
| 52 | right_hand_index_1_joint | revolute | right_hand_index_0_link | right_hand_index_1_link | [0.0, 1.74532925] | [-1.4, 1.4] |
