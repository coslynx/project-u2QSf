class Notifications:
    def __init__(self):
        self.notifications_enabled = True

    def enable_notifications(self):
        self.notifications_enabled = True
        return "Notifications enabled."

    def disable_notifications(self):
        self.notifications_enabled = False
        return "Notifications disabled."

    def send_notification(self, user_id, message):
        if self.notifications_enabled:
            # Code to send notification to the user with user_id using Discord API
            return f"Notification sent to user {user_id}: {message}"
        else:
            return "Notifications are currently disabled. Enable notifications to receive messages."