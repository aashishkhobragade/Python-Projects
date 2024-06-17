import tkinter as tk
from tkinter import font, filedialog
from PIL import Image, ImageTk
import cv2
import pytesseract

# Set the path to Tesseract-OCR executable
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# Function to upload and display a new image
def upload_image():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", ".png")])
    if file_path:
        # Load and resize the new image
        new_image = Image.open(file_path)
        new_image = new_image.resize((300, 300), Image.ADAPTIVE)
        new_photo = ImageTk.PhotoImage(new_image)
        # Update the image label with the new image
        image_label.config(image=new_photo)
        image_label.image = new_photo  # Keep a reference to avoid garbage collection

# Function to perform OCR on the selected image
def perform_ocr():
    global file_path
    if not file_path:
        return
    
    img = cv2.imread(file_path)
    
    # Preprocessing steps
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    # Process each contour and perform OCR
    recognized_text = ""
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cropped = img[y:y + h, x:x + w]
        text = pytesseract.image_to_string(cropped)
        recognized_text += text + "\n"
    
    # Display the recognized text in the text widget
    text_output.config(state=tk.NORMAL)
    text_output.delete('1.0', tk.END)
    text_output.insert(tk.END, recognized_text)
    text_output.config(state=tk.DISABLED)

# Define color variables
color1 = '#FFA62F'
color2 = '#FFC96F'

# Create the main window
root = tk.Tk()
root.title("Image to Text Converter")

# Define the dimensions of the window
root.geometry("900x600")

# Disable window resizing
root.resizable(False, False)

# Create the first container (frame) and set its background color
frame1 = tk.Frame(root, bg=color1, width=300, height=600)
frame1.pack(side='left', fill='both', expand=True)

title_font = font.Font(family='Helvetica', size=20)
# Create a label instructing the user to upload an image
label_upload = tk.Label(frame1, text="Upload Image here", bg=color1, font=title_font)
label_upload.pack(pady=10)

# Load the initial image
image = Image.open('image.png')  # Replace with the path to your initial image
image = image.resize((300, 300), Image.ADAPTIVE)
photo = ImageTk.PhotoImage(image)

# Create a Label widget to display the image
image_label = tk.Label(frame1, image=photo)
image_label.pack(padx=30, pady=20)

# Create an "Upload Image" button below the image
upload_button = tk.Button(frame1, text="Upload Image", command=upload_image , font=title_font)
upload_button.pack(padx=20, pady=20)
btn_ocr = tk.Button(frame1, text="Perform OCR", command=perform_ocr, font=title_font)
btn_ocr.pack(pady=10)

# Create the second container (frame) and set its background color
frame2 = tk.Frame(root, bg=color2, width=600, height=600)
frame2.pack(side='left', fill='both', expand=True)

label_text = tk.Label(frame2, text="Extracted Text from Image", bg=color2, font=title_font)
label_text.pack(pady=8)

# Text widget to display OCR output
text_output = tk.Text(frame2, wrap=tk.WORD, state=tk.DISABLED, font=title_font)
text_output.pack(padx=40, pady=40)

# Button to trigger OCR

# Start the Tkinter event loop
root.mainloop()

