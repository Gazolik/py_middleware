from . import Runner
class Builder:

    def __init__(self, opts=None):
        opts = opts or {}
        self.runner_class = opts.setdefault('runner_class', Runner)
        self.stack = []    

    def use(self, middleware, *args):
        if middleware is Builder:
            self.stack.concat(middleware.stack)
        else:
            self.stack.append([middleware, args])
        return self

    def insert(self, index, middleware, *args):
        self.stack.insert(index, [middleware, args])

    def insert_after(self, index, middleware, *args):
        self.stack.insert(index+1, [middleware, args])

    def delete(self, index):
        self.stack.pop(index)

    def replace(self, index, middleware, *args):
        self.delete(index)
        self.insert(index, middleware, *args)

    def call(self, env=None):
        self.to_app().call(env)
    
    def to_app(self):
        return self.runner_class(self.stack)

