import os

from ament_index_python.packages import get_package_share_directory

from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

robot_ns = ""

def generate_launch_description():
    pkg_path = os.path.join(get_package_share_directory('ros2_whill_gazebo'))
    world_path = os.path.join(pkg_path,
                        'world', "field.world")
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gzserver.launch.py')
            ),
            launch_arguments={'world': world_path}.items(),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gzclient.launch.py')
            ),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_path, 'launch', 'robot_show.launch.py')
            ),
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            namespace=robot_ns,
            arguments=['-topic', 'robot_description',
                '-entity', 'whill'
                , "-x", "1.0", "-y", "-0.5", "-z", "0.0"
                , "-R", "0.0", "-P", "0.0", "-Y", "-1.5708"
                ],
            output='screen'
        ),
    ])
