import Model
import View

class Control():
    def __init__(self):
        self.model = Model.Model(self)
        self.view = View.View(self)

    def start(self):
        self.view.start()

    def get_tasks(self):
        return self.model.db.fetch_all()

    def get_task(self, id):
        return self.model.db.fetch(id)

    def create_task(self, title, importance, urgency, detail, memo):
        task = Model.TableItem(0, True, title, importance, urgency, detail, memo)
        self.model.db.insert(task)

    def get_daily(self):
        tasks = self.model.db.fetch_all()
        return self.model.daily_gen.generate(tasks)
