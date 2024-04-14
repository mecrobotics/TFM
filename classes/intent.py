class Intent:

    clases_intencion=""
    archivo_excel = './data/train_llm.csv' 

    def __init__(self, pd):
        self.cargar_clases_intencion(pd)       
    
    # Carga las clases de intención desde el archivo Excel
    def cargar_clases_intencion(self, pd):

        df = pd.read_csv(self.archivo_excel, delimiter=';')
        # Asumiendo que tu archivo tiene una columna 'ClaseIntencion' con las clases de intención
        self.clases_intencion = df['category'].unique().tolist()
    
    # Clasifica una nueva entrada de texto según las clases de intención
    def clasificar_intencion(self, texto_entrada, openai):
        # Preparamos el prompt para la clasificación de intención
        prompt = f"Clasifica la siguiente entrada en una de las siguientes categorías: {', '.join(self.clases_intencion)}.\n\nEntrada: \"{texto_entrada}\".Responde siempre, en todos los casos, con solo una de las opciones de categoría y nada más de texto y sin punto final.Si no sabes a cual debe ir, devolver 'ninguna'"

        response = openai.chat.completions.create(
            messages=[
                {"role": "system", "content": f"Clasifica textos en las siguientes categorías: {', '.join(self.clases_intencion)}."},
                {"role": "user", "content": prompt}
            ],
            model="gpt-3.5-turbo",
        )
        respuesta = response.choices[0].message.content
        return respuesta.strip()

    def handle_card_arrival(self):
        return "Tu tarjeta debería llegar en un plazo de 7 a 10 días laborales después de tu solicitud."

    def handle_card_linking(self):
        return "card_linking"

    def handle_exchange_rate(self):
        return "Puedes consultar el tipo de cambio actual directamente en nuestra aplicación en la sección de moneda extranjera."

    def handle_card_payment_wrong_exchange_rate(self):
        return "card_payment_wrong_exchange_rate"

    def handle_extra_charge_on_statement(self):
        return "extra_charge_on_statement"

    def handle_pending_cash_withdrawal(self):
        return "pending_cash_withdrawal"

    def handle_fiat_currency_support(self):
        return "fiat_currency_support"

    def handle_card_delivery_estimate(self):
        return """Tu tarjeta debería llegar en un plazo menor a 10 días desde la solicitud. Puedes consultar su estado con un agente.
                <br><br>
                <a href='URL_DE_CONTACTO' target='_blank'>
                    <button style='color: white; background-color: #4CAF50; padding: 10px 24px; border: none; cursor: pointer; border-radius: 5px; text-align: center;'>
                        Contactar con un gestor
                    </button>
                </a>"""

    def handle_automatic_top_up(self):
        return "automatic_top_up"

    def handle_card_not_working(self):
        return "card_not_working"

    def handle_exchange_via_app(self):
        return "exchange_via_app"

    def handle_lost_or_stolen_card(self):
        return "lost_or_stolen_card"

    def handle_age_limit(self):
        return "age_limit"

    def handle_pin_blocked(self):
        return "pin_blocked"

    def handle_contactless_not_working(self):
        return "contactless_not_working"

    def handle_top_up_by_bank_transfer_charge(self):
        return "top_up_by_bank_transfer_charge"

    def handle_pending_top_up(self):
        return "pending_top_up"

    def handle_cancel_transfer(self):
        return "cancel_transfer"

    def handle_top_up_limits(self):
        return "top_up_limits"

    def handle_wrong_amount_of_cash_received(self):
        return "wrong_amount_of_cash_received"

    def handle_card_payment_fee_charged(self):
        return "card_payment_fee_charged"

    def handle_transfer_not_received_by_recipient(self):
        return "transfer_not_received_by_recipient"

    def handle_supported_cards_and_currencies(self):
        return "supported_cards_and_currencies"

    def handle_getting_virtual_card(self):
        return "getting_virtual_card"

    def handle_card_acceptance(self):
        return "card_acceptance"

    def handle_top_up_reverted(self):
        return "top_up_reverted"

    def handle_balance_not_updated_after_cheque_or_cash_deposit(self):
        return "balance_not_updated_after_cheque_or_cash_deposit"

    def handle_card_payment_not_recognised(self):
        return "card_payment_not_recognised"

    def handle_edit_personal_details(self):
        return "edit_personal_details"

    def handle_why_verify_identity(self):
        return "why_verify_identity"

    def handle_unable_to_verify_identity(self):
        return "unable_to_verify_identity"

    def handle_get_physical_card(self):
        return "get_physical_card"

    def handle_visa_or_mastercard(self):
        return "visa_or_mastercard"

    def handle_topping_up_by_card(self):
        return "topping_up_by_card"

    def handle_disposable_card_limits(self):
        return "disposable_card_limits"

    def handle_compromised_card(self):
        return "compromised_card"

    def handle_atm_support(self):
        return "atm_support"

    def handle_direct_debit_payment_not_recognised(self):
        return "direct_debit_payment_not_recognised"

    def handle_passcode_forgotten(self):
        return "passcode_forgotten"

    def handle_declined_cash_withdrawal(self):
        return "declined_cash_withdrawal"

    def handle_pending_card_payment(self):
        return "pending_card_payment"

    def handle_lost_or_stolen_phone(self):
        return "lost_or_stolen_phone"

    def handle_request_refund(self):
        return "request_refund"

    def handle_declined_transfer(self):
        return "declined_transfer"

    def handle_Refund_not_showing_up(self):
        return "Refund_not_showing_up"

    def handle_declined_card_payment(self):
        return "declined_card_payment"

    def handle_pending_transfer(self):
        return "pending_transfer"

    def handle_terminate_account(self):
        return "terminate_account"

    def handle_card_swallowed(self):
        return "card_swallowed"

    def handle_transaction_charged_twice(self):
        return "transaction_charged_twice"

    def handle_verify_source_of_funds(self):
        return "verify_source_of_funds"

    def handle_transfer_timing(self):
        return "transfer_timing"

    def handle_reverted_card_payment(self):
        return "reverted_card_payment"

    def handle_change_pin(self):
        return "change_pin"

    def handle_beneficiary_not_allowed(self):
        return "beneficiary_not_allowed"

    def handle_transfer_fee_charged(self):
        return "transfer_fee_charged"

    def handle_receiving_money(self):
        return "receiving_money"

    def handle_failed_transfer(self):
        return "failed_transfer"

    def handle_transfer_into_account(self):
        return "transfer_into_account"

    def handle_verify_top_up(self):
        return "verify_top_up"

    def handle_getting_spare_card(self):
        return "handle_getting_spare_card"

    def handle_top_up_by_cash_or_cheque(self):
        return "top_up_by_cash_or_cheque"

    def handle_order_physical_card(self):
        return "order_physical_card"

    def handle_virtual_card_not_working(self):
        return "virtual_card_not_working"

    def handle_wrong_exchange_rate_for_cash_withdrawal(self):
        return "wrong_exchange_rate_for_cash_withdrawal"

    def handle_get_disposable_virtual_card(self):
        return "get_disposable_virtual_card"

    def handle_top_up_failed(self):
        return "top_up_failed"

    def handle_balance_not_updated_after_bank_transfer(self):
        return "balance_not_updated_after_bank_transfer"

    def handle_cash_withdrawal_not_recognised(self):
        return "cash_withdrawal_not_recognised()"

    def handle_exchange_charge(self):
        return "exchange_charge"

    def handle_top_up_by_card_charge(self):
        return "top_up_by_card_charge"

    def handle_activate_my_card(self):
        return "activate_my_card"

    def handle_cash_withdrawal_charge(self):
        return "cash_withdrawal_charge"

    def handle_card_about_to_expire(self):
        return "card_about_to_expire"

    def handle_apple_pay_or_google_pay(self):
        return "apple_pay_or_google_pay"

    def handle_verify_my_identity(self):
        return "verify_my_identity"

    def handle_country_support(self):
        return "country_support"

    def handle_fallback(self):
        return "Lo siento, no entiendo tu pregunta. ¿Puedes ser más específico?"
