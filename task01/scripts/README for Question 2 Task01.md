# 🔁 Question 2 – ROS Multi-Node Data Flow

## 🤦 How It Started

So... I actually made q2.py *before even reading the question properly*. Once I finally sat down and read the full question, I realized I couldn’t just do everything in one node—I'd need to break it up into **multiple specific nodes**, each doing part of the task.

---

## 🧠 Learning On the Fly

As usual, I ran into something new. I had no idea how to use integers in ROS, so I Googled it—and boom:

python
from std_msgs.msg import Int32
## 🧐 Reading the Question

After reading the question, I quickly realized this wasn’t a single-node task anymore. I'd need to create **multiple nodes**, each doing a specific job and passing data to the next. Time to level up.

---

🧱 Node 1 – ogpub (Original Publisher)
This was the first publisher. All it had to do was continuously publish multiples of 2.

So I did something like:

python
Copy code
num = 1
while not rospy.is_shutdown():
    pub.publish(num * 2)
    num += 1
And that got the stream of even numbers going.

🔄 Node 2 – sub2pub
Next up, this node subscribed to the topic published by ogpub. Once it got the value, it multiplied it by 10 and published the result on another topic.

Kind of like a middleman:

Listens 👂

Processes 🔄

Publishes 📤

Simple and neat.

🔚 Node 3 – fsub (Final Subscriber)
The last node in the chain just subscribed to the topic from sub2pub. It received the value, added 5, and then simply printed the result using rospy.loginfo().

No need to publish again—this was the final step.

✅ Final Thoughts
This question was a smooth ride compared to the first one. The flow of data from node to node made a lot of sense once I broke it down step-by-step.

Also, by now I was way more comfortable with:

Setting up publishers/subscribers

Chaining multiple nodes

Working with Int32 message types

Each question is building my confidence, and this one made me appreciate how clean multi-node systems can be when done right.
