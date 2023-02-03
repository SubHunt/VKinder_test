from modules.bot import start_VK_bot
from modules.vkinder_db import drop_tables, create_tables
import psycopg2

if __name__ == '__main__':
    drop_tables()
    create_tables()
    start_VK_bot()



