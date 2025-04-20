# 🤖 Solving Question 1 – ROS ChatBot

## 📚 Getting Started

Before even jumping into the problem, I made sure to complete the ROS tutorial that was shared in the group. It honestly took quite a while, but it helped me become familiar with how ROS works—especially the basics like nodes, topics, publishers, and subscribers.

## 🛠️ Building the ChatBot

Once I felt ready, I started working on the chatbot. Here's how it went:

### 🧩 The First Problem

I didn’t know what to import to use strings in ROS. A quick Google search taught me that I needed to import from:

python
from std_msgs.msg import String
Simple fix, but it felt like a little win.

👥 Setting Up the Publishers
I created two publishers: jolyne and joestar. My initial idea was to take input from one side, publish it to a topic (like /chatter), and have the other node subscribe to it—essentially making it an interactive back-and-forth chat from both ends.

But then I realized, it wasn’t mentioned anywhere in the question that both sides had to subscribe. So I simplified my plan: let both nodes publish messages, and then make just one subscriber that would print whatever is published to the topic.

🧵 Enter Threading
Now the big question was: How can I make both users send messages from the same node?

Back to the internet I went. That’s when I discovered Python’s threading module. Using threads, I could handle both publishers from the same script—and it finally worked!

😄 The Final Feeling
When everything came together and I saw the messages flowing as intended, I was genuinely happy. It felt like a real achievement, especially because this was my first ROS script involving real interaction.

🙌 Shoutouts
Mosh Programming on YouTube — for helping me understand threading in Python.

ChatGPT — for cleaning up my code, fixing indentation, and helping me debug issues I got stuck on.
