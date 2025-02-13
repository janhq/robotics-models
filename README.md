# Collection of Common Robot Model file in URDF and MJCF

This repository intention is to amass a collection of different common robot model including but not limited to humanoid, quadruped, and robot arm from notable manufacturer. These repository does not and will not support any other robotic format so we can remain consistent with the effort to unified robot development.

Include in this repository, there will also be complimentary script to help with extracting basic information and mapping of robot joint and link to a Mardown file and a JSON file to help developer more easily import and config the robot model in their simulation.

## How to use the script

If you just need to generate the `json` mapping and the `md` file. Use `convert.py` as follow:

> python convert.py path/to/your/robot.urdf --output-dir desc

If you want to generate for a whole folder at once then use `batch_convert.py` as follow:

> python batch_convert.py /path/to/input/directory
