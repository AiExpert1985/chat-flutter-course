import firebase_admin
from firebase_admin import messaging

from firebase_functions.firestore_fn import (
    on_document_created,
    Event,
    Change,
    DocumentSnapshot,
)

firebase_admin.initialize_app()


@on_document_created(document="chat/{messageId}")
def myfunction(event: Event[Change[DocumentSnapshot]]) -> None:
    try:
        # Hamandi: below code to achive operation based on event
        data = event.data.to_dict()
        if "text" not in data:
            print("Error: 'text' field not found in document.")
            return

        text = data["text"]

        event.data.reference.update({"text": text.upper()})

        # Hamandi: below code to send notification to user in the chat group
        notification = messaging.Notification(
            title="New Chat Message",
            body='some body message',
        )

        message = messaging.Message(
            token = None,
            topic = 'chat',
            notification = notification,
            data = {
              'title': 'Notification Title',
              'body': 'Notification Body',
              'click_action': 'FLUTTER_NOTIFICATION_CLICK' 
            },
        )
        
        response = messaging.send(message)
        print('memo sent message:', response)
    except Exception as e:
        print(f"Error sending notification: {e}")

