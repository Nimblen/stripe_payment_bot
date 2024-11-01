from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from conf import logger

def get_payment_keyboard() -> InlineKeyboardMarkup:
    """
    Creates an inline keyboard with payment options.

    Returns:
        InlineKeyboardMarkup: The keyboard with payment options.
    """
    logger.info("Creating payment keyboard with 'CLICK' and 'Stripe' options.")
    keyboard = [
        [
            InlineKeyboardButton("Клик", callback_data="click"),
            InlineKeyboardButton("Stripe", callback_data="stripe")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
