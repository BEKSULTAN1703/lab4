import tkinter as tk

def on_click(event):
    # This function is triggered when a mouse click occurs.
    print("Mouse clicked at", event.x, event.y)

def on_motion(event):
    # This function is triggered when the mouse moves over the window.
    print("Mouse is at", event.x, event.y)

def main():
    root = tk.Tk()
    root.title("Mouse Interaction")

    # Set the window size
    root.geometry("400x300")

    # Bind mouse events to the window: left click and mouse motion
    root.bind("<Button-1>", on_click)  # Left mouse button click
    root.bind("<Motion>", on_motion)   # Mouse movement

    # Start the main event loop of the application
    root.mainloop()

if __name__ == "__main__":
    main()
