with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

bad_str = """        ]
    }
        ]
    }
]"""

good_str = """        ]
    }
]"""

if bad_str in text:
    text = text.replace(bad_str, good_str)
    with open(r'privet\onyx_reports\app.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Cleaned double brackets!")
else:
    print("Not found, checking...")
