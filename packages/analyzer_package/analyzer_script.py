import rosbag
bag = rosbag.Bag('/bags/example_rosbag_H3.bag')
print(bag.get_type_and_topic_info()[1].keys())

print(bag.get_type_and_topic_info()[1].values())

#for topic, msg, t in bag.read_messages():
#    print(topic)

