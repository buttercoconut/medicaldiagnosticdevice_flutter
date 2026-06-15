import 'package:flutter/material.dart';
import 'package:charts_flutter/flutter.dart' as charts;
import '../services/api_service.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Medical Diagnostic Device'),
      ),
      body: const Center(
        child: Text('Welcome to the Medical Diagnostic Device App'),
      ),
    );
  }
}