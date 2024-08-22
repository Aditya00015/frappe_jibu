import frappe
from frappe import _

from insights.insights.doctype.insights_settings.insights_settings import InsightsSettings

class CustomInsightsSettings(InsightsSettings):
    def before_save(self):
        try:
            # Custom logic before save
            doc_before_save = frappe.get_doc(self.doctype, self.name)
            if self.setup_complete and (doc_before_save and not doc_before_save.setup_complete):
                pass
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Custom Insights Settings Error")
            frappe.throw(_("An error occurred while saving Insights Settings: {0}").format(str(e)))
