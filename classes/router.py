class Router:
    intention = ""
    intentions_to_functions = {}

    def __init__(self, intention):

        self.intention = intention
        # Mapeo de intenciones a funciones
        self.intentions_to_functions = {
            'card_arrival': self.intention.handle_card_arrival,
            'card_linking': self.intention.handle_card_linking,
            'exchange_rate': self.intention.handle_exchange_rate,
            'card_payment_wrong_exchange_rate':self.intention.handle_card_payment_wrong_exchange_rate,
            'extra_charge_on_statement':self.intention.handle_extra_charge_on_statement,
            'pending_cash_withdrawal':self.intention.handle_pending_cash_withdrawal,
            'fiat_currency_support':self.intention.handle_fiat_currency_support,
            'card_delivery_estimate':self.intention.handle_card_delivery_estimate,
            'automatic_top_up':self.intention.handle_automatic_top_up,
            'card_not_working':self.intention.handle_card_not_working,
            'exchange_via_app':self.intention.handle_exchange_via_app,
            'lost_or_stolen_card':self.intention.handle_lost_or_stolen_card,
            'age_limit':self.intention.handle_age_limit,
            'pin_blocked':self.intention.handle_pin_blocked,
            'contactless_not_working':self.intention.handle_contactless_not_working,
            'top_up_by_bank_transfer_charge':self.intention.handle_top_up_by_bank_transfer_charge,
            'pending_top_up':self.intention.handle_pending_top_up,
            'cancel_transfer':self.intention.handle_cancel_transfer,
            'top_up_limits':self.intention.handle_top_up_limits,
            'wrong_amount_of_cash_received':self.intention.handle_wrong_amount_of_cash_received,
            'card_payment_fee_charged':self.intention.handle_card_payment_fee_charged,
            'transfer_not_received_by_recipient':self.intention.handle_transfer_not_received_by_recipient,
            'supported_cards_and_currencies':self.intention.handle_supported_cards_and_currencies,
            'getting_virtual_card':self.intention.handle_getting_virtual_card,
            'card_acceptance':self.intention.handle_card_acceptance,
            'top_up_reverted':self.intention.handle_top_up_reverted,
            'balance_not_updated_after_cheque_or_cash_deposit':self.intention.handle_balance_not_updated_after_cheque_or_cash_deposit,
            'card_payment_not_recognised':self.intention.handle_card_payment_not_recognised,
            'edit_personal_details':self.intention.handle_edit_personal_details,
            'why_verify_identity':self.intention.handle_why_verify_identity,
            'unable_to_verify_identity':self.intention.handle_unable_to_verify_identity,
            'get_physical_card':self.intention.handle_get_physical_card,
            'visa_or_mastercard':self.intention.handle_visa_or_mastercard,
            'topping_up_by_card':self.intention.handle_topping_up_by_card,
            'disposable_card_limits':self.intention.handle_disposable_card_limits,
            'compromised_card':self.intention.handle_compromised_card,
            'atm_support':self.intention.handle_atm_support,
            'direct_debit_payment_not_recognised':self.intention.handle_direct_debit_payment_not_recognised,
            'passcode_forgotten':self.intention.handle_passcode_forgotten,
            'declined_cash_withdrawal':self.intention.handle_declined_cash_withdrawal,
            'pending_card_payment':self.intention.handle_pending_card_payment,
            'lost_or_stolen_phone':self.intention.handle_lost_or_stolen_phone,
            'request_refund':self.intention.handle_request_refund,
            'declined_transfer':self.intention.handle_declined_transfer,
            'Refund_not_showing_up':self.intention.handle_Refund_not_showing_up,
            'declined_card_payment':self.intention.handle_declined_card_payment,
            'pending_transfer':self.intention.handle_pending_transfer,
            'terminate_account':self.intention.handle_terminate_account,
            'card_swallowed':self.intention.handle_card_swallowed,
            'transaction_charged_twice':self.intention.handle_transaction_charged_twice,
            'verify_source_of_funds':self.intention.handle_verify_source_of_funds,
            'transfer_timing':self.intention.handle_transfer_timing,
            'reverted_card_payment':self.intention.handle_reverted_card_payment,
            'change_pin':self.intention.handle_change_pin,
            'beneficiary_not_allowed':self.intention.handle_beneficiary_not_allowed,
            'transfer_fee_charged':self.intention.handle_transfer_fee_charged,
            'receiving_money':self.intention.handle_receiving_money,
            'failed_transfer':self.intention.handle_failed_transfer,
            'transfer_into_account':self.intention.handle_transfer_into_account,
            'verify_top_up':self.intention.handle_verify_top_up,
            'getting_spare_card':self.intention.handle_getting_spare_card,
            'top_up_by_cash_or_cheque':self.intention.handle_top_up_by_cash_or_cheque,
            'order_physical_card':self.intention.handle_order_physical_card,
            'virtual_card_not_working':self.intention.handle_virtual_card_not_working,
            'wrong_exchange_rate_for_cash_withdrawal':self.intention.handle_wrong_exchange_rate_for_cash_withdrawal,
            'get_disposable_virtual_card':self.intention.handle_get_disposable_virtual_card,
            'top_up_failed':self.intention.handle_top_up_failed,
            'balance_not_updated_after_bank_transfer':self.intention.handle_balance_not_updated_after_bank_transfer,
            'cash_withdrawal_not_recognised':self.intention.handle_cash_withdrawal_not_recognised,
            'exchange_charge':self.intention.handle_exchange_charge,
            'top_up_by_card_charge':self.intention.handle_top_up_by_card_charge,
            'activate_my_card':self.intention.handle_activate_my_card,
            'cash_withdrawal_charge':self.intention.handle_cash_withdrawal_charge,
            'card_about_to_expire':self.intention.handle_card_about_to_expire,
            'apple_pay_or_google_pay':self.intention.handle_apple_pay_or_google_pay,
            'verify_my_identity':self.intention.handle_verify_my_identity,
            'country_support':self.intention.handle_country_support

        }
     

    def smart_routing(self, intencion):
        # Obtener la función basada en la intención y llamarla, o llamar a handle_fallback si la intención no es reconocida
        return self.intentions_to_functions.get(intencion, self.intention.handle_fallback)()