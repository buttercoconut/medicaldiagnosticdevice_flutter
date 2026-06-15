import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'services/api_service.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(const MedicalDiagnosticApp());
}

class MedicalDiagnosticApp extends StatelessWidget {
  const MedicalDiagnosticApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        Provider<ApiService>(create: (_) => ApiService()),
      ],
      child: MaterialApp(
        title: 'Medical Diagnostic Device',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: const HomeScreen(),
      ),
    );
  }
}