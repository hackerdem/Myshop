import redis
from django.conf import settings
from .models import Product

#connection to redis
r=redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.REDIS_DB)

class Recommender(object):

    def get_product_key(self,id):
        return 'product:{}:purchased_with'.format(id)

    def products_bought(self,products):
        products_ids=[p.id for p in products]
        for product_id in product_ids:
            for with_id in product_ids:# get the other products bought with each product
            if product_id!=with_id:
                r.zincrby(self.get_product_key(product_id),with_id,amount=1)

    def suggest_products_for(self,products,max_results=6):
        product_ids=[p.id for p in products]
        if len(products)==1:
            suggestions=r.zrange(self.get_product_key(product_ids[0]),0,-1,desc=True)[:max_results]
        else:
            #generete a temporary key
            flat_ids=''.join([str(id) for id in product_ids])
            tmp_key='tmp_{}'.format(flat_ids)
            
