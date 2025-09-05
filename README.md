# ✋ Hand Gesture Controlled Presentation

Control your presentations seamlessly using hand gestures and OpenCV.
With just your webcam, you can:

Navigate slides left & right

Use a virtual pointer

Draw annotations

Erase annotations

# 📌 Features

Gesture Recognition (powered by cvzone
 HandTrackingModule).

Slide Navigation:

 Gesture                     Action                

 ☝️ Index finger up         | Draw on slide         

 ✌️ Index + Middle finger   | Pointer               

 👆 Hand up (left gesture)  | Previous Slide       

 👉 Hand up (right gesture) | Next Slide            

 ✋ All fingers up          | Erase last annotation 


# ⚙️ Installation
## Clone this repository
git clone https://github.com/NiShAnt12356/hand-gesture-presentation.git
cd hand-gesture-presentation

## Install dependencies
pip install opencv-python cvzone numpy

## ▶️ How to Run

Place your presentation images in a folder named presentation/ (e.g., slide1.jpg, slide2.png).

Run the script:

python app.py


# Use gestures to control slides.

## ✨ Gesture Controls

☝️ Index finger up	Draw on slide

✌️ Index + Middle finger	Pointer

👆 Left swipe gesture	Previous Slide

👉 Right swipe gesture	Next Slide

✋ All fingers up	Erase last annotation


# 📂 Project Structure

presentation/ → Folder containing slides (images)

app.py → Main Python script

README.md → Project documentation

# 📊 Workflow Diagram

##  Illustration
Gesture → Action Mapping

Gesture: ☝️   → Draw Annotation

Gesture: ✌️   → Pointer Mode

Gesture: 👆   → Previous Slide

Gesture: 👉   → Next Slide

Gesture: ✋   → Erase Drawing

# 🛠️ Dependencies

OpenCV
 – Image & video processing

cvzone
 – Hand tracking wrapper

NumPy
 – Array operations

# 🚀 Future Improvements

Support for PPT/PDF files directly

Add multi-hand controls

Gesture customization via config file

# 🙌 Contributing

Pull requests are welcome! Please open an issue first to discuss what you’d like to change.
