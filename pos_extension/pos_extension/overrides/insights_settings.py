import frappe
from insights.insights.doctype.insights_settings.insights_settings import InsightsSettings as OriginalInsightsSettings

class CustomInsightsSettings(OriginalInsightsSettings):
    def before_save(self):
        # Check if the document exists in the database
        doc_before_save = frappe.get_doc(self.doctype, self.name)
        
        # If the document exists, doc_before_save.setup_complete will be available
        if self.setup_complete and (doc_before_save and not doc_before_save.setup_complete):
            # Your custom logic here
            pass
