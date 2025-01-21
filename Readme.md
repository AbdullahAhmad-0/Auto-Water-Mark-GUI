# Auto Watermark Tool with GUI

![screenshot](https://github.com/user-attachments/assets/2f2d1c4b-295b-4506-bccb-dfd1313f3b3b)

This is a Python-based graphical user interface (GUI) application for adding watermarks to images, built with the Tkinter library. The tool is simple, intuitive, and supports both text-based and image-based watermarks.

## Features

- **Multiple Watermark Types**: 
  - Add **text watermarks** with customizable font, size, and color.
  - Add **image watermarks** by uploading your logo or other images.
  
- **Batch Processing**: 
  - Apply watermarks to individual images or entire folders of images.

- **Positioning**: 
  - Easily set the location of the watermark on the image.

- **User-Friendly Interface**:
  - Clear labels, buttons, and input fields for an effortless experience.

- **Error Handling**:
  - Built-in validation to ensure proper inputs and supported formats.

- **Multi-Format Support**:
  - Compatible with popular image formats supported by the Python Imaging Library (PIL).

## Requirements

- **Python Version**: Python 3.9.6 or higher
- **Dependencies**:
  - Install the required dependencies using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AbdullahAhmad-0/Auto-Water-Mark-GUI.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Auto-Water-Mark-GUI
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the script:
    ```bash
    python Auto WM.py
    ```

### Prebuilt Executable

A prebuilt executable is available for Windows users:
- Download the installer: [Download](https://github.com/AbdullahAhmad-0/Auto-Water-Mark-GUI/releases/latest).

## How to Use

1. **Open the App**: Launch the script or use the executable file.
2. **Load Images**: 
   - Choose a single image, multiple images, or a folder of images.
3. **Select Watermark Type**:
   - Text: Enter the text, choose the font, size, and color.
   - Image: Upload your watermark image.
4. **Position the Watermark**:
   - Select a predefined location or set custom coordinates.
5. **Save the Output**:
   - Specify the output folder to save the watermarked images.

<video controls>
  <source src="demo\Demo.mkv" type="video/mkv">
Your browser does not support the video tag.
</video>


## File Structure

- **Main Script**: Contains the core GUI and logic.
- **dist/WM-1.0-win64.msi**: Prebuilt executable installer for Windows.
- **requirements.txt**: List of Python dependencies.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements or bug fixes.

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit:
    ```bash
    git commit -m "Description of feature"
    ```
4. Push your branch and create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

### Contact

If you have questions or feedback, feel free to open an issue or contact the repository owner.

Enjoy watermarking!
