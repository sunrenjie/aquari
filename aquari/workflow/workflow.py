import copy
import json
import uuid


router = {}
flow_data = {}

projects = [
    {
        'username': 'foo',
        'project': 'foo-project',
        'contact': None,
    },
    {
        'username': 'foo',
        'project': 'foo-project-2',
        'contact': None,
    },
    {
        'username': 'bar',
        'project': 'bar-project',
        'contact': 'Mr. Bar',
    }
]


class StepBasic(object):
    def __init__(self, workflow):
        self.workflow = workflow

    def get_pos(self):
        return self.workflow.get_step_pos(self.__class__)

    def upon_done(self):
        self.workflow.pos_inc()


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

    def create(self, data):
        d = {}
        for f in self.fields:
            d[f] = data.get(f, None)
        pos = self.get_pos()
        flow_data[self.workflow.id][pos] = json.dumps(d)


class StepCreateOrderVM(StepCreate):
    fields = ['username', 'project', 'contact', '#vms']


class StepConfirm(StepBasic):
    pass


class WorkflowBasic(object):
    steps = None
    step2pos = None

    def __init__(self):
        self.step_objects = [c(self) for c in self.steps]
        self.pos = 0
        self.id = self.gen_new_id()
        assert self.id not in flow_data
        flow_data[self.id] = {}

    @classmethod
    def get(cls):
        return cls.steps[0].get_empty_form()

    @classmethod
    def post(cls, data):
        flow = cls()  # create the workflow instance now
        e = flow.step_objects[0]
        try:
            e.create(data)
        except Exception as ex:
            print(ex)
            raise
        # Now create succeeds,
        return flow

    @staticmethod
    def gen_new_id():
        return uuid.uuid4()

    @classmethod
    def get_step_pos(cls, step):
        if not cls.step2pos:
            cls.step2pos = {}
            for i in xrange(0, len(cls.steps)):
                # TODO extend the system if the steps are duplicated
                assert cls.steps[i] not in cls.step2pos
                cls.step2pos[cls.steps[i]] = i
        return cls.step2pos[step]

    def pos_get(self):
        return self.pos

    def pos_set(self, pos):
        self.pos = pos

    def pos_inc(self):
        if self.pos < len(self.steps):
            self.pos += 1



class WorkflowCreateOrder(WorkflowBasic):
    steps = [StepCreateOrderVM, StepConfirm]


def user():
    ret = WorkflowCreateOrder.get()
    addr = ret['form']['post_to']
    fields = copy.deepcopy(ret['form']['fields'])
    for f in fields:
        fields[f] = f + ' to be filled by user'
    fields['username'] = 'foo'
    fields['project'] = 'foo-project'
    cc = WorkflowCreateOrder.post(fields)
    print(cc)


user()
