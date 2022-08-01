# The Center Piece File
class MManager:
    def __init__(self, accs: dict):
        self.accs = accs

    def post_on_all_accs(self, specified_values: dict):
        for account in self.accs:
            post_account(account)

    def start(self, specified_values: dict):
        print("Starting...")

    def stop(self, specified_values: dict):
        print("Stopping...")
    


def post_accs(self):




# 2 types of accs:
# 1: automated (say someone has set parameters for each account)
# 2: manual (say someone wants to post a picture on 8 different platforms...)
# However, it is possible to do both at once...

# specified_values:
"""
{
    "account_name (example manual (this is required for manual accounts))": {
        "Time_To_Post": "12:00",
        "Image": "path_to_image",
        "Caption": "caption",
        "Tags": ["tag1", "tag2", "tag3"],
        "Location": "location",
        "Comments": {
            "comment1": {
                "time": "time",
                "like": True,
                "***Deep_Comment***": {}
            }
            , "comment2", "comment3"},
        "Like": True,
    },
    "account_name (example automated (this is not required for manual accounts))": {
        "offsets_automation_time": True,
        "Time_To_Post": "12:00",
        "Image": "path_to_image",
        "Caption": "caption",
        "Tags": ["tag1", "tag2", "tag3"],
        "Location": "location",
        "Comments": {
            "comment1": {
                "time": "time",
                "like": True,
                "***Deep_Comment***": {}
            }
            , "comment2", "comment3"},
        "Like": True,
    }
}
"""