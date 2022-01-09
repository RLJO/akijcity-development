odoo.define('ibos_sms_integration_sslwireless.send_sms', function (require) {
    "use strict";

    var core = require('web.core');
    var gui = require('point_of_sale.gui');
    var rpc = require('web.rpc');
    var ScreenWidget = require('point_of_sale.screens').ReceiptScreenWidget;

    var _t = core._t;

    ScreenWidget.include({
        get_receipt_render_env: function() {
            var node = this._super.apply(this, arguments);
            if (node.order.attributes.client) {
                var paymentlines = node.receipt.paymentlines;
                var credit = node.order.amount_due;

                if (paymentlines.length > 0){
                    var total_amount = node.receipt.total_rounded
                    var paid_amount = 0;
                    for (var i=0; i < paymentlines.length; i++){
                        paid_amount = paymentlines[i].amount
                    }
                    credit = total_amount - paid_amount;
                }
                const client = {
                    'id': node.order.attributes.client.id,
                    'name': node.order.attributes.client.name,
                    'mobile': node.order.attributes.client.mobile,
                    'receipt_no': node.order.uid,
                    'credit': credit
                }
                var paymentline = {}
                var mrp = rpc.query({
                    model: 'send.sms.notification',
                    method: 'send_sms_to_customer',
                    args: [client, paymentlines],
                }).then(function (result) {

                });
            }
            return node
        }
    });
});