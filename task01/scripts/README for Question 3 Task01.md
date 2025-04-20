# 🐢 Question 3 – TurtleSim Bot + State Machine

## 🎯 The Goal

The question had **bonus points** for using a state machine — so obviously, I wanted to go for that. My **first idea** was to just create a ROS package where a bot's position and direction could be manually entered by the user. Pretty simple, right?

Then I remembered **TurtleSim**, and thought:

> “Wait… what if I could *see* the bot move based on user input?”

So yeah, I decided to integrate that.  
**Was it a good idea?** Maybe not.  
**Was it fun?** Absolutely. 😂

---

## 🛠️ Node 1 – `turtle_cont.py` (Turtle Controller)

This file handled **movement commands** — forward, left, right, etc.

- I didn’t even need to Google how to take strings and integers this time 😎
- Defined a function to send velocity commands (`send_cmd`)
- Controlled **linear** and **angular** velocity of the turtle

### 🌀 The Funny Part

I spent like **20 minutes wondering why the turtle wouldn't turn left**…  
Turns out I was setting `angular.x` instead of `angular.z`.  
*bruh.*

After fixing that, I played around to find a **decent turning value** — `1.6` radians worked well for a ~90° turn.

---

## 🔄 Node 2 – `turtle_state_machine.py` (State Machine + Tracker)

Here’s where it got a bit more complex. For the bonus part, I made a **state machine** to track:

- **Direction** → North, South, East, West
- **Coordinates** → `x`, `y` from turtle’s position

### 🧠 How I Did It

- Googled how to convert **radians to degrees**
- Used the turtle’s orientation angle (from the `/turtle1/pose` topic)
- Wrote logic to translate degrees into **named directions**
- Used `rospy.loginfo()` to print both direction and location

---

## 📍 The Origin Problem

I read the question again and realized…  
The **turtle had to start from (0, 0)** — and mine wasn’t.

So I asked ChatGPT (*my coding bestie lol*) and it told me to use:

python
teleport_absolute(0, 0, 0)
That let me teleport the turtle to the origin at the start of the code. Problem solved!

🔚 Final Thoughts
This question taught me a LOT:

Integrating visuals into ROS (via TurtleSim)

Writing a basic state machine

Using math for angle conversion

Working with Pose messages and movement control

Yeah, it took time and a bit of pain, but honestly — seeing the turtle move like a robot you built logic for felt amazing.

Would 100% do it again. 


