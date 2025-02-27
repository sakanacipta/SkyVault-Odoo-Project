# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    billable_time_target = fields.Float("Billing Time Target", groups="hr.group_hr_user")

    @api.model
    def get_billable_time_target(self, user_ids):
        if self.env.user.has_group("hr_timesheet.group_hr_timesheet_user"):
            return self.sudo().search_read([("user_id", 'in', user_ids)], ["billable_time_target"])

    _sql_constraints = [
        (
            "check_billable_time_target",
            "CHECK(billable_time_target >= 0)",
            "The billable time target cannot be negative."
        ),
    ]
