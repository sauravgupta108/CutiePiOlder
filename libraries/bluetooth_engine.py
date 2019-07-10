from helper import get_logger


class BluetoothClient:
    """
    Class to interface with Arduino using Bluetooth.
    """
    def __init__(self):
        self.logger = get_logger(_type="bluetooth", name=__name__)

    def start(self):
        """
        It switches Bluetooth on and Connect
        :return: True/False if Bluetooth is on and connected.
        """
        pass
        return True

    def is_active(self):
        """
        Check if Bluetooth is On and Connected.
        :return: True/False
        """
        pass
        return True

    def is_connected(self):
        pass

    def transmit_signal(self, signal):
        """
        Transmit signal to Arduino via Bluetooth
        :param signal: signal to transmit
        :return: True/False if signal transmitted.
        """
        connected_device = self.connect_to_arduino()
        bytes_sent = connected_device.send(signal)
        self.logger.info("%s bytes sent." % bytes_sent)
        return True is bytes_sent > 0 else False

    def start_receiving(self):
        """
        Start receiving signal from Arduino via Bluetooth.
        :return: True/False if reception started or not.
        """
        pass

    def connect_to_arduino(self):
        import bluetooth as bt
        name, address, port = self.get_device()
        
        self.logger.info("Attempting to connect with device %s" % name)        
        
        try:
            bt_sock = bt.BluetoothSocket(bt.RFCOMM)
            bt_sock.connect(address, port)
            self.logger.info("Connected with device %s at port %s" % (name, str(port)))
            return bt_sock
        except bluetooth.btcommon.BluetoothError as e:
            self.logger.exception("Unable to connect with device %s" % name)
            raise bluetooth.btcommon.BluetoothError("Unable to connect with device %s" % name)

    def get_device(self):
        self.logger.info("Getting Bluetooth Device detailss")
        with open(os.path.join(os.getcwd(), 'config/bluetooth_devices.json'), "r") as bt_dev:
            devices = json.load(bt_dev)
            self.logger.info("Got Bluetooth Device details")
            return (devices['hc05']["name"], devices['hc05']["device_id"], devices['hc05']["port"])
        return (None, None, None)

    def disconnect(self):
        pass
