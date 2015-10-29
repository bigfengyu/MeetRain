# __author__ = 'fengyu'
# from django.db.models.signals import pre_delete
# from django.dispatch.dispatcher import receiver
# from blog.models import *
#
# @receiver(pre_delete,sender=Category)
# def Category_delete(sender,instance,**kwargs):
#     if instance.order == 0 or instance.order == 1:
#         pass
#     else:
#         instance.delete()
