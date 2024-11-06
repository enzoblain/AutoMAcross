# Moving Average Crossover Trading Bot

This project is a Python-based trading automation bot that uses a **Moving Average Crossover** strategy to analyze financial data and make trading decisions. The bot monitors the market, identifies trading signals when short-term and long-term moving averages cross, and executes trades accordingly.

## Project Structure

- **main.py**: The main script that runs the trading bot, managing data retrieval, crossover detection, and order execution.
- **requirements.txt**: A list of all Python packages required to run this project.

## Features

- **Moving Average Crossover Strategy**: Implements a simple yet effective strategy that signals buy or sell based on the crossover of short and long-term moving averages.
- **Automated Trading**: Executes trades automatically based on real-time crossover signals.
- **Customizable Parameters**: Allows customization of moving average lengths and other parameters to adjust the strategy to different market conditions.

## Installation

To get started with this project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/enzoblain/AutoMAcross.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd AutoMAcross
   ```

3. **Install the required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API Key:**

   This project requires an API key from [Twelve Data](https://twelvedata.com/) to access financial data. Create a `.env` file in the root directory and add your API key as follows:

   ```env
   TWELVE_DATA_API_KEY=your_api_key_here
   ```

   Replace `your_api_key_here` with your actual Twelve Data API key, which you can obtain by signing up at [Twelve Data](https://twelvedata.com/).

## Usage

To run the bot, use the following command:

```bash
python main.py
```

### Configuration

You can modify parameters like the lengths of the moving averages and trading frequency directly in `main.py` to customize the strategy for different market conditions.

## Contributing

Contributions are welcome! To contribute:

1. **Fork the repository.**
2. **Create a new branch** for your feature or fix.
3. **Commit your changes** to your branch.
4. **Push to your forked repository.**
5. **Submit a pull request** detailing your changes.

## Contact

For questions or feedback, please reach out:

- **Enzo Blain** - [blenzodu57@gmail.com](mailto:blenzodu57@gmail.com)
- **GitHub** - [https://github.com/enzoblain](https://github.com/enzoblain)

## Acknowledgements

Thanks to the open-source community and contributors for the tools and libraries that made this project possible.