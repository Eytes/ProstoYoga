from prostoyoga.database import users


def create_user(first_name: str, phone: str, tg_id: str = None, last_name: str = None, pather_name: str = None) -> None:
    users.insert_one(
        {
            'tg_id': tg_id,
            'firs_name': first_name,
            'last_name': last_name,
            'pather_name': pather_name,
            'phone': phone,
            'role': 'user',
            'subscription': {
                "start_date": None,
                "end_date": None,
                "remaining_visits": 0,
                "visits": []
            }
        }
    )



def deposit(): ...


def get_user_visits(): ...


def get_last_user_visit(): ...


def change_user_profile(): ...


def get_user(): ...
