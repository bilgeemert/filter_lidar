import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from os.path import join as Path


rviz_path=  os.path.join(
        get_package_share_directory('filter_scan'),
        'rviz',
        'filter_rviz.rviz'
    )

config_file = os.path.join(
        get_package_share_directory('filter_scan'),
        
        'params.yaml'
    )

rviz_file=  Node(
    package="rviz2",
    executable="rviz2",
    arguments=['-d', rviz_path],  # Use 'arguments' to pass command-line arguments
    output="screen"
)

filter_scan = Node(
    package="filter_scan",                                               # ros_ign_bridge eski versiyonda kullanılır.
    executable="distance_node",
  
    parameters=[config_file],
    output="screen"
)


def generate_launch_description():
    return LaunchDescription([
          filter_scan,
          rviz_file,
          
                  
    ]) 