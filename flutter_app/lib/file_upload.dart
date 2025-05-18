import 'package:file_picker/file_picker.dart';

class FileUploader {
  Future<String?> pickFile() async {
    try {
      FilePickerResult? result = await FilePicker.platform.pickFiles(
        type: FileType.custom,
        allowedExtensions: ['jpg', 'png', 'pdf'], // Add supported formats
      );

      if (result != null) {
        return result.files.single.path; // Return file path
      } else {
        return null; // User canceled the picker
      }
    } catch (e) {
      print('Error picking file: $e');
      return null;
    }
  }
}
