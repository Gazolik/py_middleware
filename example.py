from py_middleware import Runner, Builder

class Trace:
  def __init__(self, app, value):
    self.app=app
    self.value=value

  def call(self, env):
    print('--> %s' % self.value)
    self.app.call(env)
    print('<-- %s' % self.value)

stack = Builder()

stack.use(Trace, "A")
stack.use(Trace, "B")
stack.use(Trace, "C")

stack.call(None)
