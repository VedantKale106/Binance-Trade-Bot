# 📈 Binance Spot Trading Bot (Flask + Binance API)

This sophisticated **Flask-based web application** offers a robust platform for executing **market**, **limit**, and **stop-limit** orders exclusively on the **Binance Spot Testnet**. Leveraging the official Binance API, this tool provides a secure and intuitive environment for simulated trading activities.

-----

## 🔒 Important Notice

This application is strictly designed for use with the Binance **Spot Testnet** for development and testing purposes only. It is **not intended for real trading** with actual funds.

-----

## ✨ Key Features

  * **Diverse Order Types**: Seamlessly place **Market**, **Limit**, and **Stop-Limit** orders.
  * **Bid/Ask Support**: Facilitates both **Buy** and **Sell** operations.
  * **Enhanced Security**: Employs `.env` files for secure handling of API keys, ensuring credentials are not exposed in the codebase.
  * **Robust Input Validation**: Implements client-side and server-side validation to ensure accurate order parameters before API submission.
  * **Comprehensive Logging**: Detailed logging of all order placements and potential errors for easy monitoring and debugging.
  * **User-Friendly Interface**: Built with Flask and Bootstrap, offering a simple yet effective user experience.

-----

## 📸 Visual Overview

### ⚙️ Order Placement Interface
![Image](https://github.com/user-attachments/assets/84cba38a-4e36-4873-8375-f59aedfe6418)
![Image](https://github.com/user-attachments/assets/7c00e436-b170-4f0f-8c92-34531b62318d)

-----

## 🛠️ Technology Stack

  * **Backend**: Python (Flask Framework)
  * **Binance API Integration**: `python-binance` library
  * **Frontend**: HTML5, CSS3 (Bootstrap Framework)
  * **Logging Management**: Python's built-in `logging` module
  * **Environment Variable Management**: `python-dotenv`

-----

## 📂 Project Structure

```
project/
│
├── app.py
├── spot_bot.py
├── .env                 # Stores Binance API credentials (excluded from version control)
├── requirements.txt
├── templates/
│   └── index.html
└── README.md
```

-----

## ⚙️ Configuration

### `.env` File Setup

To ensure secure access to the Binance Spot Testnet, create a `.env` file in the project root with the following format, replacing the placeholders with your actual API credentials:

```env
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

-----

## 🚀 Getting Started

### Installation

To set up the project locally, follow these steps:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# Create and activate a virtual environment (highly recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the required dependencies
pip install -r requirements.txt
```

### Running the Application Locally

Once the dependencies are installed, you can launch the Flask application:

```bash
python app.py
```

Open your web browser and navigate to `http://127.0.0.1:5000` to access the trading bot interface.

### Deployment on GitHub

To deploy your project to GitHub, execute the following commands:

```bash
# Initialize a Git repository
git init

# Exclude the .env file from version control
echo ".env" > .gitignore

# Add all project files to the staging area
git add .

# Commit your changes
git commit -m "Initial commit"

# Link to your GitHub repository (replace with your actual repository URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push your local commits to GitHub
git push -u origin main
```

-----

## 🌐 Live Demo 

Not deployed due to some technical issue

-----

We welcome contributions and feedback to enhance this project. Feel free to open issues or pull requests on the GitHub repository.
