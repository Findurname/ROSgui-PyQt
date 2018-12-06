# ROSgui-PyQt
Example on how develop a user interface with Qt Designer (PyQt) to communicate with rosmaster (publisher and subscriber)

Didn't find great examples on how to publish and subscribe to rostopic using a gui, so I wrote this breaf code.

If you want to run it, you'll have to have:

1-Ros kinetic installed ( https://github.com/HackInstitute/ros-hackathon/wiki/Installation-of-ROS-on-Ubuntu )
2-If you want to edit or to create your own gui with Qt Designer, you'll must have everything set up ( https://gist.github.com/ujjwal96/1dcd57542bdaf3c9d1b0dd526ccd44ff )

My code subscribes the /chatter topic, provided by the node "talker" from rospy_tutorials pkg.

So:
1-Be sure rosmaster is running
2-Rosrun talker.py
3-Run the gui
