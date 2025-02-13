# Robot Joint Configuration: g1_23dof_rev_1_0

## Joints

| Index | Name | Type | Parent | Child | Angle Limits | Force Limits |
|---|---|---|---|---|---|---|
| 0 | pelvis_contour_joint | fixed | pelvis | pelvis_contour_link | N/A | N/A |
| 1 | left_hip_pitch_joint | revolute | pelvis | left_hip_pitch_link | -2.5307 to 2.8798 | -88.0 to 88.0 |
| 2 | left_hip_roll_joint | revolute | left_hip_pitch_link | left_hip_roll_link | -0.5236 to 2.9671 | -139.0 to 139.0 |
| 3 | left_hip_yaw_joint | revolute | left_hip_roll_link | left_hip_yaw_link | -2.7576 to 2.7576 | -88.0 to 88.0 |
| 4 | left_knee_joint | revolute | left_hip_yaw_link | left_knee_link | -0.087267 to 2.8798 | -139.0 to 139.0 |
| 5 | left_ankle_pitch_joint | revolute | left_knee_link | left_ankle_pitch_link | -0.87267 to 0.5236 | -50.0 to 50.0 |
| 6 | left_ankle_roll_joint | revolute | left_ankle_pitch_link | left_ankle_roll_link | -0.2618 to 0.2618 | -50.0 to 50.0 |
| 7 | right_hip_pitch_joint | revolute | pelvis | right_hip_pitch_link | -2.5307 to 2.8798 | -88.0 to 88.0 |
| 8 | right_hip_roll_joint | revolute | right_hip_pitch_link | right_hip_roll_link | -2.9671 to 0.5236 | -139.0 to 139.0 |
| 9 | right_hip_yaw_joint | revolute | right_hip_roll_link | right_hip_yaw_link | -2.7576 to 2.7576 | -88.0 to 88.0 |
| 10 | right_knee_joint | revolute | right_hip_yaw_link | right_knee_link | -0.087267 to 2.8798 | -139.0 to 139.0 |
| 11 | right_ankle_pitch_joint | revolute | right_knee_link | right_ankle_pitch_link | -0.87267 to 0.5236 | -50.0 to 50.0 |
| 12 | right_ankle_roll_joint | revolute | right_ankle_pitch_link | right_ankle_roll_link | -0.2618 to 0.2618 | -50.0 to 50.0 |
| 13 | waist_yaw_joint | revolute | pelvis | torso_link | -2.618 to 2.618 | -88.0 to 88.0 |
| 14 | logo_joint | fixed | torso_link | logo_link | N/A | N/A |
| 15 | head_joint | fixed | torso_link | head_link | N/A | N/A |
| 16 | imu_in_torso_joint | fixed | torso_link | imu_in_torso | N/A | N/A |
| 17 | imu_in_pelvis_joint | fixed | pelvis | imu_in_pelvis | N/A | N/A |
| 18 | d435_joint | fixed | torso_link | d435_link | N/A | N/A |
| 19 | mid360_joint | fixed | torso_link | mid360_link | N/A | N/A |
| 20 | left_shoulder_pitch_joint | revolute | torso_link | left_shoulder_pitch_link | -3.0892 to 2.6704 | -25.0 to 25.0 |
| 21 | left_shoulder_roll_joint | revolute | left_shoulder_pitch_link | left_shoulder_roll_link | -1.5882 to 2.2515 | -25.0 to 25.0 |
| 22 | left_shoulder_yaw_joint | revolute | left_shoulder_roll_link | left_shoulder_yaw_link | -2.618 to 2.618 | -25.0 to 25.0 |
| 23 | left_elbow_joint | revolute | left_shoulder_yaw_link | left_elbow_link | -1.0472 to 2.0944 | -25.0 to 25.0 |
| 24 | left_wrist_roll_joint | revolute | left_elbow_link | left_wrist_roll_rubber_hand | -1.972222054 to 1.972222054 | -25.0 to 25.0 |
| 25 | right_shoulder_pitch_joint | revolute | torso_link | right_shoulder_pitch_link | -3.0892 to 2.6704 | -25.0 to 25.0 |
| 26 | right_shoulder_roll_joint | revolute | right_shoulder_pitch_link | right_shoulder_roll_link | -2.2515 to 1.5882 | -25.0 to 25.0 |
| 27 | right_shoulder_yaw_joint | revolute | right_shoulder_roll_link | right_shoulder_yaw_link | -2.618 to 2.618 | -25.0 to 25.0 |
| 28 | right_elbow_joint | revolute | right_shoulder_yaw_link | right_elbow_link | -1.0472 to 2.0944 | -25.0 to 25.0 |
| 29 | right_wrist_roll_joint | revolute | right_elbow_link | right_wrist_roll_rubber_hand | -1.972222054 to 1.972222054 | -25.0 to 25.0 |
