import 'package:flutter/material.dart';
import 'package:charts_flutter/flutter.dart' as charts;
import '../screens/home_screen.dart';

class DiagnosticChart extends StatelessWidget {
  final List<DiagnosticData> data;

  const DiagnosticChart({Key? key, required this.data}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    List<charts.Series<DiagnosticData, DateTime>> series = [
      charts.Series<DiagnosticData, DateTime>(
        id: 'Diagnostic',
        colorFn: (_, __) => charts.MaterialPalette.teal.shadeDefault,
        domainFn: (DiagnosticData d, _) => d.timestamp,
        measureFn: (DiagnosticData d, _) => d.value,
        data: data,
      ),
    ];

    return charts.TimeSeriesChart(
      series,
      animate: true,
      dateTimeFactory: const charts.LocalDateTimeFactory(),
      behaviors: [
        charts.ChartTitle('Time', behaviorPosition: charts.BehaviorPosition.bottom),
        charts.ChartTitle('Value', behaviorPosition: charts.BehaviorPosition.start),
      ],
    );
  }
}
