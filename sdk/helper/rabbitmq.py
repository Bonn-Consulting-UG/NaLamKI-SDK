import paho.mqtt.client as mqtt
import logging
import os

class RabbitMQHelper:

    """
    Helper class for establishing connection to MQTT broker. 

    A request/reply pattern is implemented.
    """

    def __init__(self, endpoint: str, port: int, topic: str, username: str, password: str, path: str = "") -> None:
        """
        Connection setup for MQTT broker.

        :param endpoint: endpoint to MQTT broker
        :param port: port of the endpoint 
        :param topic: the topic for sending the message
        :param username: username for MQTT broker
        :param password: password for MQTT broker
        :param path: path for message storage (if needed)
        """

        logging.basicConfig(format='%(asctime)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.ERROR)

        self.client = mqtt.Client()
        self.client.username_pw_set(username, password)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        try:
            self.client.connect(endpoint, port, 60)
            self.logger.debug("Connection to MQTT broker successful.")
        except Exception as exp:
            self.logger.error(f"Connection error to MQTT broker. \nMessage: {exp}")

        self.topic = topic
        self.sending_message_back = True
        self.path = path
        self.message = None 

    def check_and_create_path(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def write_message(self, topic, message):
        """
        Sends/writes a message on the topic.

        :param topic: name of the topic
        :param message: message to be sent
        """
        self.client.publish(topic, message)

    def get_message(self, topic):
        """
        Subscribes to a topic and prints the message received.
        
        :param topic: name of the topic
        """
        self.client.subscribe(topic)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.logger.debug("Connected to MQTT broker successfully.")
        else:
            self.logger.error(f"Connection failed with code {rc}.")

    def on_message(self, client, userdata, msg):
        print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

    def listen(self, topic, method=None):
        """
        Listens for messages on a topic.

        :param topic: name of the topic
        :param method: method to handle the message (default is self.on_message)
        """
        self.client.subscribe(topic)
        if method is None:
            self.client.on_message = self.on_message
        else:
            self.client.on_message = method
        self.client.loop_forever()

# Beispiel der Nutzung
# mqtt_helper = MQTTClientHelper(endpoint="mqtt.example.com", port=1883, topic="test/topic", username="user", password="pass")
# mqtt_helper.write_message("test/topic", "Hello MQTT")
# mqtt_helper.get_message("test/topic")
# mqtt_helper.listen("test/topic")
