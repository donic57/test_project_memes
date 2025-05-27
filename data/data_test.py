
class DataTest:

    TEST_DATA = [
        {
            "text": 12345,
            "url": "https://ya.ru/",
            "tags": ["test_driver", "test_driver2"],
            "info": {"description": "sdfsdfo", "color": "sdfsdf"}
        },
        {
            "text": "test_text",
            "url": "https://ya.ru/",
            "tags": "test_driver2",
            "info": {"description": "sdfsdfo", "color": "sdfsdf"}
        },
        {
            "text": "test_text",
            "url": "https://ya.ru/",
            "tags": ["test_driver", "test_driver2"],
            "info": ["driver", "driver2"]
        },
    ]

    TEST_DATA_OK = [
        {
            "text": "",
            "url": "https://ya.ru/",
            "tags": ["test_driver", "test_driver2"],
            "info": {"description": "test_info"}
        },
        {
            "text": "test_text",
            "url": "",
            "tags": ["test_driver", "test_driver2"],
            "info": {"description": "test_info"}
        },
        {
            "text": "Спасибо всем народам, которые дружат за 3 выходных",
            "url": "https://www.memify.ru/meme/128787/",
            "tags": ["kotey", "andrey"],
            "info": {"description": "test_info"}
        }
    ]

    TEST_DATA_BAD = [
        {
            "id": '354',
         "text": "test_text",
         "url": "https://ya.ru/",
         "tags": ["test_driver", "test_driver2"],
         "info": {"description": "sdfsdfo", "color": "sdfsdf"}
        },
        {
            "id": 354,
         "text": 12345,
         "url": "https://ya.ru/",
         "tags": ["test_driver", "test_driver2"],
         "info": {"description": "sdfsdfo", "color": "sdfsdf"}
        },
        {
            "id": 354,
         "text": "test_text",
         "url": "https://ya.ru/",
         "tags": "test_driver2",
         "info": {"description": "sdfsdfo", "color": "sdfsdf"}
        },
        {
            "id": 354,
         "text": "test_text",
         "url": "https://ya.ru/",
         "tags": ["test_driver", "test_driver2"],
         "info": ["driver", "driver2"]
        },
        {
            "id": 354,
         "text": "",
         "url": "https://ya.ru/",
         "tags": ["test_driver", "test_driver2"],
         "info": ["driver", "driver2"]
        },
        {
            "id": 354,
         "text": "test_text",
         "url": "",
         "tags": ["test_driver", "test_driver2"],
         "info": ["driver", "driver2"]
        }
    ]
