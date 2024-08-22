import 'package:demo/screen/widgets/chat_messages.dart';
import 'package:demo/screen/widgets/new_message.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';

class ChatScreen extends StatefulWidget {
  const ChatScreen({super.key});

  @override
  State<ChatScreen> createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
// here we added a helper method because it is recommended to no use async in initState()
  void setupPushNotifications() async {
    final fcm = FirebaseMessaging.instance;
    // ask user for permission
    await fcm.requestPermission();
    // address of the device that you need to target this device, which you can send to a backend & use it later
    final token = await fcm.getToken();
    print(token);
  }

  // here we ask for permission from the device
  // to send push notificaiton, because it runs once only
  @override
  void initState() {
    super.initState();
    setupPushNotifications();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        actions: [
          IconButton(
              onPressed: () {
                FirebaseAuth.instance.signOut();
              },
              icon: Icon(Icons.exit_to_app,
                  color: Theme.of(context).colorScheme.primary))
        ],
        title: const Text('FlutterChat'),
      ),
      body: const Column(
        children: [
          Expanded(child: ChatMessages()),
          NewMessage(),
        ],
      ),
    );
  }
}
