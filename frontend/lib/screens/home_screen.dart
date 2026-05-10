import 'package:flutter/material.dart';
import '../widgets/diagnostic_chart.dart';
import '../services/api_service.dart';
import 'package:provider/provider.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  late Future<List<DiagnosticData>> _futureData;

  @override
  void initState() {
    super.initState();
    _futureData = context.read<ApiService>().fetchDiagnosticData();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Diagnostic Overview'),
      ),
      body: FutureBuilder<List<DiagnosticData>>(
        future: _futureData,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }
          if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          }
          final data = snapshot.data ?? [];
          return Padding(
            padding: const EdgeInsets.all(16.0),
            child: DiagnosticChart(data: data),
          );
        },
      ),
    );
  }
}

class DiagnosticData {
  final DateTime timestamp;
  final double value;

  DiagnosticData({required this.timestamp, required this.value});
}
