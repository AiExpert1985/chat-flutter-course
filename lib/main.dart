import 'package:demo/screen/auth.dart';
import 'package:demo/screen/chat.dart';
import 'package:demo/screen/splash.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';

void main() async {
  // print('.........................Main..........................');
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  runApp(
    MaterialApp(
      home: StreamBuilder(
        stream: FirebaseAuth.instance.authStateChanges(),
        builder: (ctx, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const SplashScreen();
          }
          if (snapshot.hasData) {
            // FirebaseAuth.instance.signOut();
            // print('singned bout');
            return const ChatScreen();
          }

          return const AuthScreen();
        },
      ),
    ),
  );
}
