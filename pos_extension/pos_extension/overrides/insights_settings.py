import frappe
from insights.insights.doctype.insights_settings.insights_settings import InsightsSettings

def custom_before_save(self):
    try:
        # Fetch the existing document from the database if it exists
        doc_before_save = frappe.get_doc(self.doctype, self.name)

        # If the document is not new and setup_complete is being changed
        if self.setup_complete and (doc_before_save and not doc_before_save.setup_complete):
            # Your custom logic here
            pass

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Custom Insights Settings Error")
        frappe.throw(_("An error occurred while saving Insights Settings: {0}").format(str(e)))

# Override the before_save method
InsightsSettings.before_save = custom_before_save