{
  "targets": [
    {
      "target_name": "binding",
      "sources": [
        "src/binding.cc"
      ],
      'defines': [ 'V8_DEPRECATION_WARNINGS=1' ],
      'include_dirs': [
      ],
      'libraries': [
        '-llibtesseract',
        '-lleptonica'
      ]
    }
  ]
}
