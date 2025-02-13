#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from typing import List, Dict
from parser import (
    RobotFormatParser,
    Joint,
    # Actuator,
)


def joint_to_dict(joint: Joint) -> Dict:
    """Convert Joint object to dictionary, excluding the name field."""
    return {
        "joint_type": joint.joint_type,
        "index": joint.index,
        "limits": joint.limits or {},
        "parent": joint.parent,
        "child": joint.child,
    }


def create_markdown_table(joints: List[Joint]) -> str:
    """Create a markdown table from joint information."""
    # Define table headers
    headers = [
        "Index",
        "Name",
        "Type",
        "Parent",
        "Child",
        "Angle Limits",
        "Force Limits",
    ]

    # Create header row with alignment
    markdown = "| " + " | ".join(headers) + " |\n"
    markdown += "|" + "|".join(["---" for _ in headers]) + "|\n"

    # Add each joint as a row
    for joint in joints:
        position_limits = "N/A"
        force_limits = "N/A"

        if joint.limits:
            if "angle_lower" in joint.limits and "angle_upper" in joint.limits:
                position_limits = (
                    f"{joint.limits['angle_lower']} to {joint.limits['angle_upper']}"
                )
            if "force_lower" in joint.limits and "force_upper" in joint.limits:
                force_limits = (
                    f"{joint.limits['force_lower']} to {joint.limits['force_upper']}"
                )

        row = [
            str(joint.index),
            joint.name,
            joint.joint_type,
            joint.parent or "N/A",
            joint.child or "N/A",
            position_limits,
            force_limits,
        ]

        markdown += "| " + " | ".join(row) + " |\n"

    return markdown


# def actuator_to_dict(actuator: Actuator) -> Dict:
#     """Convert Actuator object to dictionary, excluding the name field."""
#     return {
#         "joint": actuator.joint,
#         "range": actuator.range,
#         "forcerange": actuator.forcerange,
#     }


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Convert robot description file to Markdown and JSON"
    )
    parser.add_argument("input_file", type=str, help="Path to input URDF or MJCF file")
    parser.add_argument(
        "--output-dir",
        type=str,
        default="output",
        help="Directory for output files (default: output)",
    )
    args = parser.parse_args()

    # Create output directory if it doesn't exist
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get input file name without extension
    input_path = Path(args.input_file)
    base_name = input_path.stem

    try:
        # Parse the robot description file
        robot_parser = RobotFormatParser(args.input_file)
        joints = robot_parser.parse_joints()
        # actuators = robot_parser.parse_actuators()

        # Create markdown output
        markdown_content = f"# Robot Joint Configuration: {base_name}\n\n"
        markdown_content += "## Joints\n\n"
        markdown_content += create_markdown_table(joints)

        # # Add actuator information if available
        # if actuators:
        #     markdown_content += "\n## Actuators\n\n"
        #     markdown_content += "| Name | Joint | Position Range | Force Range |\n"
        #     markdown_content += "|------|--------|----------------|-------------|\n"
        #
        #     for actuator in actuators:
        #         position_range = "N/A"
        #         force_range = "N/A"
        #
        #         if actuator.range:
        #             position_range = (
        #                 f"{actuator.range[0]:.2f} to {actuator.range[1]:.2f}"
        #             )
        #         if actuator.forcerange:
        #             force_range = (
        #                 f"{actuator.forcerange[0]:.2f} to {actuator.forcerange[1]:.2f}"
        #             )
        #
        #         markdown_content += f"| {actuator.name} | {actuator.joint} | {position_range} | {force_range} |\n"

        # Save Markdown file
        markdown_path = output_dir / f"{base_name}_config.md"
        with open(markdown_path, "w") as f:
            f.write(markdown_content)

        json_data = {
            "format": robot_parser.format,
            "joints": {joint.name: joint_to_dict(joint) for joint in joints},
            # "actuators": {
            #     actuator.name: actuator_to_dict(actuator) for actuator in actuators
            # },
        }

        # Save JSON file
        json_path = output_dir / f"{base_name}_config.json"
        with open(json_path, "w") as f:
            json.dump(json_data, f)

        print("Successfully created:")
        print(f"  Markdown file: {markdown_path}")
        print(f"  JSON file: {json_path}")

    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
