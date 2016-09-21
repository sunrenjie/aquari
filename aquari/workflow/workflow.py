import copy

router = {}


class StepBasic(object):
    def __init__(self, workflow):
        self.workflow = workflow


class StepCreate(StepBasic):
    fields = None

    @classmethod
    def get_empty_form(cls):
        router['StepCreate'] = cls
        fd = {}
        for f in cls.fields:
            fd[f] = None
        return {
            'form': {
                'post_to': 'StepCreate',
                'fields': fd
            }
        }

    def create(self):




class StepCreateOrderVM(StepCreate):
    fields = ['username', 'project', 'contact', '#vms']


class StepConfirm(StepBasic):
    pass


class WorkflowBasic(object):
    steps = None

    def __init__(self):
        self.step_objects = [c(self) for c in self.steps]

    def get_empty_form(self):
        return self.step_objects[0].get_empty_form()


class WorkflowCreateOrder(WorkflowBasic):
    steps = [StepCreateOrderVM, StepConfirm]


def user():
    ret = WorkflowCreateOrder().get_empty_form()
    addr = ret['form']['post_to']
    fields = copy.deepcopy(ret['fields'])
    for f in fields:
        fields[f] = f + ' to be filled by user'
    c = router[addr]
    cc = c.create()

