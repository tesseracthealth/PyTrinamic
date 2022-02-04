from abc import ABC
from pytrinamic.tmcl import TMCL, TMCLRequest, TMCLCommand, TMCLReply
from pytrinamic.helpers import TMC_helpers


class TmclInterface(ABC):
    """
    This class is a base class for sending TMCL commands over a communication
    interface.

    Each instance of this class represents one TMCL host. The bus connection for
    the TMCL communication is represented by a subclass inheriting this base
    class. An application with multiple busses should therefore use subclasses
    for all types of busses (e.g. one USB TMCL interface and one serial TMCL
    interface) and create exactly one instance of one of those subclasses per
    bus.

    A subclass is required to override the following functions:
        _send(self, hostID, moduleID, data)
        _recv(self, hostID, moduleID)

    A subclass may use the boolean _debug attribute to toggle printing further
    debug output.

    A subclass may read the _HOST_ID and _MODULE_ID parameters.
    """

    def __init__(self, host_id=2, default_module_id=1, debug=False):
        """
        Parameters:
            host_id:
                Type: int, optional, default value: 2
                The ID of the TMCL host. This ID is the same for each module
                when communicating with multiple modules.
            default_module_id:
                Type: int, optional, default value: 1
                The default module ID to use when no ID is given to any of the
                tmcl_interface functions. When only communicating with one
                module a script can omit the moduleID for all TMCL interface
                calls by declaring this default value once at the start.
            debug:
                Type: bool, optional, default: False
                A switch for enabling debug mode. Can be changed with
                enableDebug(). In debug mode all sent and received TMCL packets
                get dumped to stdout. The boolean _debug attribute holds the
                current state of debug mode - subclasses may read it to print
                further debug output.
        """

        TMCL.validate_host_id(host_id)
        TMCL.validate_module_id(default_module_id)

        if not type(debug) == bool:
            raise TypeError

        self._HOST_ID = host_id
        self._MODULE_ID = default_module_id
        self._debug = debug

    def enable_debug(self, enable):
        """
        Set the debug mode, which dumps all TMCL datagrams written and read.
        """
        if type(enable) != bool:
            raise TypeError("Expected boolean value")

        self._debug = enable

    def print_info(self):
        info = "ConnectionInterface {"
        info += "'debug_enabled':" + str(self._debug) + ", "
        info = info[:-2]
        info += "}"
        print(info)

    def _send(self, host_id, module_id, data):
        """
        Send the bytearray [data] representing a TMCL command. The length of
        [data] is 9. The hostID and moduleID parameters may be used for extended
        addressing options available on the implemented communication interface.
        """
        raise NotImplementedError("The TMCL interface requires an implementation of the send() function")

    def _recv(self, host_id, module_id):
        """
        Receive a TMCL reply and return it as a bytearray. The length of the
        returned byte array is 9. The hostID and moduleID parameters may be used
        for extended addressing options available on the implemented
        communication interface.
        """
        raise NotImplementedError("The TMCL interface requires an implementation of the receive() function")

    def send_request(self, request, module_id=None):
        """
        Send a TMCL_Request and read back a TMCL_Reply. This function blocks until
        the reply has been received.
        """
        if not module_id:
            module_id = self._MODULE_ID

        if self._debug:
            request.dump()

        self._send(self._HOST_ID, module_id, request.to_buffer())
        reply = TMCLReply.from_buffer(self._recv(self._HOST_ID, module_id))

        if self._debug:
            reply.dump()

        return reply

    def send(self, opcode, op_type, motor, value, module_id=None):
        """
        Send a TMCL datagram and read back a reply. This function blocks until
        the reply has been received.
        """
        if not(type(opcode) == type(op_type) == type(motor) == type(value) == int):
            raise TypeError("Expected integer values")

        # If no module ID is given, use the default one
        if not module_id:
            module_id = self._MODULE_ID

        request = TMCLRequest(module_id, opcode, op_type, motor, value)

        if self._debug:
            request.dump()

        self._send(self._HOST_ID, module_id, request.to_buffer())
        reply = TMCLReply.from_buffer(self._recv(self._HOST_ID, module_id))

        if self._debug:
            reply.dump()

        return reply

    def send_boot(self, module_id=None):
        """
        Send the command for entering bootloader mode. This TMCL command does
        result in a reply.
        """
        # If no module ID is given, use the default one
        if not module_id:
            module_id = self._MODULE_ID

        request = TMCLRequest(module_id, TMCLCommand.BOOT, 0x81, 0x92, 0xA3B4C5D6)

        if self._debug:
            request.dump()

        # Send the request
        self._send(self._HOST_ID, module_id, request.to_buffer())

    def get_version_string(self, module_id=None):
        """
        Request the ASCII version string.
        """
        reply = self.send(TMCLCommand.GET_FIRMWARE_VERSION, 0, 0, 0, module_id)
        return reply.version_string()

    # General parameter access functions
    def get_parameter(self, p_command, p_type, p_axis, p_value, module_id=None, signed=False):
        value = self.send(p_command, p_type, p_axis, p_value, module_id).value
        return TMC_helpers.to_signed_32(value) if signed else value

    def set_parameter(self, p_command, p_type, p_axis, p_value, module_id=None):
        return self.send(p_command, p_type, p_axis, p_value, module_id)

    # Axis parameter access functions
    def get_axis_parameter(self, command_type, axis, module_id=None, signed=False):
        value = self.send(TMCLCommand.GAP, command_type, axis, 0, module_id).value
        return TMC_helpers.to_signed_32(value) if signed else value

    def set_axis_parameter(self, command_type, axis, value, module_id=None):
        return self.send(TMCLCommand.SAP, command_type, axis, value, module_id)

    def store_axis_parameter(self, command_type, axis, module_id=None):
        return self.send(TMCLCommand.STAP, command_type, axis, 0, module_id)

    def set_and_store_axis_parameter(self, command_type, axis, value, module_id=None):
        self.send(TMCLCommand.SAP, command_type, axis, value, module_id)
        self.send(TMCLCommand.STAP, command_type, axis, 0, module_id)

    # Global parameter access functions
    def get_global_parameter(self, command_type, bank, module_id=None, signed=False):
        value = self.send(TMCLCommand.GGP, command_type, bank, 0, module_id).value
        return TMC_helpers.to_signed_32(value) if signed else value

    def set_global_parameter(self, command_type, bank, value, module_id=None):
        return self.send(TMCLCommand.SGP, command_type, bank, value, module_id)

    def store_global_parameter(self, command_type, bank, module_id=None):
        return self.send(TMCLCommand.STGP, command_type, bank, 0, module_id)

    def set_and_store_global_parameter(self, command_type, bank, value, module_id=None):
        self.send(TMCLCommand.SGP, command_type, bank, value, module_id)
        self.send(TMCLCommand.STGP, command_type, bank, 0, module_id)

    # Register access functions
    def write_mc(self, register_address, value, module_id=None):
        return self.write_register(register_address, TMCLCommand.WRITE_MC, 0, value, module_id)

    def read_mc(self, register_address, module_id=None, signed=False):
        return self.read_register(register_address, TMCLCommand.READ_MC, 0, module_id, signed)

    def write_mc_by_id(self, ic_id, register_address, value, module_id=None):
        return self.write_register(register_address, TMCLCommand.WRITE_MC, ic_id, value, module_id)

    def read_mc_by_id(self, ic_id, register_address, module_id=None, signed=False):
        return self.read_register(register_address, TMCLCommand.READ_MC, ic_id, module_id, signed)

    def write_drv(self, register_address, value, module_id=None):
        return self.write_register(register_address, TMCLCommand.WRITE_DRV, 1, value, module_id)

    def read_drv(self, register_address, module_id=None, signed=False):
        return self.read_register(register_address, TMCLCommand.READ_DRV, 1, module_id, signed)

    def read_register(self, register_address, command, channel, module_id=None, signed=False):
        value = self.send(command, register_address, channel, 0, module_id).value
        return TMC_helpers.to_signed_32(value) if signed else value

    def write_register(self, register_address, command, channel, value, module_id=None):
        return self.send(command, register_address, channel, value, module_id)

    # Motion control functions
    def rotate(self, motor, velocity, module_id=None):
        return self.send(TMCLCommand.ROR, 0, motor, velocity, module_id)

    def stop(self, motor, module_id=None):
        return self.send(TMCLCommand.MST, 0, motor, 0, module_id)

    def move(self, move_type, motor, position, module_id=None):
        return self.send(TMCLCommand.MVP, move_type, motor, position, module_id)

    def move_to(self, motor, position, module_id=None):
        """
        Use the TMCL MVP command to perform an absolute movement.

        Returns the value of the reply. Refer to the documentation of your
        specific module for details on what is returned.
        """
        return self.move(0, motor, position, module_id).value

    def move_by(self, motor, distance, module_id=None):
        """
        Use the TMCL MVP command to perform a relative movement.

        Returns the value of the reply. Refer to the documentation of your
        specific module for details on what is returned.
        """
        return self.move(1, motor, distance, module_id).value

    # IO pin functions
    def get_analog_input(self, x, module_id=None):
        return self.send(TMCLCommand.GIO, x, 1, 0, module_id).value

    def get_digital_input(self, x, module_id=None):
        return self.send(TMCLCommand.GIO, x, 0, 0, module_id).value

    def get_digital_output(self, x, module_id=None):
        return self.send(TMCLCommand.GIO, x, 2, 0, module_id).value

    def set_digital_output(self, x, module_id=None):
        self.send(TMCLCommand.SIO, x, 2, 1, module_id)

    def clear_digital_output(self, x, module_id=None):
        self.send(TMCLCommand.SIO, x, 2, 0, module_id)