with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

bad_end = """     ) WHERE ROWNUM<=300"""},
 ]}
        ]
    }
]"""

good_end = """     ) WHERE ROWNUM<=300"""},
 ]}
]"""

if bad_end in text:
    text = text.replace(bad_end, good_end)
    with open(r'privet\onyx_reports\app.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Cleaned TABS end brackets!")
else:
    print("Not found")
