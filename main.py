import logging
from telebot import TeleBot, types
from conf import BOT_TOKEN, logger
from keyboards.inline import get_payment_keyboard
from payment.invoice import send_invoice

bot = TeleBot(BOT_TOKEN)

# Dictionary to store the selected payment method for each user
user_payment_method = {}

@bot.message_handler(commands=['start'])
def start_command(message):
    """
    Handle the start command by sending a welcome message and instructions.
    """
    logger.info(f"Received start command from chat_id {message.chat.id}")
    bot.send_message(message.chat.id, "Добро пожаловать! Используйте команду /pay для начала процесса оплаты.")

@bot.message_handler(commands=['pay'])
def pay_command(message):
    """
    Handle the /pay command by sending the payment method keyboard.
    """
    chat_id = message.chat.id
    logger.info(f"Received pay command from chat_id {chat_id}")
    
    # Prompt the user to choose a payment method
    bot.send_message(chat_id, "Выберите способ оплаты:", reply_markup=get_payment_keyboard())

@bot.callback_query_handler(func=lambda call: call.data in ["click", "stripe"])
def handle_payment_selection(call):
    """
    Handles the payment method selection and prompts for the amount.
    """
    method = call.data
    chat_id = call.message.chat.id
    logger.info(f"User selected {method} payment method in chat_id {chat_id}")

    # Store the selected payment method for this user
    user_payment_method[chat_id] = method
    
    # Prompt the user to enter an amount manually
    bot.send_message(chat_id, "Введите сумму для оплаты")

@bot.message_handler(func=lambda message: message.chat.id in user_payment_method)
def handle_amount_input(message):
    """
    Handles the amount input from the user, validates it, and sends the invoice.
    """
    chat_id = message.chat.id
    amount_text = message.text.strip()
    
    # Validate the amount input
    if not amount_text.isdigit():
        bot.send_message(chat_id, "Пожалуйста, введите корректное числовое значение.")
        return
    
    amount = int(amount_text) * 100  
    
    # Retrieve the stored payment method for this user
    method = user_payment_method.pop(chat_id, None)  # Remove the method after retrieving

    if method:
        logger.info(f"User entered amount {amount} for payment method {method} in chat_id {chat_id}")
        send_invoice(bot, chat_id, method, amount)
    else:
        logger.error(f"No payment method selected for chat_id {chat_id}")
        bot.send_message(chat_id, "Произошла ошибка: не выбран метод оплаты. Пожалуйста, начните сначала с команды /pay.")

if __name__ == "__main__":
    logger.info("Starting bot polling.")
    bot.polling(none_stop=True)
