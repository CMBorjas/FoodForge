import 'package:flutter/material.dart';
import 'file_upload.dart';
import 'ocr_service.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: FileUploadPage(),
    );
  }
}

class FileUploadPage extends StatelessWidget {
  final FileUploader fileUploader = FileUploader();
  final OCRService ocrService = OCRService(); // Initialize the OCR service

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Upload and Extract Text')),
      body: Center(
        child: ElevatedButton(
          onPressed: () async {
            String? filePath = await fileUploader.pickFile(); // Pick a file
            if (filePath != null) {
              print('File selected: $filePath');
              ScaffoldMessenger.of(context).showSnackBar(
                SnackBar(content: Text('File selected: $filePath')),
              );

              // Perform OCR on the selected file
              String extractedText = await ocrService.extractTextFromImage(filePath);
              print('Extracted Text: $extractedText');

              // Display the extracted text in a dialog
              showDialog(
                context: context,
                builder: (context) {
                  return AlertDialog(
                    title: Text('Extracted Text'),
                    content: SingleChildScrollView(
                      child: Text(extractedText),
                    ),
                    actions: [
                      TextButton(
                        onPressed: () => Navigator.of(context).pop(),
                        child: Text('OK'),
                      ),
                    ],
                  );
                },
              );
            } else {
              ScaffoldMessenger.of(context).showSnackBar(
                SnackBar(content: Text('No file selected.')),
              );
            }
          },
          child: Text('Upload and Extract Text'),
        ),
      ),
    );
  }
}
