import db_com
import api

if __name__ == '__main__':
    db_com.init()
    result= db_com.get_product("5901478005243")
    print(result)
    api.run_server()

