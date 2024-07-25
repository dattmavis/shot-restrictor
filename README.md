# Shot Restrictor

Shot Restrictor is a Python GUI application that helps create a more intentional photography experience by simulating the limitation of film. Modern SD cards have large storage capacities, which can lead to taking a large number of shots without much thought. This tool calculates and generates a dummy file to restrict the number of available shots on the SD card, encouraging a more deliberate approach to photography.

![image](https://github.com/user-attachments/assets/5baeb48d-6a5c-438a-80ad-6c5ebbfddb7d)


## Features

- **Select SD Card**: Choose the SD card or mount point where the dummy file will be created.
- **Average JPEG Size**: Input the average size of each JPEG file in megabytes.
- **Number of Shots**: Input the number of shots you want available on your SD card.
- **Generate Dummy File**: Create a dummy file to restrict the available space on your SD card.

## How to Use

1. **Download and Install**: Clone the repository and ensure you have Python installed on your system.
2. **Run the Application**: Execute the `shot_restrictor.py` script using Python.
3. **Select SD Card**: Browse to select the path of your SD card or enter it manually.
4. **Enter Average JPEG Size**: Input the average size of each JPEG file in megabytes.
5. **Enter Number of Shots**: Input the number of shots you want available.
6. **Generate**: Click the "Generate" button to create the dummy file and restrict the available space on your SD card.

## Requirements

- Python 3.x
- `tkinter` library

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/shot-restrictor.git
    cd shot-restrictor
    ```

2. **Run the application**:
    ```sh
    python shot_restrictor.py
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
