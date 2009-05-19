from django.db import models
from extdirect.interfaces import IExtDirectProvider
from zope import component, interface

class AbstractBase(models.Model):

    class Meta:
        abstract = True

    @classmethod
    def add(klass, **kw):
        c = klass(**kw)
        c.save()
        return "instance saved."

    @classmethod
    def remove(klass, **kw):
        c = klass.objects.get(pk=kw['ide'])
        c.delete()
        return "instance deleted."

    @classmethod
    def getAll(klass):
        objects = klass.objects.all()
        cs = []
        for c in objects:
            cs.append({'id': c.id})

        return cs        
       
class IClientAPI(interface.Interface):
    """
    Clients API
    """

    def add(name):
        """
        Create a new client instance
        """
        pass
    def remove(ide):
        """
        Remove the client by id
        """
        pass
    def getAll():
        """
        Return all the clients instances
        """
        pass
    def getById(ide):
        """
        Return a client by id
        """
       
 
class ISellerAPI(interface.Interface):
    """
    Sellers API
    """
    
    def add(first_name, last_name, address, telephone, email):
        """
        Create a new seller instance
        """
        pass
    
    def remove(ide):
        """
        Remove the seller by id
        """
        pass
        
    def getAll():
        """
        Return all the sellers instances
        """
        pass
    
    def getById(ide):
        """
        Return a seller by id
        """
        pass
               
class Seller(AbstractBase):
    interface.implements(ISellerAPI)
    
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    address = models.CharField(max_length=35)
    telephone = models.CharField(max_length=35)
    email = models.CharField(max_length=35)    
    
    
class Client(AbstractBase):
    interface.implements(IClientAPI)
    
    name = models.CharField(max_length=35)
    
        
component.provideUtility(Seller, IExtDirectProvider,name='Seller')
component.provideUtility(Client, IExtDirectProvider, name='Client')
    
