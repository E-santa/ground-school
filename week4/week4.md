## Week 4 Notes

1. What is the role of a flight controller in a drone system, and how does it differ from an onboard computer (like a Jetson)?

   a. The flight controller's role is to control the drone's actual hardware and ensure drone stability.

   b. The onboard computer's role is to do the actual thinking part of controlling the drone: send commands to the flight controller, run computer vision, handle path planning and autonomy.

2. What sensors are typically connected to a flight controller?

   a. IMU (Inertial Measurement Unit): accelerometers and gyroscopes to measure orientation, angular velocity, and linear acceleration (essential for flight stabilization and attitude control), often fused with magnetometers for heading estimation purposes

   b. Barometer (pressure sensor): measures atmospheric pressure (relative to ground point) to estimate attitude, used for attitude hold and smooth vertical control

   c. Magnetometer (compass): detects Earth's magnetic field to determine heading, helps correct yaw drift and supports navigation in GPS-denied environments (annoying to calibrate), needs to be adjusted for with declination

   d. GPS modules: provides global position, velocity, and time data, enabling waypoint navigation, return-to-home, and geofencing (keeping the drone from flying too far away), contains real-time kinematics (RTK) because GPS has so many satellites these days

   e. Drone cameras: usually standard RGB cameras, can send optical data to flight controller and onboard computer and capture full-color images and video, used for mapping, inspection, and general aerial photography, and often mounted on a gimbal for stabilized footage (sensor size, resolution, field-of-view (FOV), frame rate, dynamic range, interface type (HDMI, USB, Ethernet, or UART), and digital vs. optical zoom are all important specs to consider)

   f. RC Transmitter/Receiver: transmitter used by pilot to send commands through stick inputs and switch positions, communicates wirelessly together via radio protocols (2.4 GHz), receiver mounted on drone to receive signals from transmitter and passes commands to flight controller via protocols like Serial Bus (SBUS)

3. What are the key communication protocols between flight controllers and peripherals (e.g. I2C, CAN, MAVLink)?

   a. Serial (UART): direct, basic communication between 2 devices, used for comms between flight controller and onboard computer, GPS modules, and telemetry radios, simple 2-wire setup: TX (transmit) and RX (receive), each UART connection has own set of wires, common for MAVLink messages & debugging

   b. Controller Area Network (CAN): like a device "group chat", robust multi-device protocol used in cars & high-end drones, great for unpredictable environments & long cable runs, used for smart ESCs, gimbals, & advanced sensor networks, has error checking to prevent miscommunication

   c. Inter-Integrated Circuit (I2C): for low-speed communication with devices like barometers, magnetometers, & IMUs, shares 2 wires (SDA (data) and SCL (clock)), multiple devices can talk on the same bus but only one speaks at a time, clock is the heartbeat of the device/drum of the marching band (keeps time for everything)

   d. Serial Peripheral Interface (SPI): same as serial/UART but for multiple devices listening to 1 master device

   e. Micro Air Vehicle Link (MAVLink): "drone language" for commands and telemetry, not a physical protocol (a message format that runs over Serial, UDP, or CAN), used to send commands and receive data, powers communication between flight controller & onboard computer/ground station

   f. Data Distribution Service (DDS): communication protocol used by ROS 2 and modern flight systems, has real-time publish-subscribe messaging between modules, powers direct connection between flight controllers & onboard computers, great for real-time performance (i.e. control loops) unlike MAVLink, also works over Serial

4. How does firmware (e.g. Betaflight) influence the capabilities of the flight controller?

   a. Flight controller contains PID system: integral watches past, proportional watches present, derivative watches the future; needs tuning in order to create critical damping (the optimal situation)

   b. Firmware can be modified to optimize flight characteristics based on the drone itself, has different "flight modes"

   c. Firmware is written by someone else

   d. Firmware options: ArduPilot (baseline), Betaflight (racing), PX4 (robotics)

