
fix_data = dict ({"place": "дом",
    "time_action": "08:00:00",
    "action": "действие",
    "nice": True,
    "related": None,
    "reward": None,
    "time": 1,
    "public": False,
    "user": 1,
    "period": "1,2,4"
                 })

# 422
# Unprocessable Entity
"""
{
    "error": "ValidationError",
    "serial": "Связанная привычка не 'приятная'"
}
"""
"""
{
    "error": "ValidationError",
    "serial": "одновременный выбор 'related' и 'reward'."
}
"""
"""
{
    "error": "ValidationError",
    "serial": "должно быть в пределах 1-120 секунд."
}
"""
"""
{
    "error": "ValidationError",
    "serial": "У 'приятной' не должно быть связанной или вознаграждения"
}
"""
"""
{
    "error": "ValidationError",
    "serial": "period должно быть в пределе '1,2,3,4,5,6,0'."
}
"""