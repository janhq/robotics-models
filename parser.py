import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import List, Optional, Dict, Union
from pathlib import Path


@dataclass
class Joint:
    name: str
    joint_type: str
    index: int
    limits: Optional[Dict[str, float]] = None
    parent: Optional[str] = None
    child: Optional[str] = None


@dataclass
class Actuator:
    name: str
    joint: str
    range: Optional[List[float]] = None
    forcerange: Optional[List[float]] = None


class RobotFormatParser:
    def __init__(self, file_path: Union[str, Path]):
        self.file_path = Path(file_path)
        self.tree = ET.parse(self.file_path)
        self.root = self.tree.getroot()
        self.format = self._detect_format()

    def _detect_format(self) -> str:
        """Detect whether the file is URDF or MJCF format."""
        root_tag = self.root.tag
        if root_tag == "robot":
            return "urdf"
        elif root_tag == "mujoco":
            return "mjcf"
        else:
            raise ValueError(f"Unsupported format with root tag: {root_tag}")

    def parse_joints(self) -> List[Joint]:
        """Extract joint information from the robot description."""
        joints = []

        if self.format == "urdf":
            for idx, joint in enumerate(self.root.findall(".//joint")):
                limits = {}
                limit_elem = joint.find("limit")
                if limit_elem is not None:
                    for attr in ["lower", "upper", "effort"]:
                        if attr in limit_elem.attrib:
                            if attr == "lower":
                                limits["angle_lower"] = float(limit_elem.attrib[attr])

                            if attr == "upper":
                                limits["angle_upper"] = float(limit_elem.attrib[attr])

                            if attr == "effort":
                                limits["force_lower"] = -float(limit_elem.attrib[attr])
                                limits["force_upper"] = float(limit_elem.attrib[attr])

                parent = joint.find("parent").attrib["link"]
                child = joint.find("child").attrib["link"]

                joints.append(
                    Joint(
                        name=joint.attrib["name"],
                        joint_type=joint.attrib["type"],
                        index=idx,
                        limits=limits,
                        parent=parent,
                        child=child,
                    )
                )

        elif self.format == "mjcf":
            for idx, joint in enumerate(self.root.findall(".//joint")):
                limits = {}
                if "range" in joint.attrib:
                    range_values = [float(x) for x in joint.attrib["range"].split()]
                    limits["angle_lower"] = range_values[0]
                    limits["angle_upper"] = range_values[1]

                if "actuatorfrcrange" in joint.attrib:
                    range_values = [
                        float(x) for x in joint.attrib["actuatorfrcrange"].split()
                    ]
                    limits["force_lower"] = range_values[0]
                    limits["force_upper"] = range_values[1]

                joints.append(
                    Joint(
                        name=joint.attrib["name"],
                        joint_type=joint.attrib.get("type", "hinge"),
                        index=idx,
                        limits=limits,
                    )
                )

        return joints

    # def parse_actuators(self) -> List[Actuator]:
    #     """Extract actuator information from the robot description."""
    #     actuators = []
    #
    #     if self.format == "urdf":
    #         # URDF doesn't have explicit actuator definitions
    #         # We can create them based on joints with limits
    #         joints = self.parse_joints()
    #         for joint in joints:
    #             if joint.limits:
    #                 actuators.append(
    #                     Actuator(
    #                         name=f"{joint.name}_actuator",
    #                         joint=joint.name,
    #                         range=[
    #                             joint.limits.get("lower", 0),
    #                             joint.limits.get("upper", 0),
    #                         ],
    #                         forcerange=[
    #                             -joint.limits.get("effort", 0),
    #                             joint.limits.get("effort", 0),
    #                         ],
    #                     )
    #                 )
    #
    #     elif self.format == "mjcf":
    #         for actuator in self.root.findall(".//motor"):
    #             range_values = None
    #             if "range" in actuator.attrib:
    #                 range_values = [float(x) for x in actuator.attrib["range"].split()]
    #
    #             force_range = None
    #             if "forcerange" in actuator.attrib:
    #                 force_range = [
    #                     float(x) for x in actuator.attrib["forcerange"].split()
    #                 ]
    #
    #             actuators.append(
    #                 Actuator(
    #                     name=actuator.attrib["name"],
    #                     joint=actuator.attrib["joint"],
    #                     range=range_values,
    #                     forcerange=force_range,
    #                 )
    #             )
    #
    #     return actuators

    def get_joint_by_name(self, joint_name: str) -> Optional[Joint]:
        """Get joint information by name."""
        joints = self.parse_joints()
        for joint in joints:
            if joint.name == joint_name:
                return joint
        return None

    # def get_actuator_by_name(self, actuator_name: str) -> Optional[Actuator]:
    #     """Get actuator information by name."""
    #     actuators = self.parse_actuators()
    #     for actuator in actuators:
    #         if actuator.name == actuator_name:
    #             return actuator
    #     return None
