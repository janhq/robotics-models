# Robot Joint Configuration: g1_29dof_with_hand

## Joints

| Index | Name | Type | Parent | Child | Angle Limits | Force Limits |
|---|---|---|---|---|---|---|
| 0 | floating_base_joint | free | N/A | N/A | [] | [] |
| 1 | left_hip_pitch_joint | hinge | N/A | N/A | [-2.5307, 2.8798] | [-88.0, 88.0] |
| 2 | left_hip_roll_joint | hinge | N/A | N/A | [-0.5236, 2.9671] | [-88.0, 88.0] |
| 3 | left_hip_yaw_joint | hinge | N/A | N/A | [-2.7576, 2.7576] | [-88.0, 88.0] |
| 4 | left_knee_joint | hinge | N/A | N/A | [-0.087267, 2.8798] | [-139.0, 139.0] |
| 5 | left_ankle_pitch_joint | hinge | N/A | N/A | [-0.87267, 0.5236] | [-50.0, 50.0] |
| 6 | left_ankle_roll_joint | hinge | N/A | N/A | [-0.2618, 0.2618] | [-50.0, 50.0] |
| 7 | right_hip_pitch_joint | hinge | N/A | N/A | [-2.5307, 2.8798] | [-88.0, 88.0] |
| 8 | right_hip_roll_joint | hinge | N/A | N/A | [-2.9671, 0.5236] | [-88.0, 88.0] |
| 9 | right_hip_yaw_joint | hinge | N/A | N/A | [-2.7576, 2.7576] | [-88.0, 88.0] |
| 10 | right_knee_joint | hinge | N/A | N/A | [-0.087267, 2.8798] | [-139.0, 139.0] |
| 11 | right_ankle_pitch_joint | hinge | N/A | N/A | [-0.87267, 0.5236] | [-50.0, 50.0] |
| 12 | right_ankle_roll_joint | hinge | N/A | N/A | [-0.2618, 0.2618] | [-50.0, 50.0] |
| 13 | waist_yaw_joint | hinge | N/A | N/A | [-2.618, 2.618] | [-88.0, 88.0] |
| 14 | waist_roll_joint | hinge | N/A | N/A | [-0.52, 0.52] | [-50.0, 50.0] |
| 15 | waist_pitch_joint | hinge | N/A | N/A | [-0.52, 0.52] | [-50.0, 50.0] |
| 16 | left_shoulder_pitch_joint | hinge | N/A | N/A | [-3.0892, 2.6704] | [-25.0, 25.0] |
| 17 | left_shoulder_roll_joint | hinge | N/A | N/A | [-1.5882, 2.2515] | [-25.0, 25.0] |
| 18 | left_shoulder_yaw_joint | hinge | N/A | N/A | [-2.618, 2.618] | [-25.0, 25.0] |
| 19 | left_elbow_joint | hinge | N/A | N/A | [-1.0472, 2.0944] | [-25.0, 25.0] |
| 20 | left_wrist_roll_joint | hinge | N/A | N/A | [-1.97222, 1.97222] | [-25.0, 25.0] |
| 21 | left_wrist_pitch_joint | hinge | N/A | N/A | [-1.61443, 1.61443] | [-5.0, 5.0] |
| 22 | left_wrist_yaw_joint | hinge | N/A | N/A | [-1.61443, 1.61443] | [-5.0, 5.0] |
| 23 | left_hand_thumb_0_joint | hinge | N/A | N/A | [-1.0472, 1.0472] | [-2.45, 2.45] |
| 24 | left_hand_thumb_1_joint | hinge | N/A | N/A | [-0.724312, 1.0472] | [-1.4, 1.4] |
| 25 | left_hand_thumb_2_joint | hinge | N/A | N/A | [0.0, 1.74533] | [-1.4, 1.4] |
| 26 | left_hand_middle_0_joint | hinge | N/A | N/A | [-1.5708, 0.0] | [-1.4, 1.4] |
| 27 | left_hand_middle_1_joint | hinge | N/A | N/A | [-1.74533, 0.0] | [-1.4, 1.4] |
| 28 | left_hand_index_0_joint | hinge | N/A | N/A | [-1.5708, 0.0] | [-1.4, 1.4] |
| 29 | left_hand_index_1_joint | hinge | N/A | N/A | [-1.74533, 0.0] | [-1.4, 1.4] |
| 30 | right_shoulder_pitch_joint | hinge | N/A | N/A | [-3.0892, 2.6704] | [-25.0, 25.0] |
| 31 | right_shoulder_roll_joint | hinge | N/A | N/A | [-2.2515, 1.5882] | [-25.0, 25.0] |
| 32 | right_shoulder_yaw_joint | hinge | N/A | N/A | [-2.618, 2.618] | [-25.0, 25.0] |
| 33 | right_elbow_joint | hinge | N/A | N/A | [-1.0472, 2.0944] | [-25.0, 25.0] |
| 34 | right_wrist_roll_joint | hinge | N/A | N/A | [-1.97222, 1.97222] | [-25.0, 25.0] |
| 35 | right_wrist_pitch_joint | hinge | N/A | N/A | [-1.61443, 1.61443] | [-5.0, 5.0] |
| 36 | right_wrist_yaw_joint | hinge | N/A | N/A | [-1.61443, 1.61443] | [-5.0, 5.0] |
| 37 | right_hand_thumb_0_joint | hinge | N/A | N/A | [-1.0472, 1.0472] | [-2.45, 2.45] |
| 38 | right_hand_thumb_1_joint | hinge | N/A | N/A | [-1.0472, 0.724312] | [-1.4, 1.4] |
| 39 | right_hand_thumb_2_joint | hinge | N/A | N/A | [-1.74533, 0.0] | [-1.4, 1.4] |
| 40 | right_hand_middle_0_joint | hinge | N/A | N/A | [0.0, 1.5708] | [-1.4, 1.4] |
| 41 | right_hand_middle_1_joint | hinge | N/A | N/A | [0.0, 1.74533] | [-1.4, 1.4] |
| 42 | right_hand_index_0_joint | hinge | N/A | N/A | [0.0, 1.5708] | [-1.4, 1.4] |
| 43 | right_hand_index_1_joint | hinge | N/A | N/A | [0.0, 1.74533] | [-1.4, 1.4] |
