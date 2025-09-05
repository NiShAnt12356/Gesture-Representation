✋ Hand Gesture Controlled Presentation

Control your presentations seamlessly using hand gestures and OpenCV.
With just your webcam, you can:

Navigate slides left & right

Use a virtual pointer

Draw annotations

Erase annotations

📌 Features

Gesture Recognition (powered by cvzone
 HandTrackingModule).

Slide Navigation:

👆 Left finger → Previous Slide

👉 Right finger → Next Slide

Pointer Mode: Index + Middle finger up

Draw Mode: Only Index finger up

Erase Mode: All five fingers up

Mini Webcam Preview on the presentation screen.

⚙️ Installation
# Clone this repository
git clone https://github.com/yourusername/hand-gesture-presentation.git
cd hand-gesture-presentation

# Install dependencies
pip install opencv-python cvzone numpy

▶️ How to Run

Place your presentation images in a folder named presentation/ (e.g., slide1.jpg, slide2.png).

Run the script:

python app.py


Use gestures to control slides.

✨ Gesture Controls
Gesture	Action
☝️ Index finger up	Draw on slide
✌️ Index + Middle finger	Pointer
👆 Left swipe gesture	Previous Slide
👉 Right swipe gesture	Next Slide
✋ All fingers up	Erase last annotation
📂 Project Structure
hand-gesture-presentation/
│── presentation/       # Folder containing slides (images)
│── app.py              # Main Python script
│── README.md           # Project documentation

📊 Workflow Diagram
Hand Tracking & Gesture Detection
flowchart TD
    A[Webcam Feed] --> B[Hand Detection - cvzone]
    B --> C[Gesture Recognition]
    C --> D[Slide Navigation]
    C --> E[Pointer Mode]
    C --> F[Draw Mode]
    C --> G[Eraser Mode]
    D & E & F & G --> H[Update Presentation Screen]

🎥 Demo Illustration
Gesture → Action Mapping
+-------------+-----------------+
|   Gesture   |      Action     |
+-------------+-----------------+
| ☝️          | Draw Annotation |
| ✌️          | Pointer Mode    |
| 👆          | Previous Slide  |
| 👉          | Next Slide      |
| ✋          | Erase Drawing   |
+-------------+-----------------+


(Replace with actual screenshots/gifs if you want in the repo)

🛠️ Dependencies

OpenCV
 – Image & video processing

cvzone
 – Hand tracking wrapper

NumPy
 – Array operations

🚀 Future Improvements

Support for PPT/PDF files directly

Add multi-hand controls

Gesture customization via config file

🙌 Contributing

Pull requests are welcome! Please open an issue first to discuss what you’d like to change.
