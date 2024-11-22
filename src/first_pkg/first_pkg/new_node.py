import rclpy
from rclpy.node import Node


from std_msgs.msg import String

class new_node(Node):
    def __init__(self):
        super().__init__('new')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Jaxon'
        self.publisher_.publish(msg)
        self.get_logger().info("%s" % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    new = new_node()

    rclpy.spin(new)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    new.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()