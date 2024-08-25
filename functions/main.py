# import firebase_admin
# from firebase_admin import messaging

# from firebase_functions.firestore_fn import (
#   on_document_created,
#   Event,
#   Change,
#   DocumentSnapshot,
# )

# firebase_admin.initialize_app()


# @on_document_created(document="chat/{messageId}")
# def myfunction(event: Event[Change[DocumentSnapshot]]) -> None:
#   text = event.data.to_dict().get("text")
#   event.data.reference.update({"text": text.upper()})
  
#   notification = messaging.Notification(
#       title="New Chat Message",
#       body='some body message', 
#   )
#   message = messaging.Message(
#     topic='chat',
#     notification=notification
#     )
  
#   response = messaging.send(message)
#   print('Successfully sent message:', response)


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
        # Extract text from document
        data = event.data.to_dict()
        if "text" not in data:
            print("Error: 'text' field not found in document.")
            return

        text = data["text"]

        # Update document with uppercase text
        event.data.reference.update({"text": text.upper()})

        # Create notification
        notification = messaging.Notification(
            title="New Chat Message",
            body='some body message',
        )

        message = messaging.Message(
            topic = 'chat',
            data = {
              'title': 'Notification Title',
              'body': 'Notification Body',
              'click_action': 'FLUTTER_NOTIFICATION_CLICK' 
            },
            # token='e1fTFxseSwW-TslfZiVC38:APA91bFlUbuK5FwH_0j-Tv0aTKqDL6s0XPkclTVrIA0mm-fYN6-4QVrjDTkFj1t1fZ10_5vFtQy5CdnikRXkcHg_DKaSaDXOKkqBa-yaMgCBOMByPh8E6ZdtzwZ1_KjdXolIetuPa-Pl'
            notification=notification,
        )

        # Send notification
        response = messaging.send(message)
        print('memo sent message:', response)
    except Exception as e:
        print(f"Error sending notification: {e}")

