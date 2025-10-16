"""
Example usage of the WeChat Work API client.
"""

from weixin_work import WeChatWorkClient, Config

# Initialize the client with configuration
# You can either pass config directly or let it load from .env file
config = Config()  # This will load from .env file if present
client = WeChatWorkClient(config=config)

test_user_id = "test_user"
test_phone_number = "13800000000"
test_biz_mail_alias = ["test_alias1@domain.com", "test_alias2@domain.com"]


# Example: Get user information
try:
    user_info = client.get_user(test_user_id)
    print("User Info:", user_info)
except Exception as e:
    print(f"Error getting user: {e}")

# # Example: Update user information
try:
    result = client.update_user(
        userid=test_user_id,
        biz_mail_alias={
            "item": test_biz_mail_alias
        },
    )
    print("Update Result:", result)
except Exception as e:
    print(f"Error updating user: {e}")

# Example: Convert mobile to userid
try:
    userid_result = client.mobile_to_userid(test_phone_number)
    print("User ID:", userid_result.get('userid'))
except Exception as e:
    print(f"Error getting userid: {e}")