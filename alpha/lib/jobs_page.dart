import 'package:alpha/NetworkUtilities/network_utilities.dart';
import 'package:flutter/material.dart';

class JobsPage extends StatefulWidget {
  const JobsPage({super.key});

  @override
  State<JobsPage> createState() => _JobsPageState();
}

class _JobsPageState extends State<JobsPage> {
  late List<dynamic> jobData;

  Future _getjobdata() async {
    NetworkUtils ntw = NetworkUtils();

    var data = await ntw.getData();

    return data;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Jobs'),
        leading: IconButton(
          icon: const Icon(Icons.person),
          onPressed: () {},
        ),
      ),
      body: FutureBuilder(
        future: _getjobdata(),
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            jobData = snapshot.data as List<dynamic>;
            return ListView.builder(
              itemCount: jobData.length,
              itemBuilder: (context, index) {
                return Card(
                  child: ListTile(
                    title: Text(jobData[index]['company_name']),
                    subtitle: Text(jobData[index]['job_prof']),
                    trailing: Text(jobData[index]['date']),
                  ),
                );
              },
            );
          } else {
            return const Center(
              child: CircularProgressIndicator(),
            );
          }
        },
      ),
    );
  }
}
