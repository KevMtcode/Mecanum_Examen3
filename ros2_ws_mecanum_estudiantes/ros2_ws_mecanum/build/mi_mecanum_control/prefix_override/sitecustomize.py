import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/kevin/Mecanum-Examen-3/Mecanum_Examen3/ros2_ws_mecanum/install/mi_mecanum_control'
