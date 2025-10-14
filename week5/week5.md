## Week 5 Notes

1. How do we communicate with the drone while it’s in the air?

   a. The ground station communicates with the onboard computer over WiFi, with the drone being a WiFi hotspot. This uses the UDP protocol, which is different from TCP in that instead of being reliable through acknowledgement of a stable connection it allows for packet loss by just throwing data and seeing what sticks (being faster and more lightweight), which is less of a hassle for one-way transmission of real-time data.

   b. The flight controller communicates with the ground station using radio.

2. What is the role of the onboard computer system and how does it complement the flight controller? How does it communicate?

   a. The onboard computer system runs ROS in order to do complex tasks for decision-making and higher-level control like object detection, SLAM, and mission logic.

   b. The onboard computer uses Ethernet to connect to the gimbal camera, USB-C to transfer data, HDMI to see what's in the brain of the computer (if needed), and 40 extra pins.

3. What are the trade-offs between different data links (WiFi, radio, LTE)?

   a. WiFi has high bandwidth and works for short-range communications, but requires line of sight and has a very limited range (no more than a few hundred meters) with some interference in commonly used bands.

   b. Radio is very long range and reliable and low-latency, but requires dedicated hardware and is low bandwidth (and has regulations on allowed frequencies).

   c. LTE has a very wide coverage, has a high bandwidth and datarate, and runs on cell towers such that no line of sight is required, but latency is still higher than WiFi, it requires a SIM card and data plan, and depending on how far you are from cities you still have dead zones.

   d. Starlink is new and requires a heavy terminal, but it has the benefits of cellular without any coverage problems.

4. How does the onboard computer connect to the ground station or other devices over WiFi? (SSH tutorial)

   a. The onboard computer connects to devices over WiFi using SSH.
