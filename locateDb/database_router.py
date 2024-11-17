class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'search1':
            return 'default' 
        elif model._meta.db_table == 'search2':
            return 'db2' 
        elif model._meta.db_table == 'search3':
            return 'db3'  
        return None

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None
