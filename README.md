# Wojak Meme Generator

This project allows users to create Wojak memes by selecting a Wojak image and adding text to the top, center, and bottom of the image. The application is built using Flask for the backend and HTML/CSS/JavaScript for the frontend.

## Features

- **Image Selection**: Users can select from a set of pre-uploaded Wojak images.
- **Text Input**: Users can add text to the top, center, and bottom of the selected image.
- **Meme Generation**: The application generates a Wojak meme based on user input and displays it.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.
- Git installed on your machine.

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/wojak-meme-generator.git
    cd wojak-meme-generator
    ```

2. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```bash
    python app.py
    ```

4. **Access the Application**:
    Open your web browser and go to:
    ```
    http://127.0.0.1:5000/
    ```

## Adding Wojak Images

1. **Upload Wojak Images**:
    - Place 30 Wojak images in the `static/images` folder.
    - Ensure the images are named `wojak1.jpg`, `wojak2.jpg`, ..., `wojak30.jpg`.

2. **Commit and Push Changes**:
    ```bash
    git add static/images/
    git commit -m "Added Wojak images"
    git push
    ```

## Usage

1. **Select an Image**:
    - Choose a Wojak image from the dropdown menu on the homepage.

2. **Enter Text**:
    - Enter text in the fields for top, center, and bottom text.

3. **Generate Meme**:
    - Click the "Generate Meme" button.

4. **View Meme**:
    - The generated Wojak meme will be displayed below the form.

## Contributing

Contributions are welcome! To contribute to this project, follow these steps:

1. **Fork the Repository**:
    - Click the "Fork" button on the GitHub repository page.

2. **Clone Your Fork**:
    ```bash
    git clone https://github.com/yourusername/wojak-meme-generator.git
    cd wojak-meme-generator
    ```

3. **Create a New Branch**:
    ```bash
    git checkout -b feature/your-feature-name
    ```

4. **Make Changes**:
    - Make your changes and commit them:
    ```bash
    git add .
    git commit -m "Describe your changes"
    ```

5. **Push Changes**:
    ```bash
    git push origin feature/your-feature-name
    ```

6. **Create a Pull Request**:
    - Go to your forked repository on GitHub and click "New Pull Request".
    - Fill out the pull request form and submit it.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
