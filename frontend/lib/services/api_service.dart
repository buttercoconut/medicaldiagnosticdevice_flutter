import 'dart:convert';
import 'package:http/http.dart' as http;
import '../screens/home_screen.dart';

class ApiService {
  final String baseUrl = 'http://localhost:8000/api';

  Future<List<DiagnosticData>> fetchDiagnosticData() async {
    final response = await http.get(Uri.parse('$baseUrl/diagnostics'));
    if (response.statusCode == 200) {
      final List<dynamic> jsonList = jsonDecode(response.body);
      return jsonList
          .map((e) => DiagnosticData(
                timestamp: DateTime.parse(e['timestamp'] as String),
                value: (e['value'] as num).toDouble(),
              ))
          .toList();
    } else {
      throw Exception('Failed to load diagnostics');
    }
  }
}
