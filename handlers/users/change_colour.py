from loader import dp


@dp.callback_query_handler()
async def change_colour(call):
    print(call)