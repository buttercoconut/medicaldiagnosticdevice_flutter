import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../services/api_service.dart';
import '../widgets/diagnostic_chart.dart';
import 'package:charts_flutter/flutter.dart' as charts;

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  late Future<List<dynamic>> _futureData;

  @override
  void initState() {
    super.initState();
    _futureData = context.read<ApiService>().fetchDiagnosticData('patient123');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Diagnostic Dashboard')),
      body: FutureBuilder<List<dynamic>>(
        future: _futureData,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }
          if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          }
          final data = snapshot.data ?? [];
          final series = [
            charts.Series<dynamic, DateTime>(
              id: 'HeartRate',
              domainFn: (datum, _) => DateTime.parse(datum['timestamp'] as String),
              measureFn: (datum, _) => datum['heartRate'] as num,
              data: data,
            ),
          ];
          return Padding(
            padding: const EdgeInsets.all(16.0),
            child: DiagnosticChart(seriesList: series, animate: true),
          );
        },
      ),
    );
  }
}
