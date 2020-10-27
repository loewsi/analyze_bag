import rosbag
import numpy as np
bag = rosbag.Bag('example_rosbag_H3.bag')
readtopics = list(bag.get_type_and_topic_info()[1].keys())

for i in range(0, np.size(readtopics)):
    dt=[]
    t_0=0.
    t_1=0.
    for topic, msg, t in bag.read_messages(topics=str(readtopics[i])):
        t_1=t_0
        t_0=t.to_sec()
        dt.append(t_0-t_1)
    del dt[0]
    print(readtopics[i], ":")
    print("  num_messages:", np.size(dt)+1)
    print("  period:")
    print("    min:", "%.2f" % (np.min(dt)))
    print("    max:", "%.2f" % (np.max(dt)))
    print("    average:", "%.2f" % (np.average(dt)))
    print("    media:", "%.2f" % (np.median(dt)))
    print(" ")





