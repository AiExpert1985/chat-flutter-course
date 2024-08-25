import firebase_admin

from firebase_functions.firestore_fn import (
  on_document_created,
  Event,
  Change,
  DocumentSnapshot,
)


firebase_admin.initialize_app()

@on_document_created(document="chat/{messageId}")
def myfunction(event: Event[Change[DocumentSnapshot]]) -> None:
  # Get the current and previous document values.
  text = new_value = event.data.to_dict().get("text")
  event.data.reference.update({"text": text.upper()})