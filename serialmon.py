#!/usr/bin/python3

import serial, subprocess, sys, yaml

BYTESIZE = { 5: serial.FIVEBITS, 6: serial.SIXBITS, 7: serial.SEVENBITS, 8: serial.EIGHTBITS }
PARITY = { 'N': serial.PARITY_NONE, 'E': serial.PARITY_EVEN, 'O': serial.PARITY_ODD, 'M': serial.PARITY_MARK, 'S': serial.PARITY_SPACE }
STOPBITS = { 1: serial.STOPBITS_ONE, 1.5: serial.STOPBITS_ONE_POINT_FIVE, 2: serial.STOPBITS_TWO }

def run(config, ser, triggers, charset):
    while True:
        l = ser.readline().decode(charset).strip()
        print(l)
        for k, v in triggers.items():
            if k in l:
                if isinstance(v, list):
                    # if the trigger is a list, treat it as a command + arguments
                    cmd = v
                else:
                    # otherwise treat it as just a command
                    cmd = [v]
                subprocess.Popen(cmd)

def run_with_config_file(config_file):
    with open(config_file, 'r') as s:
        config = yaml.safe_load(s)

        serial_config = config['serial']
        port = serial_config['port']
        baudrate = serial_config.get('baudrate', 9600)
        bytesize = BYTESIZE[serial_config.get('bytesize', 8)]
        parity = PARITY[serial_config.get('parity', 'N')]
        stopbits = STOPBITS[serial_config.get('stopbits', 1)]
        xonxoff = serial_config.get('xonxoff', False)
        rtscts = serial_config.get('rtscts', False)
        dsrdtr = serial_config.get('dsrdtr', False)
        exclusive = serial_config.get('exclusive')

        ser = serial.Serial(
            port=port, baudrate=baudrate, bytesize=bytesize, parity=parity, stopbits=stopbits,
            xonxoff=xonxoff, rtscts=rtscts, dsrdtr=dsrdtr, exclusive=exclusive
        )

        triggers = config.get('triggers', {})
        charset = config.get('charset', 'ascii')

        run(config, ser, triggers, charset)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        run_with_config_file(sys.argv[1])
    else:
        print('Usage: {} <config_file>'.format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)
