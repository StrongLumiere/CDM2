# data example
patient_data = {
    "ID": [101, 102, 103],  # 환자 ID 목록
    "Name": ["환자A", "환자B", "환자C"],  # 환자 이름 (선택 사항)
    "Visits": [
        [  # 환자 101의 방문 기록
            {"날짜": "2024-04-01", "입원시간": "10:30", "퇴원시간": "13:00", "ktas": "Level 1",
             "HR": [72, 75, 78], "SBP": [120, 122, 124], "DBP": [80, 82, 84], "DRUG": ["Drug A", "Drug B"]},
            {"날짜": "2024-05-15", "입원시간": "09:00", "퇴원시간": "11:30", "ktas": "Level 2",
             "HR": [70, 73, 76], "SBP": [118, 120, 122], "DBP": [78, 80, 82], "DRUG": ["Drug C"]}
        ],
        [  # 환자 102의 방문 기록
            {"날짜": "2024-04-02", "입원시간": "12:15", "퇴원시간": "15:00", "ktas": "Level 2",
             "HR": [95, 98, 100], "SBP": [150, 148, 145], "DBP": [90, 88, 85], "DRUG": ["Drug D"]},
            {"날짜": "2024-06-20", "입원시간": "14:00", "퇴원시간": "16:45", "ktas": "Level 3",
             "HR": [90, 92, 95], "SBP": [140, 138, 135], "DBP": [85, 83, 80], "DRUG": ["Drug E", "Drug F"]}
        ],
        [  # 환자 103의 방문 기록
            {"날짜": "2024-04-03", "입원시간": "14:45", "퇴원시간": "17:30", "ktas": "Level 3",
             "HR": [88, 85, 82], "SBP": [130, 128, 126], "DBP": [85, 83, 81], "DRUG": ["Drug H", "Drug I"]}
        ]
    ]
}



def display_tab1():
    print(1)
    