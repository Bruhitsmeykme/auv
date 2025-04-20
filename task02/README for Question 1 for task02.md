# 📷 Task 2 – OpenCV + ROS Camera Pipeline

## 🤕 WSL Woes...

So this one was supposed to be all about using **OpenCV** with ROS, and I was honestly excited to try it.

Until...

> Spent 1 hour trying to get OpenCV to work on WSL —  
> **Only to find out it’s not really supported.**

At that point, I had two options:
1. Boot up Ubuntu with ROS on VirtualBox
2. Cry (optional)
3. Just write the code in WSL and hope it works 🤷‍♂️

I went with option 3.

---

## 📚 What I Learned

- Basics of **OpenCV** in Python
- Using **`cv_bridge`** to convert between ROS and OpenCV image types
- Subscribing to a camera feed topic in ROS
- Displaying real-time video frames using `cv2.imshow()`

---

## 🧠 My Approach

### 🔧 Code Structure

I created a class called `CameraViewer` and defined:

- `__init__()`  
  → sets up the subscriber to the camera feed

- `image_callback()`  
  → uses `cv_bridge` to convert the image and display it using OpenCV

### 🎥 Camera Pipeline

The first question in Task 2 was just about creating a working pipeline —  
aka showing camera feed using OpenCV in ROS.

Here’s the process in simple terms:
1. Import OpenCV and cv_bridge
2. Subscribe to `/camera/image_raw` or whatever camera topic
3. Use `CvBridge` to convert image to OpenCV format
4. Display it using `cv2.imshow()`

---

## ✅ Final Notes

I **couldn’t test** the code because I was on WSL,  
but I got it **reviewed by ChatGPT** (and it looked correct) —  
so fingers crossed, it should work on a proper Ubuntu setup.

There wasn’t too much space to get creative here, since it’s a very standard setup,  
but I still learned a lot — especially how OpenCV and ROS talk to each other.
