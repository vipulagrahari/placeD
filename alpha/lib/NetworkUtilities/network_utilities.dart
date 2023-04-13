// ignore: file_names
import 'package:http/http.dart' as http;
import 'dart:convert';

class NetworkUtils {
  Future<List<dynamic>> getData() async {
    // var headers = {
    //   'Content-Type': 'application/json',
    // };

    final response = await http
        .get(Uri.parse("https://palaceD.vipulagrahari.repl.co/api/get/all"));

    if (response.statusCode == 200) {
      String data = response.body;
      var decodedData = jsonDecode(data);

      return decodedData;
    } else {
      return [];
    }
  }

  Future<List<dynamic>> getYearlyData(int year) async {
    final response = await http
        .get(Uri.parse("https://palaceD.vipulagrahari.repl.co/api/get/$year"));

    if (response.statusCode == 200) {
      String data = response.body;
      var decodedData = jsonDecode(data);

      return decodedData;
    } else {
      return [];
    }
  }

  Future<List<dynamic>> postData(
      String year,
      String company,
      String jobprof,
      String jobdesc,
      String remarks,
      String venue,
      String date,
      String eligibility,
      String ctc,
      String college) async {
    var headers = {
      'Content-Type': 'application/json',
    };

    var request = http.Request(
        'POST', Uri.parse("https://palaceD.vipulagrahari.repl.co/api/post"));

    request.body = '''{
    "Year": "$year",
    "company_name": "$company",
    "job_prof": "$jobprof",
    "job_desc": "$jobdesc",
    "remarks":"$remarks",
    "venue":"$venue",
    "date":"$date",
    "eligibility":"$eligibility",
    "ctc":"$ctc",
    "college":"$college"
    }''';

    request.headers.addAll(headers);

    http.StreamedResponse response = await request.send();

    if (response.statusCode == 200) {
      String data = await response.stream.bytesToString();
      var decodedData = jsonDecode(data);

      return decodedData;
    } else {
      return [];
    }
  }
}
