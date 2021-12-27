
#запросы категорий
#выбор основной категории
res = "Select * from sc_categories where type=1;"
#выбирает  id субкатегоий которые входят в указаную категорию 
res2 = "Select * from sc_category_links where rootcatID=757;"