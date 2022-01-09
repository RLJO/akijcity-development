from odoo import fields, models, api
import requests
import json

class SendSms(models.Model):
    _name = "send.sms.notification"

    @api.model
    def send_sms_to_customer(self, client=False, paymentlines=False):
        print("client:", client)
        if client:
            payment_lines_dict = dict(paymentlines)
            payment_line = ""
            for line in paymentlines:
                payment_line += str(line['payment_method']) + ":" + str(float(line['amount'])) + " "

            partner_id = client['id']
            res_partner = self.env['res.partner'].search([('id', '=', partner_id)])
            credit_limit = res_partner.employess_id.credit_limit


            current_credit = client['credit']

            #previous credit
            pos_order = self.env['pos.order'].search([('partner_id', '=', partner_id)])
            credit_sum = sum(pos_order.mapped('amount_due'))

            credit_payment = self.env['customer.credit.payment.line'].search([('partner_id', '=', partner_id)])
            payment_sum = sum(credit_payment.mapped('amount'))
            previous_credit = credit_sum - payment_sum
            total_credit = current_credit + previous_credit
            remaining_credit = credit_limit - total_credit

            msg = "Dear "+ client['name'] +", Thanks purchase from The Daily City Bazar. Invoice:" + client['receipt_no'] +", "+ payment_line +" Credit: Current "+ \
                  str(float("{:.2f}".format(current_credit))) +" Previous "+ str(float("{:.2f}".format(previous_credit)))+" Total "+ \
                  str(float("{:.2f}".format(total_credit)))+" Remaining "+ str(float("{:.2f}".format(remaining_credit))) +"  and Limit " + str(credit_limit)

            print("msg:", msg)

            mobile = client['mobile']
            if mobile:
                url = "https://smsplus.sslwireless.com/api/v3/send-sms?api_token=akijgroupadmin-abfd7bb4-2148-4ecd-81f8-295522b001f8&sid=CALLALADDIN&sms="+msg+"&msisdn="+mobile+"&csms_id=4473433434pZ684333392"
                payload = {}
                headers = {}
                response = requests.request("GET", url, headers=headers, data=payload)

                print(response.text)
                print(type(response.text))
                json_response = json.loads(response.text)
                sms_info = json_response['smsinfo']
                print("sms_info:", sms_info, type(sms_info))
                message = sms_info[0]['sms_body']
                mobile = sms_info[0]['msisdn']
                status = sms_info[0]['status_message']
                reference_id = sms_info[0]['reference_id']
                error_msg = json_response['error_message']
                response = response.text

                self.env['sms.notification.history'].create({
                    'message': message,
                    'mobile': mobile,
                    'status': status,
                    'reference_id': reference_id,
                    'error_msg': error_msg,
                    'response': response
                })
