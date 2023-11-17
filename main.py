# here, all packages/files are brought together to build the full app.

class Main:
  def __init__(self, app):
    self.app = app

  def run(self):
    return self.app()


new_app = Main(lambda: print("Welcome"))

new_app.run()
