from openerp.osv import osv,fields

class test_module(osv.osv):
    _name = 'test.module'
    _columns={
                'name' : fields.char('Nom', size=128),
                'avatar' : fields.binary("avatar",filters='*.png,*.gif'),
                'code' : fields.char('Code' , size=130),
                'description' : fields.text('Description',size=128)
            }
    def _check_name(self,cr,uid,ids):
        for i in self.browse(cr,uid,ids):
            if 'spam' in i.name : return False
        return True 
    
    _sql_constraints =[('name_uniq','unique(name)','Nom doit etre unique')]
    _constraints=[( _check_name, 'Spam est dans la liste',['name'])]
    
    def print_a(self,cr,uid,ids,context={}):
        return self.write(cr,uid, ids,{'code':'200'},context=context)
    
    def print_b(self,cr,uid,ids,context={}):
        return self.write(cr,uid, ids,{'code': '401'},context=context)
    
    _orders="name asc"