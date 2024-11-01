
# Stripe Payment Bot

This project is a Telegram bot built to handle payments through multiple providers, including Stripe and Click. It enables users to select a payment method, enter an amount, and complete the payment. The bot is built with Python and uses the `telebot` library for Telegram integration and `stripe` for payment processing.

## Table of Contents

* [Features](#features)
* [Project Structure](#project-structure)
* [Requirements](#requirements)
* [Setup Instructions](#setup-instructions)
* [Environment Variables](#environment-variables)
* [Usage](#usage)
* [Modules Explanation](#modules-explanation)
* [Contributing](#contributing)
* [License](#license)

## Features

* **Multiple Payment Methods**: Supports both Stripe and Click for handling payments.
* **Custom Amount Entry**: Users can enter the payment amount in whole currency units.
* **Inline Keyboards for User Interaction**: Users can choose payment methods via an inline keyboard.
* **Error Handling and Logging**: Includes robust error handling and logs important events for easier debugging.

## Project Structure

```markdown
stripe_payment_bot/
├── keyboards/
│   ├── __init__.py
│   └── inline.py  # Contains inline keyboard functions for payment and amount selection
├── payment/
│   ├── __init__.py
│   └── invoice.py  # Handles sending invoices via Telegram and Stripe API
├── .env  # Environment variables (not included; create your own)
├── conf.py  # Configuration file for loading environment variables and setting up logging
├── main.py  # Main bot logic, command handlers, and payment processing
├── requirements.txt  # Python dependencies
└── README.md  # Project documentation
```

## Requirements

* Python 3.7+
* Libraries:
	+ `python-telegram-bot`
	+ `stripe`
	+ `python-dotenv`
	+ `Flask` (optional, only if webhook handling is needed)

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/Nimblen/stripe_payment_bot.git
cd stripe_payment_bot
```

### Set Up Environment Variables

Create a `.env` file in the root directory with the following variables:

```makefile
BOT_TOKEN=<Your Telegram Bot Token>
CLICK_PROVIDER_TOKEN=<Your Click Provider Token>
STRIPE_PROVIDER_TOKEN=<Your Stripe Secret Key>
STRIPE_WEBHOOK_SECRET=<Your Stripe Webhook Secret (only if using webhooks)>
```

### Configure the Bot

1. In the Telegram BotFather, set up a new bot and obtain the `BOT_TOKEN`.
2. Register with Stripe and Click, and set up API tokens for each provider.
3. Run the bot by executing the following command:

```bash
python main.py
```

The bot will begin polling for updates and respond to commands.

## Environment Variables

The following environment variables are required:

* `BOT_TOKEN`: Telegram Bot token for interacting with Telegram API.
* `CLICK_PROVIDER_TOKEN`: Token for Click payment provider.
* `STRIPE_PROVIDER_TOKEN`: Secret key for Stripe API.
* `STRIPE_WEBHOOK_SECRET` (optional): Secret for verifying Stripe webhook signatures (if webhooks are used).

## Usage

### Start the Bot

Use `/start` to start interacting with the bot.

### Initiate Payment

Use `/pay` to initiate the payment process. The bot will prompt you to:

1. Select a payment method (either Click or Stripe).
2. Enter an amount in whole currency units (e.g., 10 for $10).

### Receive Invoice

After selecting a method and entering an amount, the bot will send an invoice or payment link (for Stripe).

## Modules Explanation

### `conf.py`

This module loads environment variables and configures logging. It provides easy access to configuration settings across the project.

### `main.py`

The main entry point of the bot. Contains:

* Command handlers (`/start` and `/pay`) to start and process payments.
* Logic to handle user interactions, including payment method selection and amount entry.

### `keyboards/inline.py`

Contains functions to generate inline keyboards for Telegram:

* `get_payment_keyboard()`: Displays available payment methods.
* `get_amount_keyboard()`: (Optional) Displays predefined amount options.

### `payment/invoice.py`

Handles sending invoices and payment links:

* Uses `telebot` to send messages and invoices.
* Integrates with Stripe API to generate payment sessions and links.

## Contributing

Contributions are welcome!:
