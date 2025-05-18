import 'dart:io';
import 'package:google_ml_vision/google_ml_vision.dart';

class OCRService {
  Future<String> extractTextFromImage(String filePath) async {
    try {
      final File imageFile = File(filePath);
      final GoogleVisionImage visionImage = GoogleVisionImage.fromFile(imageFile);
      final TextRecognizer textRecognizer = GoogleVision.instance.textRecognizer();

      final VisionText visionText = await textRecognizer.processImage(visionImage);
      textRecognizer.close();

      // Safely handle nullability
      return visionText.text ?? "No text found"; // Provide a fallback string if null
    } catch (e) {
      print('OCR Error: $e');
      return 'Error extracting text';
    }
  }
}

