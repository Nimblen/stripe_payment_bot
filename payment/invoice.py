from telebot import TeleBot
from telebot.types import LabeledPrice
import stripe
from conf import CLICK_PROVIDER_TOKEN, STRIPE_PROVIDER_TOKEN, logger

stripe.api_key = STRIPE_PROVIDER_TOKEN

def send_invoice(bot: TeleBot, chat_id: int, method: str, amount: int) -> None:
    """
    Sends an invoice with the specified amount based on the chosen payment method.

    Parameters:
        bot (TeleBot): Bot instance for sending messages.
        chat_id (int): ID of the chat where the invoice will be sent.
        method (str): Payment method, either 'click' or 'stripe'.
        amount (int): Amount in the smallest currency units (e.g., cents for USD).
    """
    title = "Оплата за продукт"
    description = "Описание продукта или услуги"
    payload = "Custom-Payload"
    currency = "USD"
    logger.info(f"Preparing to send invoice for {method} with amount {amount}.")

    try:
        if method == "click":
            logger.info("Using CLICK payment method.")
            prices = [LabeledPrice(label="Цена", amount=amount)]
            bot.send_invoice(
                chat_id=chat_id,
                title=title,
                description=description,
                invoice_payload=payload,
                provider_token=CLICK_PROVIDER_TOKEN,
                currency='UZS',
                prices=prices,
                start_parameter="payment-start"
            )
            logger.info(f"Invoice sent via CLICK for chat_id: {chat_id}.")

        elif method == "stripe":
            logger.info("Using Stripe payment method.")
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[{
                    "price_data": {
                        "currency": currency,
                        "unit_amount": amount,
                        "product_data": {
                            "name": title,
                            "description": description
                        }
                    },
                    "quantity": 1
                }],
                mode="payment",
                success_url="https://t.me/Nimblen_bot/",
                cancel_url="https://t.me/Nimblen_bot/",
            )
            bot.send_message(chat_id=chat_id, text=f"Ссылка на оплату через Stripe: {session.url}")
            logger.info(f"Stripe payment link sent to chat_id: {chat_id}. URL: {session.url}")

        else:
            logger.error(f"Unsupported payment method: {method}")
            raise ValueError(f"Unsupported payment method: {method}")

    except Exception as e:
        logger.error(f"Failed to send invoice for chat_id {chat_id}: {e}", exc_info=True)
        bot.send_message(chat_id=chat_id, text="Произошла ошибка при создании инвойса. Пожалуйста, попробуйте позже.")
