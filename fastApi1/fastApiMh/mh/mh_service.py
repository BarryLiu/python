from db import get_a_conn

import random

class m_service():
    
    def service_home_comic():
        print('service_home_comic:')
        mysql = get_a_conn()
        blockList = mysql.fetchall('select id as id ,img_url as cover,title as title,description as description from t_wwbook limit 5');
        
        start_index = random.randint(1,500);
        banner = mysql.fetchall('select id as id , banner_img_url as banner_img_url from t_wwbook limit %s , 3'%start_index);
        
        recommendEveryDay = mysql.fetchone('select id as id ,img_url as cover,title as title,description as description,tags from t_wwbook  limit 1');

        # for item in result:
        #     print('item:',item)
        
        res = {
            "banner":banner,
            "blockList":blockList,
            "recommendEveryDay":{},
            "updateTodayList":[]
        }
        return res
    def service_home_comic_page(keyword: str = None,skip: int = 0, limit: int = 10):
        mysql = get_a_conn()
        sql = ""
        if keyword:
            sql.join(" and title like %")
        blockList = mysql.fetchall("select id as id ,img_url as cover,title as title,description as description from t_wwbook where 1=1 limit %s,%s"%(skip,limit));



        res = {
            "banner":[],
            "blockList":blockList,
            "recommendEveryDay":{},
            "updateTodayList":[]
        }
        return res


    def service_comic_detail(id:int):
        mysql = get_a_conn()
        detail = mysql.fetchone("select * from t_wwbook where id = %s"%id)

        return detail
    
    def service_comic_detail_tab2(id:int):
        mysql = get_a_conn()
        categoryList = mysql.fetchall("select id as id ,title,img_url from t_wwbook_item where book_id = %s"%id)

        return {
            "categoryList": categoryList
        }

    def service_reader_image(item_id):
        mysql = get_a_conn()
        sql = """
        select id,
        (
            SELECT id from t_wwbook_item where book_id = wi.book_id AND seq < wi.seq ORDER BY seq desc limit 1
        ) as prev_id,
        (
            SELECT id from t_wwbook_item where book_id = wi.book_id AND seq > wi.seq ORDER BY seq ASC limit 1
        ) as next_id,
        img_urls from t_wwbook_item wi where id = %s
        """
        rtn = mysql.fetchone(sql%item_id)
        #print('img_urls',img_urls)
        comicPictureList = rtn['img_urls'].split(',')
        return {
            "prev_id":rtn["prev_id"],
            "next_id":rtn["next_id"],
            "comicPictureList":comicPictureList
        }