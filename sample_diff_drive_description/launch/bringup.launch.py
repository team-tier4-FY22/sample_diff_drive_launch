import os
import xacro
import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    urdf_xacro_path = os.path.join(get_package_share_directory('sample_diff_drive_description'), 'urdf/vehicle.xacro')
    urdf_xacro = xacro.process_file(urdf_xacro_path)
    urdf_xml = urdf_xacro.toprettyxml()
    rsp = launch_ros.actions.Node(package='robot_state_publisher',
                                  executable='robot_state_publisher',
                                  output='screen',
                                  parameters=[
                                      {'robot_description': urdf_xml}
                                  ])
    jsp = launch_ros.actions.Node(package='joint_state_publisher',
                                  executable='joint_state_publisher',
                                  output='screen')
    return launch.LaunchDescription([rsp, jsp])

