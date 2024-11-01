from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

# Bot settings
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Payment provider tokens
CLICK_PROVIDER_TOKEN = os.getenv("CLICK_PROVIDER_TOKEN")
STRIPE_PROVIDER_TOKEN = os.getenv("STRIPE_PROVIDER_TOKEN")

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("PaymentBot")
