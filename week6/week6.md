## Week 6 Notes

1. What are the benefits of simulating a drone with software/hardware-in-the-loop before flying?

   a. Simulating a drone provides cost savings as crashing real drones is expensive and more importantly allows for faster testing through its modeling of real-life scenarios, processing power (hardware-in-the-loop), and communication links.

   b. Simulating a drone allows for getting thousands of realistic flights to train AI models.

   c. Simulator examples include Gazebo (with PX4), Isaac Sim, ArduPilot, AirSim, and Flightmare.

2. How is machine learning used to improve drone autonomy (navigation, obstacle avoidance, etc.)? What benefits does it have over traditional guidance systems like PID loops?

   a. Supervised ML learns from labeled flight data for things like obstacle detection, unsupervised ML discovers pattern in sensor data for things like terrain clustering, and reinforcement learning learns by trial and error in simulation for things like agile maneuvers.

   b. Machine learning is used for navigation and path planning in cluttered environments, real-time obstacle avoidance using vision models, and adaptive control under disturbances (like wind).

   c. One challenge with these policies is Sim2Real transfer: making sure simulation-based policies work in the real world (ideal is zeroshot: works perfectly on the first try).

   d. A benefit machine learning has over traditional guidance systems is that it requires less human effort in finetuning policies manually.

3. What is ROS, and why is it universal in autonomous robotics?

   a. Robot Operating System (ROS) is not an operating system, but rather a piece of middleware that helps different parts of a robot communicate.

   b. ROS includes a modular, node-based system for reusable code, communication systems to pass messages between nodes, an ecosystem with lots of ROS packages for existing sensors, and simulation support for Gazebo and Isaac Sim out of the box, which is why almost everyone else uses it.

   c. A ROS Node is a process that performs a specific function, a ROS Topic is a named place where nodes can publish messages or subscribe to listen for messages, a ROS Message is a data structure sent between nodes, a ROS Service is a request/response communnication directly between nodes, a ROS Action is a Service that supports long-running tasks, a ROS Package is a collection of ROS code, nodes, and config files, and a ROS Launch File is a script that starts and initializes nodes.

4. What are the steps/challenges of deploying ROS on embedded systems like the drone?

   a. Install ROS 2 Humble (newer versions exist but aren't necessarily compatible with everything else) on Ubuntu

   b. Try running a demo

   c. Use a simulation (e.g. Gazebo) to test ROS with an actual drone

   d. Explore ROS tutorials to do more stuff

5. Thanks and final thoughts

   Thank you, Isaac, for teaching us so much about drones!

