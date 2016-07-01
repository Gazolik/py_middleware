class EmptyMiddleWare:
    def __init__(self, app, *args):
        self.app = None

    def call(self, env):
        pass


class Runner:
    
    def __init__(self, stack):
        self.kickoff = self.build_call_chain(stack)


    def call(self, env):
        self.kickoff.call(env)

    def build_call_chain(self, stack):
        call_stack = []
        last = EmptyMiddleWare(None)
        call_stack.append(last)
        for klass, args in reversed(stack):
          last = klass(last, args)
        return last
