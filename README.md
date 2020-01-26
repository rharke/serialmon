# serialmon.py

Monitor a serial port for trigger phrases and run scripts in response.

## Details

This is a simple Python script which monitors a serial port for certain trigger phrases. When they
are seen, a script is run.

I use it to monitor the activity of a certain "smart" doorbell and play a custom chime. I'm sure
there's other uses.

You need to make some minimal customizations to `config.yml` to tell the script about the triggers
to watch for, and what to do in response, then run the script:

```
serialmon.py config.yml
```

Configuration options are listed in the `config.yml` file, but they're really simple.

There's a sample unit definition to run the script as a service, if you're using `systemd`.

## FAQ

### What are the requirements?

Python 3.x, `pySerial`, and `PyYAML`. It probably works on Windows or Linux, but I've only tested
Linux.

### Does it work with Python 2.7?

Doubt it.

### You're monitoring a smart doorbell with this? Smart doorbells have serial ports?

You might be surprised what you find if you open one of these things up. If you don't mind voiding
some warranties, of course.
